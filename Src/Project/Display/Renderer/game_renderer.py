import pygame

from Display.Renderer.image_manager import ImageManager

from asset_paths import (
    STAGE1_BACK_GRAUND,
    TITLE_SELECT_PLAY, TITLE_SELECT_SETTING, TITLE_SELECT_EXIT,
    GAMECLEAR_SELECT_NEXT, GAMECLEAR_SELECT_TITLE,
    GAMEOVER_SELECT_CONTINUE, GAMEOVER_SELECT_TITLE,
    OPNING_PAGE_1, OPNING_PAGE_2, OPNING_PAGE_3
)
from config import GRAY
from Domain.game_flag import TitleSceneSelection, OpeningPage, GameOverSceneSelection, GameClearSceneSelection


class GameDisplay:
    TEXT_COLOR = (0, 0, 0)

    def __init__(self, surface: pygame.Surface, image: ImageManager):
        self._surface = surface
        self._image = image

        self._title_images: dict[TitleSceneSelection, pygame.Surface] = {
            TitleSceneSelection.START: self._image.get_image(TITLE_SELECT_PLAY),
            TitleSceneSelection.SETTING: self._image.get_image(TITLE_SELECT_SETTING),
            TitleSceneSelection.EXIT: self._image.get_image(TITLE_SELECT_EXIT),
        }

        self._gameclear_images: dict[GameClearSceneSelection, pygame.Surface] = {
            GameClearSceneSelection.NEXT: self._image.get_image(GAMECLEAR_SELECT_NEXT),
            GameClearSceneSelection.TITLE: self._image.get_image(GAMECLEAR_SELECT_TITLE),
        }

        self._gameover_images: dict[GameOverSceneSelection, pygame.Surface] = {
            GameOverSceneSelection.CONTINUE: self._image.get_image(GAMEOVER_SELECT_CONTINUE),
            GameOverSceneSelection.TITLE: self._image.get_image(GAMEOVER_SELECT_TITLE),
        }

        self._opning_images: dict[OpeningPage, pygame.Surface] ={
            OpeningPage.PAGE_1: self._image.get_image(OPNING_PAGE_1),
            OpeningPage.PAGE_2: self._image.get_image(OPNING_PAGE_2),
            OpeningPage.PAGE_3: self._image.get_image(OPNING_PAGE_3),
        }

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

    def draw_title(self, state: TitleSceneSelection) -> None:
        # 現在の選択状態に対応するタイトル画像を取得する
        image = self._title_images[state]

        # 画面サイズに合わせて画像をリサイズする
        image = pygame.transform.scale(image, (self._width, self._height))

        # タイトル画面を描画する
        self._surface.blit(image, (0, 0))


    def draw_clear(self, state: GameClearSceneSelection) -> None:
        # 現在の選択状態に対応するゲームクリア画像を取得する
        image = self._gameclear_images[state]

        # 画面サイズに合わせて画像をリサイズする
        image = pygame.transform.scale(image, (self._width, self._height))

        # ゲームクリア画面を描画する
        self._surface.blit(image, (0, 0))


    def draw_over(self, state: GameOverSceneSelection) -> None:
        # 現在の選択状態に対応するゲームオーバー画像を取得する
        image = self._gameover_images[state]

        # 画面サイズに合わせて画像をリサイズする
        image = pygame.transform.scale(image, (self._width, self._height))
        
        # ゲームオーバー画面を描画する
        self._surface.blit(image, (0, 0))

    def draw_opning(self, state: OpeningPage) -> None:
        # 現在の状態に対応するオープニング画像を取得する
        image = self._opning_images[state]

        # 画面サイズに合わせて画像をリサイズする
        image = pygame.transform.scale(image, (self._width, self._height))
        
        # ゲームオーバー画面を描画する
        self._surface.blit(image, (0, 0))

    def draw_ending(self) -> None:
        self._surface.fill(GRAY)
        self.draw_text( "ENDING", self._width // 2, self._height // 2 )

    def draw_stage1_bg(self) -> None:
        # 背景画像を取得する
        image = self._image.get_image(STAGE1_BACK_GRAUND)

        # 画面サイズに変更する
        image = pygame.transform.scale( image, (self._width, self._height) )

        # 背景画像を描画する
        self._surface.blit( image,(0, 0) )
