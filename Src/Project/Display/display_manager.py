import pygame

from Display.Renderer.touch_renderer import TouchDisplay
from Display.Renderer.game_renderer import GameDisplay
from Display.Renderer.object_renderer import StageObjectDraw
from Display.Renderer.ui_renderer import UIRenderer
from Display.Renderer.image_manager import ImageManager

from Display.Layout.layout_manager import Layout

from Display.Output.output_manager import OutputManager

from State.game_flag import TitleSceneSelection, OpeningPage, GameOverSceneSelection, GameClearSceneSelection, PauseSceneSelection

class DisplayManager:
    def __init__(self, mode: bool):
        self._mode = mode
        self._output = OutputManager(mode)
        DISPLAY_WIDTH = self._output.GAME_SCREEN_WIDTH
        DISPLAY_HEIGHT = self._output.GAME_SCREEN_HEIGHT
        TOUCH_WIDTH = self._output.TOUCH_SCREEN_WIDTH
        TOUCH_HEIGHT = self._output.TOUCH_SCREEN_HEIGHT

        self._game_surface = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT), depth=16)
        self._touch_surface = pygame.Surface((TOUCH_WIDTH, TOUCH_HEIGHT), depth=16)

        self._save_surface = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT), depth=16)

        self._layout = Layout(DISPLAY_WIDTH, DISPLAY_HEIGHT)
        self._image = ImageManager()

        self._object = StageObjectDraw(self._game_surface, self._image, self._layout)

        self._ui = UIRenderer(self._game_surface, self._image)

        self._game = GameDisplay(self._game_surface, self._image)

        self._touch = TouchDisplay(self._touch_surface, self._image)

        self._width = DISPLAY_WIDTH
        self._height = DISPLAY_HEIGHT

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def save_surface(self) -> None:
        # 現在のゲーム画面を保存する
         self._save_surface.blit(self._game_surface, (0, 0))

    def load_surface(self) -> None:
        # 保存したゲーム画面を復元する
        self._game_surface.blit(self._save_surface, (0, 0))


    def draw_black_overlay(self) -> None:
        overlay = pygame.Surface((self._width, self._height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 100))
        self._game_surface.blit(overlay, (0, 0))


    def output(self):
        # 取得した2つの画面をディスプレイに反映する
        self._output.output(self._game_surface, self._touch_surface)

    def fb_close(self):
        self._output.fb_close()


    def draw_opening(self, state: OpeningPage):
        self._game.draw_opning(state)

    def draw_over(self, state: GameOverSceneSelection):
        self._game.draw_over(state)

    def draw_title(self, state: TitleSceneSelection):
        self._game.draw_title(state)
    
    def draw_clear(self, state: GameClearSceneSelection):
        self._game.draw_clear(state)

    def draw_pause(self, state: PauseSceneSelection):
        self._game.draw_pause(state)

    def draw_ending(self):
        self._game.draw_ending()

    def draw_stage(self):
        self._game.draw_stage1_bg()



    def draw_stage_object(self, player_data, map_data, attack_data):
        self._object.draw(player_data, map_data, attack_data)


    def draw_urgency_level(self, hp):
        self._ui.health_draw(hp)

    def touch_render(self):
        self._touch.draw_controller()

    def touch_iamge_render(self):
        self._touch.draw_controller_image()