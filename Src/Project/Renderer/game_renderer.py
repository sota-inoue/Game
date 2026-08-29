import pygame

from Renderer.image_manager import ImageManager

from Domain.asset_paths import STAGE1_BACK_GRAUND
from Domain.config import GRAY
from Domain.state import TitleState


class GameDisplay:
    TEXT_COLOR = (0, 0, 0)

    def __init__(self, surface: pygame.Surface, image: ImageManager):
        self._surface = surface
        self._image = image

        self._width = surface.get_width()
        self._height = surface.get_height()

        self._font = pygame.font.Font(None, 50)

    def draw_text(self, text_data: str, x: int, y: int) -> None:
        # 指定した文字列を作成する
        text = self._font.render(text_data, True, self.TEXT_COLOR)
        # 描画する文字列の幅と高さを取得する
        text_width = text.get_width()
        text_height = text.get_height()
        # 指定された座標を文字列の中心として描画する
        self._surface.blit(text, (x - text_width // 2, y - text_height // 2))

    def draw_title(self, title_state: TitleState) -> None:
        # 背景を塗りつぶす
        self._surface.fill(GRAY)

        # タイトルを描画する
        self.draw_text( "Title", self._width // 2, self._height // 3 )

        # メニューの描画座標を計算する
        start_x = self._width // 4
        setting_x = self._width // 2
        exit_x = self._width * 3 // 4

        menu_y = self._height * 2 // 3
        arrow_y = menu_y - 50

        # メニューを描画する
        self.draw_text("START", start_x, menu_y)
        self.draw_text("SETTING", setting_x, menu_y)
        self.draw_text("EXIT", exit_x, menu_y)

        # 選択状態から矢印のX座標を決定する
        if title_state == TitleState.START:
            arrow_x = start_x

        elif title_state == TitleState.SETTING:
            arrow_x = setting_x

        elif title_state == TitleState.EXIT:
            arrow_x = exit_x

        else:
            return

        # 選択位置に矢印を描画する
        self.draw_text("▼", arrow_x, arrow_y)

    def draw_opening(self) -> None:
        self._surface.fill(GRAY)
        self.draw_text( "Opening", self._width // 2, self._height // 2 )

    def draw_over(self) -> None:
        self._surface.fill(GRAY)
        self.draw_text( "Game Over", self._width // 2, self._height // 2 )

    def draw_clear(self) -> None:
        self._surface.fill(GRAY)
        self.draw_text( "Game Clear", self._width // 2, self._height // 2 )

    def draw_stage1_bg(self) -> None:
        # 背景画像を取得する
        image = self._image.get_image(STAGE1_BACK_GRAUND)

        # 画面サイズに変更する
        image = pygame.transform.scale( image, (self._width, self._height) )

        # 背景画像を描画する
        self._surface.blit( image,(0, 0) )
