import pygame
from enum import Enum

class Command(Enum):
    LEFT = 0
    JUMP = 1
    RIGHT = 2
    STAY = 3

class GameDisplay:
    BACK_COLOR = (90, 90, 90)
    TEXT_COLOR = (0, 0, 0)
    WIDTH = 600
    HEIGHT = 450

    def __init__(self):
        self.surface = pygame.Surface((self.WIDTH, self.HEIGHT), depth=16)
        self.font = pygame.font.Font(None, 50)
        self.text = "STAY"

    def DrawText(self, text, x, y):
        text_surface = self.font.render(text, True, self.TEXT_COLOR)
        text_width = text_surface.get_width()
        text_height = text_surface.get_height()
        self.surface.blit( text_surface, (x - text_width // 2, y - text_height // 2) )

    def update(self,cmd):
        if cmd == Command.STAY:
            self.text = "STAY"
        elif cmd == Command.LEFT:
            self.text = "LEFT"
        elif cmd == Command.JUMP:
            self.text = "JUMP"
        elif cmd == Command.RIGHT:
            self.text = "RIGHT"
        else:
            return

    def draw(self):
        self.surface.fill(self.BACK_COLOR)

    def draw_Game(self):
        self.surface.fill(self.BACK_COLOR)
        self.DrawText(self.text, self.WIDTH//2, self.HEIGHT//2)
