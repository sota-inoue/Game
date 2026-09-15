
from Display.Renderer.renderer_manager import RendererManager

from Display.Output.output_manager import OutputManager

from Domain.game_flag import TitleState, GameOverState, ClearState, OpeningState

class DisplayManager:
    def __init__(self, mode: bool):
        self._output = OutputManager(mode)
        GAME_SCREEN_WIDTH = self._output.GAME_SCREEN_WIDTH
        GAME_SCREEN_HEIGHT = self._output.GAME_SCREEN_HEIGHT
        TOUCH_SCREEN_WIDTH = self._output.TOUCH_SCREEN_WIDTH
        TOUCH_SCREEN_HEIGHT = self._output.TOUCH_SCREEN_HEIGHT
        self._renderer = RendererManager(GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT, TOUCH_SCREEN_WIDTH, TOUCH_SCREEN_HEIGHT)
        self._width = GAME_SCREEN_WIDTH
        self._height = GAME_SCREEN_HEIGHT

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height


    def output(self):
        # ゲーム画面の描画結果を取得する
        game_display = self._renderer.get_game()

        # タッチ操作画面の描画結果を取得する
        touch_display = self._renderer.get_touch()

        # 取得した2つの画面をディスプレイに反映する
        self._output.output(game_display, touch_display)


    def draw_Opening(self, state: OpeningState):
        self._renderer.draw_Opening(state)

    def draw_Over(self, state: GameOverState):
        self._renderer.draw_Over(state)

    def draw_Title(self, state: TitleState):
        self._renderer.draw_Title(state)
    
    def draw_Clear(self, state: ClearState):
        self._renderer.draw_Clear(state)

    def draw_Ending(self):
        self._renderer.draw_Ending()

    def draw_Stage(self):
        self._renderer.draw_Stage()



    def draw_stage_object(self, player_data, attack_date,map_data):
        self._renderer.draw_stage_object(player_data, attack_date, map_data)

    def draw_urgency_level(self, hp):
        self._renderer.draw_urgency_level(hp)

    def touch_render(self):
        self._renderer.touch_render()

    def touch_iamge_render(self):
        self._renderer.touch_iamge_render()