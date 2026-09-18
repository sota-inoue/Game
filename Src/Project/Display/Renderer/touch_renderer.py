import pygame

from Display.Renderer.image_manager import ImageManager

from asset_paths import TOUCH_SCREEN
from config import GRAY


class TouchDisplay:

    # 文字の色
    TEXT_COLOR = (255, 255, 255)

    # 線の色
    LINE_COLOR = (255, 255, 255)

    # 線の太さ
    LINE_WIDTH = 3

    def __init__(self, surface: pygame.Surface, image: ImageManager) -> None:
        self._surface = surface
        self._image = image
        self._touch_image = self._image.get_image(TOUCH_SCREEN)
        self._width = self._surface.get_width()
        self._height = self._surface.get_height()
        self._font = pygame.font.Font(None, 50)

    def draw_text(self, text_string: str, x: int, y: int) -> None:
        # 指定した文字列を作成する
        text = self._font.render(text_string, True, self.TEXT_COLOR)
        # 描画する文字列の幅と高さを取得する
        text_width = text.get_width()
        text_height = text.get_height()
        # 指定された座標を文字列の中心として描画する
        self._surface.blit(text, ( x - text_width // 2, y - text_height // 2))

    def draw_controller(self) -> None:
        # 背景を塗りつぶす
        self._surface.fill(GRAY)

        # 下段の操作文字を描画する
        self.draw_text( "L", self._width // 6, self._height * 3 // 4)
        self.draw_text( "J", self._width * 3 // 6, self._height * 3 // 4)

        # 上段の操作文字を描画する
        self.draw_text( "R", self._width * 5 // 6, self._height * 3 // 4)
        self.draw_text( "A", self._width // 4, self._height // 4)
        self.draw_text( "P", self._width * 3 // 4, self._height // 4)

        # 画面の中央Y座標
        half_height = self._height // 2

        # 上半分を2等分する線
        pygame.draw.line(self._surface, self.LINE_COLOR, (self._width // 2, 0), (self._width // 2, half_height), self.LINE_WIDTH )

        # 下半分を3等分する線
        pygame.draw.line(self._surface, self.LINE_COLOR, (self._width // 3, half_height), (self._width // 3, self._height), self.LINE_WIDTH)
        pygame.draw.line(self._surface, self.LINE_COLOR, (self._width * 2 // 3, half_height), (self._width * 2 // 3, self._height), self.LINE_WIDTH)

        # 上半分と下半分の境界線
        pygame.draw.line(self._surface, self.LINE_COLOR, (0, half_height), (self._width, half_height), self.LINE_WIDTH)

    def draw_controller_image(self) -> None:
        
        # 画面サイズに合わせて画像をリサイズする
        image = pygame.transform.scale(self._touch_image, (self._width, self._height))

        # コントローラ画面を描画する
        self._surface.blit(image, (0, 0))