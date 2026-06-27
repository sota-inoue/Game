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

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.Surface((self.width, self.height), depth=16)
        self.font = pygame.font.Font(None, 50)
        self.text = "STAY"

    def DrawText(self, str, x, y):
        # 指定した文字列を作成
        text = self.font.render(str, True, self.TEXT_COLOR)
        # 描画する文字列の幅と高さを取得
        text_width = text.get_width()
        text_height = text.get_height()
        # 指定された座標を文字列の中心として描画
        self.surface.blit(text, (x - text_width // 2, y - text_height // 2))

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

    def draw_Title(self):
        # BACK_COLORでsurfaceを塗りつぶす
        self.surface.fill(self.BACK_COLOR)
        # 画面の中心にTitleの文字列を描画
        self.DrawText("Tirle", self.width//2, self.height//2)

    def draw_Opening(self):
        # BACK_COLORでsurfaceを塗りつぶす
        self.surface.fill(self.BACK_COLOR)
        # 画面の中心にOpeningの文字列を描画
        self.DrawText("Opening", self.width//2, self.height//2)

    def draw_Stage(self):
        # BACK_COLORでsurfaceを塗りつぶす
        self.surface.fill(self.BACK_COLOR)
        # 画面の中心にstageの文字列を描画
        self.DrawText("Stage", self.width//2, self.height//2)

    def draw_Over(self):
        # BACK_COLORでsurfaceを塗りつぶす
        self.surface.fill(self.BACK_COLOR)
        # 画面の中心にGame Overの文字列を描画
        self.DrawText("Game Over", self.width//2, self.height//2)

    def draw_Clear(self):
        # BACK_COLORでsurfaceを塗りつぶす
        self.surface.fill(self.BACK_COLOR)
        # 画面の中心にGame Game Clearの文字列を描画
        self.DrawText("Game Clear", self.width//2, self.height//2)