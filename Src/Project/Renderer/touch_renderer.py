import pygame

from Domain.config import GRAY

class TouchDisplay:

    # 文字の色
    TEXT_COLOR = (255, 255, 255)

    # 線の色
    LINE_COLOR = (255, 255, 255)

    # 線の太さ
    LINE_WIDTH = 3

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 50)

    def DrawText(self, surface, text_string, x, y):
        # 指定した文字列を作成
        text = self.font.render( text_string, True, self.TEXT_COLOR )
        # 描画する文字列の幅と高さを取得
        text_width = text.get_width()
        text_height = text.get_height()
        # 指定された座標を文字列の中心として描画
        surface.blit(text, ( x - text_width // 2,  y - text_height // 2 ) )

    def draw_Controller(self, surface):
        surface.fill(GRAY)
        # 文字を描画
        self.DrawText(surface, "L", self.width // 6, self.height * 3 // 4)
        self.DrawText(surface, "J", self.width * 3 // 6, self.height * 3 // 4)
        self.DrawText(surface, "R", self.width * 5 // 6, self.height * 3 // 4)

        self.DrawText(surface, "A", self.width // 4, self.height // 4)
        self.DrawText(surface, "P", self.width * 3 // 4, self.height // 4)

        # 区切り線を描画
        half_height = self.height // 2

        # 上半分：2等分
        pygame.draw.line(
            surface, self.LINE_COLOR,
            (self.width // 2, 0), 
            (self.width // 2, half_height),
            self.LINE_WIDTH
        )

        # 下半分：3等分
        pygame.draw.line(
            surface,
            self.LINE_COLOR,
            (self.width // 3, half_height),
            (self.width // 3, self.height),
            self.LINE_WIDTH
        )

        pygame.draw.line(
            surface,
            self.LINE_COLOR,
            (self.width * 2 // 3, half_height),
            (self.width * 2 // 3, self.height),
            self.LINE_WIDTH
        )

        # 上下の境界線
        pygame.draw.line(
            surface,
            self.LINE_COLOR,
            (0, half_height),
            (self.width, half_height),
            self.LINE_WIDTH
        )