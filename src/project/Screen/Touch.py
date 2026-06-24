import pygame


class TouchDisplay:
    WIDTH = 480
    HEIGHT = 320

    def __init__(self):
        self.surface = pygame.Surface((self.WIDTH, self.HEIGHT), depth=16)

    def draw(self):
        self.surface.fill((0, 0, 0))

        #pygame.draw.rect( self.surface, (255, 0, 0), (50, 50, 150, 100) )
        pygame.draw.circle(self.surface, (0, 255, 0), (300, 160), 50)