import pygame
from Display.Renderer.touch_renderer import TouchDisplay
from Display.Renderer.game_renderer import GameDisplay
from Display.Renderer.object_renderer import StageObjectDraw
from Display.Renderer.ui_renderer import UIRenderer

from Display.Renderer.image_manager import ImageManager

from Domain.game_flag import TitleSceneSelection, OpeningPage, GameOverSceneSelection, GameClearSceneSelection


class RendererManager:
    def __init__(self,DISPLAY_WIDTH,DISPLAY_HEIGHT,TOUCH_WIDTH,TOUCH_HEIGHT):
        self._image = ImageManager()
        self._game_surface = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT), depth=16)
        self._touch_surface = pygame.Surface((TOUCH_WIDTH, TOUCH_HEIGHT), depth=16)

        self._object = StageObjectDraw(self._game_surface, self._image)
        self._ui = UIRenderer(self._game_surface, self._image)

        self._game = GameDisplay(self._game_surface, self._image)

        self._touch = TouchDisplay(self._touch_surface, self._image)
        

    def get_game(self):
        return self._game_surface

    def get_touch(self):
        return self._touch_surface


    def draw_Opening(self, state: OpeningPage):
        self._game.draw_opning(state)

    def draw_Over(self, state: GameOverSceneSelection):
        self._game.draw_over(state)

    def draw_Title(self, state: TitleSceneSelection):
        self._game.draw_title(state)
    
    def draw_Clear(self, state: GameClearSceneSelection):
        self._game.draw_clear(state)

    def draw_Ending(self):
        self._game.draw_ending()

    def draw_Stage(self):
        self._game.draw_stage1_bg()



    def draw_stage_object(self, player_data, attack_date,map_data):
        self._object.draw(player_data, attack_date, map_data)

    def draw_urgency_level(self, hp):
        self._ui.health_draw(hp)

    def touch_render(self):
        self._touch.draw_controller()

    def touch_iamge_render(self):
        self._touch.draw_controller_image()