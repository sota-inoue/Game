import pygame

class TouchDisplay:

    WIDTH = 480
    HEIGHT = 320

    def __init__(self):

        self.surface = pygame.Surface(
            (self.WIDTH, self.HEIGHT),
            depth=16
        )

        self.Draw()

    def draw(self):
        self.surface.fill((0, 0, 0))

        pygame.draw.rect(
            self.surface,
            (255, 0, 0),
            (0, 0, 100, 100)
            )

