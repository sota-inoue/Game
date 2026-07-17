import pygame
from domein.config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    TOUCH_SCREEN_TOP_X,
    TOUCH_SCREEN_TOP_Y,
    BACK_COLOR
)

class PyGameDisplay:
    def __init__(self):
        # pygameウィンドウを生成
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw_clear(self):
        # pygameウィンドウを黒で塗りつぶす
        self.screen.fill(BACK_COLOR)
        pygame.display.flip()

    def game_draw(self, surface):
        # pygameウィンドウにゲーム画面描画する
        self.screen.blit(surface, (0, 0))
        pygame.display.flip()

    def touch_draw(self, surface):
        # pygameウィンドウにタッチパネル描画する
        self.screen.blit(surface, (TOUCH_SCREEN_TOP_X, TOUCH_SCREEN_TOP_Y))
        pygame.display.flip()