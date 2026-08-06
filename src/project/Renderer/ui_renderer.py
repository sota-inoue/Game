import pygame
from Domain.config import GRAY, WHITE 

class UIRenderer:

    def __init__(self, width, height):
        self.width = width
        self.height = height

        # 日本語を表示する場合は、日本語対応フォントを指定する
        self.font = pygame.font.Font(None, 50)

        self.health_width = width//10 * 3
        self.health_height = height//10 * 2
        self.health_x = width - self.health_width
        self.health_y = 0


    def DrawText(self, surface, str, x, y):
        # 指定した文字列を作成
        text = self.font.render(str, True, GRAY)
        # 描画する文字列の幅と高さを取得
        text_width = text.get_width()
        text_height = text.get_height()
        # 指定された座標を文字列の中心として描画
        surface.blit(text, (x - text_width // 2, y - text_height // 2))



    def health_draw(self, surface, hp):
        pygame.draw.rect(surface, WHITE, (self.health_x, self.health_y, self.health_width, self.health_height))
        self.DrawText(surface, f"おなか: {hp}%",
            self.health_x + self.health_width // 2, 
            self.health_y + self.health_height // 2)