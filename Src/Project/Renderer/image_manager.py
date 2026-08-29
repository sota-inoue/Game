import pygame
from pathlib import Path

from System.file_load_system import load_image

from Domain.asset_paths import (
    ENEMY_IMAGE_PATH,
    OBSTACLE_IMAGE_PATH,
)


class ImageManager:
    def __init__(self):
        # 読み込んだ画像をパス名をキーとして保存する
        self._images: dict[str, pygame.Surface] = {}

        # 使用する画像を読み込む
        self.load(ENEMY_IMAGE_PATH)
        self.load(OBSTACLE_IMAGE_PATH)

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