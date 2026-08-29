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
    STAGE1_BACK_GRAUND
)


class ImageManager:
    def __init__(self):
        # 読み込んだ画像をパス名をキーとして保存する
        self._images: dict[str, pygame.Surface] = {}

        # 使用する画像を読み込む
        self.load(ENEMY_IMAGE_PATH)
        self.load(OBSTACLE_IMAGE_PATH)
        self.load(PLAYER_IMAGE_PATH)

        self.load(URGENCY_FRAME1)
        self.load(URGENCY_FRAME2)
        self.load(URGENCY_FRAME3)
        self.load(URGENCY_FRAME4)
        self.load(URGENCY_FRAME5)
        self.load(URGENCY_FRAME6)
        self.load(URGENCY_FRAME7)
        self.load(URGENCY_FRAME8)
        self.load(URGENCY_FRAME9)
        self.load(URGENCY_FRAME10)
        self.load(URGENCY_FRAME11)
        self.load(URGENCY_FRAME12)
        self.load(URGENCY_FRAME13)
        self.load(URGENCY_FRAME14)
        self.load(URGENCY_FRAME15)
        self.load(URGENCY_FRAME16)
        self.load(URGENCY_FRAME17)
        self.load(URGENCY_FRAME18)
        self.load(URGENCY_FRAME19)
        self.load(URGENCY_FRAME20)
        self.load(STAGE1_BACK_GRAUND)


    def load(self, path: Path) -> None:
        # 引数の型を確認する
        if not isinstance(path, Path):
            raise TypeError(f"受け取った型 {type(path).__name__} : pathはPath型で指定してください")

        # 画像を読み込んで保存する
        self._images[path] = load_image(path)

    def get_image(self, path: Path) -> pygame.Surface:
        # 引数の型を確認する
        if not isinstance(path, Path):
            raise TypeError(f"受け取った型 {type(path).__name__} : pathはPath型で指定してください")

        # 指定されたパスの画像が存在するか確認する
        if path not in self._images:
            raise KeyError(f"画像が読み込まれていません: {path}")

        # パスに対応する画像を返す
        return self._images[path]