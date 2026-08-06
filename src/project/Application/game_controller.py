import pygame
from Domain.state import Command

# 入力処理を管理するクラス
from Input.input_manager import Input

# ゲーム内の状態を管理するクラス
from Domain.state import State, GameState

# 描画処理を管理するクラス
from Renderer.renderer_manager import Renderer

# ゲームの進行や内部処理を管理するクラス
from System.system_manager import System

# 画面への出力処理を管理するクラス
from Display.display_manager import Display


class Controller:
    def __init__(self,mode):
        self.mode = mode
        pygame.init()
        self.state = State()
        self.display = Display(mode)
        self.input = Input(mode)
        self.renderer = Renderer(
            self.display.GAME_SCREEN_WIDTH,
            self.display.GAME_SCREEN_HEIGHT,
            self.display.TOUCH_SCREEN_WIDTH,
            self.display.TOUCH_SCREEN_HEIGHT
        )
        self.system = System(self.display.GAME_SCREEN_WIDTH, self.display.GAME_SCREEN_HEIGHT)

        # デバッグ用の変数
        self.saved_command = Command.STAY
        self.saved_map_data = None

    def get_event(self):
        x, y = self.input.get_input()
        self.state.set_input_x(x)
        self.state.set_input_y(y)

    def proggress_update(self):
        game_state = self.state.get_game_state()
        count = self.state.get_count()
        input_x = self.state.get_input_x()
        input_y = self.state.get_input_y()
        new_state = self.system.progress_update(game_state, input_x, input_y, count)
        self.state.set_game_state(new_state)

        if new_state != game_state:
            self.state.set_count(0)
        else:
            self.state.set_count(count + 1)

    def command_update(self):
        input_x = self.state.get_input_x()
        input_y = self.state.get_input_y()
        command = self.system.command_update(input_x, input_y)
        count = self.state.get_count()

        # 入力があった場合だけ一時保存
        if command != Command.STAY:
            self.saved_command = command

        # デバッグログ
        print(f"{count:03d} : input = ({input_x}, {input_y}) : saved = {self.saved_command.name} ")

        # 5フレームに1回、保存した命令を反映
        if count > 0 and count % 5 == 0:
            self.system.player_set_locate(self.saved_command)
            self.state.set_game_command(self.saved_command)
            self.saved_command = Command.STAY

    def player_move(self):
        player_x, player_y = self.system.player_update()
        self.state.set_player_x(player_x)
        self.state.set_player_y(player_y)

    def player_position_update(self):
        command = self.state.get_game_command()
        player_x, player_y = self.state.get_player_position()
        new_position = self.system.player_position_update(command, player_x, player_y)
        self.state.set_player_position(new_position)

    def collision_check(self):
        stage_data = self.state.get_front_map_data()
        self.saved_map_data = stage_data
        player_x, player_y = self.state.get_player_position()
        collision = self.system.collision_update(stage_data, player_x, player_y)
        self.state.set_collision(collision)

    def health_update(self):
        hp = self.state.get_urgency_level()
        count = self.state.get_count()
        collision = self.state.get_collision()
        new_hp = self.system.health_update(hp, count, collision)
        self.state.set_urgency_level(new_hp)

    def map_updata(self):
        count = self.state.get_count()
        map_data = self.state.get_map_data()
        new_map_data = self.system.map_update(map_data, count)
        self.state.set_map_data(new_map_data)

    def system_update(self):
        self.proggress_update()
        game_state = self.state.get_game_state()
        count = self.state.get_count()
        
        if game_state == GameState.STAGE:
            self.command_update()
            self.player_move()
            if count > 0 and count % 5 == 0:
                self.player_position_update()
                self.collision_check()
                self.map_updata()
                self.health_update()

                # デバッグログ
                print(
                    f"command = {self.state.get_game_command().name} : "
                    f"position = {self.state.get_player_position()} : "
                    f"map = {self.saved_map_data} : "
                    f"collision = {self.state.get_collision()} : "
                    f"urgency = {self.state.get_urgency_level()}"
                    )

    def draw(self):
        game_state = self.state.get_game_state()

        if game_state == GameState.TITLE:
            self.renderer.draw_Title()
        elif game_state == GameState.OP:
            self.renderer.draw_Opening()
        elif game_state == GameState.STAGE:
            self.renderer.draw_Stage()
            self.renderer.stage_render(self.state.get_map_data())
            self.renderer.draw_Player(
                self.state.get_player_x(),
                self.state.get_player_y()
            )
            self.renderer.draw_UI(self.state.get_urgency_level())

        elif game_state == GameState.CLEAR:
            self.renderer.draw_Clear()

        self.renderer.touch_render()

    def output(self):
        self.display.update(
            self.renderer.get_game(),
            self.renderer.get_touch()
        )

    def loop(self):
        self.get_event()
        self.system_update()
        self.draw()
        self.output()

        if self.state.get_game_state()== GameState.CLEAR:
            if self.state.get_count() > 30:
                return False

        return True

    
    def close(self):
        if self.mode:
            self.fb.close()
        pygame.quit()