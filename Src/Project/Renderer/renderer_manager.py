import pygame
from Renderer.touch_renderer import TouchDisplay
from Renderer.game_renderer import GameDisplay
from Renderer.stage_renderer import StageObjectDraw, PlayerDraw
from Renderer.ui_renderer import UIRenderer

from Renderer.image_manager import ImageManager
from System.file_load_system import load_image

from Domain.config import GRAY

from Domain.asset_paths import (
    PLAYER_IMAGE_PATH,
)


class Renderer:
    def __init__(self,DISPLAY_WIDTH,DISPLAY_HEIGHT,TOUCH_WIDTH,TOUCH_HEIGHT):
        image = ImageManager()
        PLAYER_IMAGE = load_image(PLAYER_IMAGE_PATH)
        self.game_surface = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT), depth=16)
        self.touch_surface = pygame.Surface((TOUCH_WIDTH, TOUCH_HEIGHT), depth=16)

        self.touch = TouchDisplay(TOUCH_WIDTH, TOUCH_HEIGHT)
        self.game = GameDisplay(DISPLAY_WIDTH, DISPLAY_HEIGHT)
        self.stage = StageObjectDraw(image)
        self.ui = UIRenderer(DISPLAY_WIDTH, DISPLAY_HEIGHT)
        self.player = PlayerDraw(DISPLAY_WIDTH, DISPLAY_HEIGHT, PLAYER_IMAGE)

    def get_game(self):
        return self.game_surface

    def get_touch(self):
        return self.touch_surface


    def touch_render(self):
        self.touch.draw_Controller(self.touch_surface)
    
    def draw_Title(self, title_state):
        self.game.draw_Title(self.game_surface, title_state)

    def draw_Opening(self):
        self.game.draw_Opening(self.game_surface)
    
    def draw_Over(self):
        self.game.draw_Over(self.game_surface)
    
    def draw_Clear(self):
        self.game.draw_Clear(self.game_surface)



    def draw_Stage(self):
        self.game_surface.fill(GRAY)
    
    def draw_Player(self, x, y):
        self.player.draw(self.game_surface, x, y)

    def stage_render(self, data):
        self.stage.draw(self.game_surface, data)

    def draw_UI(self, hp):
        self.ui.health_draw(self.game_surface, hp)

    