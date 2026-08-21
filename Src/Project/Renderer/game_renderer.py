import pygame

from Domain.config import GRAY
from Domain.state import TitleState

class GameDisplay:
    TEXT_COLOR = (0, 0, 0)

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 50)

    def DrawText(self, surface, str, x, y):
        # 指定した文字列を作成
        text = self.font.render(str, True, self.TEXT_COLOR)
        # 描画する文字列の幅と高さを取得
        text_width = text.get_width()
        text_height = text.get_height()
        # 指定された座標を文字列の中心として描画
        surface.blit(text, (x - text_width // 2, y - text_height // 2))

    def draw_Title(self, surface, title_state):
        surface.fill(GRAY)
        # タイトル
        self.DrawText(surface, "Title", self.width // 2, self.height // 3)

        # メニューのX座標とY座標
        start_x = self.width // 4
        setting_x = self.width // 2
        exit_x = self.width * 3 // 4
        menu_y = self.height * 2 // 3
        arrow_y = menu_y - 50

        # メニューを表示
        self.DrawText(surface, "START", start_x, menu_y)
        self.DrawText(surface, "SETTING", setting_x, menu_y)
        self.DrawText(surface, "EXIT", exit_x, menu_y)

        # 選択状態から矢印のX座標を決定
        if title_state == TitleState.START:
            arrow_x = start_x
        elif title_state == TitleState.SETTING:
            arrow_x = setting_x
        elif title_state == TitleState.EXIT:
            arrow_x = exit_x

        # 矢印を表示
        self.DrawText(surface, "▼", arrow_x, arrow_y)
    
    def draw_Opening(self, surface):
        surface.fill(GRAY)
        self.DrawText(surface,"Opening", self.width//2, self.height//2)
    
    def draw_Over(self, surface):
        surface.fill(GRAY)
        self.DrawText(surface,"Game Over", self.width//2, self.height//2)
    
    def draw_Clear(self, surface):
        surface.fill(GRAY)
        self.DrawText(surface,"Game Clear", self.width//2, self.height//2)