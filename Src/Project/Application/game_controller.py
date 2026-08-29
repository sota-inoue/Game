import pygame
from Domain.state import Command

# 入力処理を管理するクラス
from Input.input_manager import Input

# ゲーム内の状態を管理するクラス
from Domain.state import State, GameState, TitleState, Command

# 描画処理を管理するクラス
from Renderer.renderer_manager import Renderer

# ゲームの進行や内部処理を管理するクラス
from System.system_manager import System

# 画面への出力処理を管理するクラス
from Display.display_manager import Display

from Domain.StageObject.stage_object_manager import StageObjectManager



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

        self.stageobject = StageObjectManager(self.display.GAME_SCREEN_WIDTH, self.display.GAME_SCREEN_HEIGHT)

        # デバッグ用の変数
        self.saved_command = Command.STAY
        self.saved_map_data = None

        #self.system.play_TitleBGM()
        self.loop_flug = True

    def get_event(self):
        x, y = self.input.get_input()
        self.state.set_input_x(x)
        self.state.set_input_y(y)


    def command_update(self):
        input_x = self.state.get_input_x()
        input_y = self.state.get_input_y()
        command = self.system.command_update(input_x, input_y)
        count = self.state.get_count()

        # 入力があった場合だけ一時保存
        if command != Command.STAY:
            self.saved_command = command

        # デバッグログ
        # print(f"{count:03d} : input = ({input_x}, {input_y}) : saved = {self.saved_command.name} ")

        # 5フレームに1回、保存した命令を反映
        if count > 0 and count % 5 == 0:
            
            self.state.set_game_command(self.saved_command)
            if self.saved_command != Command.STAY:
                self.system.play_PushButton()
            self.saved_command = Command.STAY

    def player_move(self):
        player_x, player_y = self.system.player_update()
        self.stageobject.set_player_locate(player_x, player_y)

    def player_position_update(self):
        command = self.state.get_game_command()
        self.stageobject.player_hitbox_update(command)

    def map_updata(self):
        count = self.state.get_count()
        new_lean = self.system.get_map_date(count)
        self.stageobject.map_update(new_lean)


    def title_system(self):
        self.command_update()
        count = self.state.get_count()
        if count <= 0 or count % 5 != 0:
            return

        title_state = self.state.get_title_state()
        cmd = self.state.get_game_command()

        if title_state == TitleState.START:
            if cmd == Command.JUMP:
                self.state.set_game_state(GameState.OP)
                self.state.set_game_command(Command.STAY)

            elif cmd == Command.RIGHT:
                self.state.set_title_state(TitleState.SETTING)

        elif title_state == TitleState.SETTING:
            if cmd == Command.RIGHT:
                self.state.set_title_state(TitleState.EXIT)

            elif cmd == Command.LEFT:
                self.state.set_title_state(TitleState.START)

        elif title_state == TitleState.EXIT:
            if cmd == Command.JUMP:
                self.loop_flug = False

            elif cmd == Command.LEFT:
                self.state.set_title_state(TitleState.SETTING)



    def system_update(self):
        game_state = self.state.get_game_state()
        count = self.state.get_count()

        if game_state == GameState.TITLE:
            self.title_system()

        elif game_state == GameState.OP:
            if count == 20:
                self.state.set_game_state(GameState.STAGE)
                self.state.set_game_command(Command.STAY)

        elif game_state == GameState.STAGE:
            self.command_update()
            self.player_move()

            if count > 0 and count % 5 == 0:
                cmd = self.state.get_game_command()
                self.system.player_set_locate(cmd)
                self.player_position_update()
                self.stageobject.player_hit_check()
                self.map_updata()

            if count == 100:
                self.state.set_game_state(GameState.CLEAR)

                # デバッグログ
                # print(
                #     f"command = {self.state.get_game_command().name} : "
                #     f"position = {self.state.get_player_position()} : "
                #     f"map = {self.saved_map_data} : "
                #     f"collision = {self.state.get_collision()} : "
                #     f"urgency = {self.state.get_urgency_level()}"
                #     )

        count = self.state.get_count()
        self.state.set_count(count + 1)

    def draw(self):
        game_state = self.state.get_game_state()

        if game_state == GameState.TITLE:
            title_state = self.state.get_title_state()
            self.renderer.draw_Title(title_state)

        elif game_state == GameState.OP:
            self.renderer.draw_Opening()

        elif game_state == GameState.STAGE:
            self.renderer.draw_Stage()

            map_data = self.stageobject.get_draw_data()
            player_data = self.stageobject.get_player_draw_data()

            self.renderer.draw_stage_object(player_data, map_data)

            self.renderer.draw_UI(self.stageobject.get_urgency_level())

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
        return self.loop_flug

    
    def close(self):
        if self.mode:
            self.fb.close()
        pygame.quit()