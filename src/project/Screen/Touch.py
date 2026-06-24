import pygame

class TouchDisplay:
    WIDTH = 480
    HEIGHT = 320
    BACK_COLOR = (90, 90, 90)

    def __init__(self):
        self.surface = pygame.Surface((self.WIDTH, self.HEIGHT))

    def draw(self):
        self.surface.fill(self.BACK_COLOR)

