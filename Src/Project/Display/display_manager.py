
from Display.Renderer.renderer_manager import RendererManager

from Display.Output.output_manager import OutputManager

from Domain.game_flag import TitleSceneSelection, OpeningPage, GameOverSceneSelection, GameClearSceneSelection

class DisplayManager:
    def __init__(self, mode: bool):
        self._mode = mode
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


    def draw_opening(self, state: OpeningPage):
        self._renderer.draw_Opening(state)

    def draw_game_over(self, state: GameOverSceneSelection):
        self._renderer.draw_Over(state)

    def draw_title(self, state: TitleSceneSelection):
        self._renderer.draw_Title(state)
    
    def draw_game_clear(self, state: GameClearSceneSelection):
        self._renderer.draw_Clear(state)

    def draw_ending(self):
        self._renderer.draw_Ending()

    def draw_stage(self):
        self._renderer.draw_Stage()



    def draw_stage_object(self, player_data, map_data):
        self._renderer.draw_stage_object(player_data, map_data)

    def draw_stage_middle_object(self, player_data, map_data):
        self._renderer.draw_stage_middle_object(player_data, map_data)

    def draw_urgency_level(self, hp):
        self._renderer.draw_urgency_level(hp)

    def touch_render(self):
        self._renderer.touch_render()

    def touch_iamge_render(self):
        self._renderer.touch_iamge_render()


    def fb_close(self):
        self._output.fb_close()