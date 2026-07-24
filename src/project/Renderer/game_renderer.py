import pygame

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

    def draw_Title(self, surface):
        # 画面の中心にTitleの文字列を描画
        self.DrawText(surface,"Title", self.width//2, self.height//2)
    
    def draw_Opening(self, surface):
        # 画面の中心にOpeningの文字列を描画
        self.DrawText(surface,"Opening", self.width//2, self.height//2)
    
    def draw_Over(self, surface):
        # 画面の中心にGame Overの文字列を描画
        self.DrawText(surface,"Game Over", self.width//2, self.height//2)
    
    def draw_Clear(self, surface):
        # 画面の中心にGame Game Clearの文字列を描画
        self.DrawText(surface,"Game Clear", self.width//2, self.height//2)