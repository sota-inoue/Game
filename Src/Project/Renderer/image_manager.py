import pygame
from pathlib import Path

from System.file_load_system import load_image

from Domain.asset_paths import (
    ENEMY_IMAGE_PATH,
    OBSTACLE_IMAGE_PATH,
    PLAYER_IMAGE_PATH,
    URGENCY_FRAME1, URGENCY_FRAME2, URGENCY_FRAME3, URGENCY_FRAME4, URGENCY_FRAME5, 
    URGENCY_FRAME6, URGENCY_FRAME7, URGENCY_FRAME8, URGENCY_FRAME9, URGENCY_FRAME10, 
    URGENCY_FRAME11, URGENCY_FRAME12, URGENCY_FRAME13, URGENCY_FRAME14, URGENCY_FRAME15, 
    URGENCY_FRAME16, URGENCY_FRAME17, URGENCY_FRAME18, URGENCY_FRAME19, URGENCY_FRAME20, 
    STAGE1_BACK_GRAUND, OHUDA_IMAGE, OJISAN_DAMAGED_IMAGE,
    TITLE_SELECT_PLAY,TITLE_SELECT_SETTING,TITLE_SELECT_EXIT,
    GAMECLEAR_SELECT_NEXT,GAMECLEAR_SELECT_TITLE,
    GAMEOVER_SELECT_CONTINUE,GAMEOVER_SELECT_TITLE,
    OPNING_PAGE_1, OPNING_PAGE_2, OPNING_PAGE_3,
    TOUCH_SCREEN
    )


class ImageManager:
    def __init__(self):
        # 読み込んだ画像をパス名をキーとして保存する
        self._images: dict[str, pygame.Surface] = {}

        # 使用する画像を読み込む
        self._load(ENEMY_IMAGE_PATH)
        self._load(OBSTACLE_IMAGE_PATH)
        self._load(PLAYER_IMAGE_PATH)
        self._load(URGENCY_FRAME1)
        self._load(URGENCY_FRAME2)
        self._load(URGENCY_FRAME3)
        self._load(URGENCY_FRAME4)
        self._load(URGENCY_FRAME5)
        self._load(URGENCY_FRAME6)
        self._load(URGENCY_FRAME7)
        self._load(URGENCY_FRAME8)
        self._load(URGENCY_FRAME9)
        self._load(URGENCY_FRAME10)
        self._load(URGENCY_FRAME11)
        self._load(URGENCY_FRAME12)
        self._load(URGENCY_FRAME13)
        self._load(URGENCY_FRAME14)
        self._load(URGENCY_FRAME15)
        self._load(URGENCY_FRAME16)
        self._load(URGENCY_FRAME17)
        self._load(URGENCY_FRAME18)
        self._load(URGENCY_FRAME19)
        self._load(URGENCY_FRAME20)
        self._load(STAGE1_BACK_GRAUND)
        self._load(OHUDA_IMAGE)
        self._load(OJISAN_DAMAGED_IMAGE)
        self._load(TITLE_SELECT_PLAY)
        self._load(TITLE_SELECT_SETTING)
        self._load(TITLE_SELECT_EXIT)
        self._load(GAMECLEAR_SELECT_NEXT)
        self._load(GAMECLEAR_SELECT_TITLE)
        self._load(GAMEOVER_SELECT_CONTINUE)
        self._load(GAMEOVER_SELECT_TITLE)
        self._load(OPNING_PAGE_1)
        self._load(OPNING_PAGE_2)
        self._load(OPNING_PAGE_3)
        self._load(TOUCH_SCREEN)

    def _load(self, path: Path | None) -> None:

        if path is None:
            image = pygame.Surface((10, 10))
            image.fill((0, 0, 0))
            self._images[path] = image
            return

        # 画像を読み込んで保存する
        self._images[path] = load_image(path)

    def get_image(self, path: Path | None) -> pygame.Surface:

        # パスに対応する画像を返す
        return self._images[path]