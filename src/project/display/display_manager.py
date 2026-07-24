import pygame
from Display.pygame_display import PyGameDisplay
from Display.fb import FbManager

from Domein.config import (
    DISPLAY_WIDTH,
    DISPLAY_HEIGHT,
    TOUCH_WIDTH,
    TOUCH_HEIGHT
)

class Display:
    def __init__(self, mode):
        # True : Raspberry Pi（フレームバッファ描画）
        # False: PC（pygameウィンドウ描画）
        self.mode = mode

        # Raspberry Piモードで使用するインスタンスを生成
        if self.mode:
            # フレームバッファへ直接描画するFbManagerクラスのインスタンスを生成
            self.fb = FbManager()
            self.GAME_SCREEN_HEIGHT = self.fb.HDMI_HEIGHT
            self.GAME_SCREEN_WIDTH = self.fb.HDMI_WIDTH
            self.TOUCH_SCREEN_HEIGHT = self.fb.SPI_HEIGHT
            self.TOUCH_SCREEN_WIDTH = self.fb.SPI_WIDTH
        else:
            # pygameウィンドウを生成
            self.pygame = PyGameDisplay()
            self.GAME_SCREEN_HEIGHT = DISPLAY_HEIGHT
            self.GAME_SCREEN_WIDTH = DISPLAY_WIDTH
            self.TOUCH_SCREEN_HEIGHT = TOUCH_HEIGHT
            self.TOUCH_SCREEN_WIDTH = TOUCH_WIDTH

    def update(self, game_surface, touch_surface):
        if self.mode:
            # Raspberry Piモードでは、フレームバッファに描画する
            self.fb.game_draw(game_surface)
            self.fb.touch_draw(touch_surface)
        else:
            # PCモードでは、pygameウィンドウに描画する
            self.pygame.game_draw(game_surface)
            self.pygame.touch_draw(touch_surface)
            pygame.display.flip()
        