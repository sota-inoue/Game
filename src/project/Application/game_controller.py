import pygame

# 入力処理を管理するクラス
from Input.input_manager import Input

# ゲーム内の状態を管理するクラス
from Domein.state import State, GameState

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

    def get_event(self):
        x, y = self.input.get_input()
        self.state.set_input_x(x)
        self.state.set_input_y(y)

    def system_update(self):
        game_state = self.state.get_game_state()
        count = self.state.get_count()
        input_x = self.state.get_input_x()
        input_y = self.state.get_input_y()

        new_state = self.system.progress_update(game_state, input_x, input_y, count)
        self.state.set_game_state(new_state)

        if game_state == GameState.STAGE:
            player_x, player_y = self.system.player_update(input_x, input_y)
            print(player_x, player_y)
            self.state.set_player_x(player_x)
            self.state.set_player_y(player_y)


        
        if game_state == GameState.STAGE and count % 5 == 0:
            updated_map_data = self.system.map_update(
                self.state.get_map_data(),
                count
            )
            self.state.set_map_data(updated_map_data)


        if new_state != game_state:
            self.state.set_count(0)
        else:
            self.state.set_count(count + 1)
    
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

        if self.state.get_count() > 100:
            return False

        return True

    
    def close(self):
        if self.mode:
            self.fb.close()
        pygame.quit()