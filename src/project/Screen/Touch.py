import pygame


class TouchDisplay:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.Surface((self.width, self.height))

    def draw(self):
        self.surface.fill((0, 0, 0))

        pygame.draw.rect(
            self.surface,
            (255, 0, 0),
            (50, 50, 150, 100)
        )

        pygame.draw.circle(
            self.surface,
            (0, 255, 0),
            (300, 160),
            50
        )