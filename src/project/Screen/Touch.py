import pygame


class TouchDisplay:

    def __init__(self):
        self.WIDTH = 480
        self.HEIGHT = 320
        self.surface = pygame.Surface( (self.WIDTH, self.HEIGHT), depth=16)
        self.Draw()

    def draw(self):
        self.surface.fill((0, 0, 0))

        pygame.draw.rect(
            self.surface,
            (255, 0, 0),
            (50, 50, 150, 100)
        )
