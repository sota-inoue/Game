import pygame

from Domein.config import (
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
        # pygameウィンドウを背景色で塗りつぶす
        self.screen.fill(BACK_COLOR)

    def game_draw(self, surface):
        # pygameウィンドウにゲーム画面を描画する
        self.screen.blit(surface, (0, 0))

    def touch_draw(self, surface):
        # pygameウィンドウにタッチパネルを描画する
        self.screen.blit(surface, (TOUCH_SCREEN_TOP_X, TOUCH_SCREEN_TOP_Y))