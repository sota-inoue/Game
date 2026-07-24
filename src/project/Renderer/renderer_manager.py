import pygame
from Renderer.stage_renderer import StageDraw
from Renderer.touch_renderer import TouchDisplay
from Renderer.game_renderer import GameDisplay
class Renderer:

    def __init__(
        self,
        DISPLAY_WIDTH,
        DISPLAY_HEIGHT,
        TOUCH_WIDTH,
        TOUCH_HEIGHT
    ):
        self.game_surface = pygame.Surface(
            (DISPLAY_WIDTH, DISPLAY_HEIGHT),
            depth=16
        )

        self.touch_surface = pygame.Surface(
            (TOUCH_WIDTH, TOUCH_HEIGHT),
            depth=16
        )

        self.stage = StageDraw(DISPLAY_WIDTH, DISPLAY_HEIGHT)
        self.touch = TouchDisplay(TOUCH_WIDTH, TOUCH_HEIGHT)
        self.game = GameDisplay(DISPLAY_WIDTH, DISPLAY_HEIGHT)

    def clear(self):
        self.game_surface.fill((255, 255, 255))
        self.touch_surface.fill((0, 0, 0))

    def stage_render(self, data):
        self.stage.draw(self.game_surface, data)

    def player_render(self, player_x, player_y):
        self.stage.player_draw(self.game_surface, player_x, player_y)

    def touch_render(self):
        self.touch.draw_Controller(self.touch_surface)

    def draw_Title(self):
        self.game.draw_Title(self.game_surface)

    def draw_Opening(self):
        self.game.draw_Opening(self.game_surface)

    def draw_Over(self):
        self.game.draw_Over(self.game_surface)

    def draw_Clear(self):
        self.game.draw_Clear(self.game_surface)

    