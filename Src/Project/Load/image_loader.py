# src/project/Load/image_loader.py
"""
【呼び出しイメージ】
描画クラス（Renderer等）からこのクラスを受け取り、以下のように使用します。

例: src/project/Renderer/stage/player_renderer.py
--------------------------------------------------
class PlayerRenderer:
    def __init__(self, image_loader):
        self.image_loader = image_loader

    def draw(self, surface, player_x, player_y):
        # ImageManager からプレイヤー画像を取得（初回のみ自動ロード、2回目以降はキャッシュから即座に取得）
        player_image = self.image_loader.get_image("player/player.png", size=(64, 64))
        
        # 画面に描画
        surface.blit(player_image, (player_x, player_y))
--------------------------------------------------
"""

import os
from typing import Dict, Optional, Tuple
import pygame


class ImageManager:
    """
    Assets/Image/ 内の画像アセットの読み込み・キャッシュ・管理を行うクラス
    """

    def __init__(self, base_dir: Optional[str] = None):
        # 読み込んだ画像を保持するキャッシュ: { "相対パス": pygame.Surface }
        self._images: Dict[str, pygame.Surface] = {}

        # 画像が格納されているルートディレクトリ（Assets/Image/）のパスを設定
        if base_dir is None:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # Load/ から見て 2つ上の src/project/Assets/Image を指す
            self._base_dir = os.path.normpath(
                os.path.join(current_dir, "..", "Assets", "Image")
            )
        else:
            self._base_dir = base_dir

    def get_image(
        self, 
        relative_path: str, 
        size: Optional[Tuple[int, int]] = None
    ) -> pygame.Surface:
        """
        指定されたパスの画像を取得する。未読み込みの場合はディスクから読み込んでキャッシュする。

        :param relative_path: Assets/Image からの相対パス (例: "player/player.png")
        :param size: リサイズしたい場合の (幅, 高さ) タプル (省略時は元サイズ)
        :return: pygame.Surface オブジェクト
        """
        # WindowsとMac/Linuxのパス区切り文字の違いを吸収
        formatted_path = relative_path.replace("\\", "/")
        
        # サイズ指定がある場合は別キーで管理
        cache_key = f"{formatted_path}_{size}" if size else formatted_path

        # 1. すでにキャッシュにある場合はそれを即座に返す
        if cache_key in self._images:
            return self._images[cache_key]

        # 2. 元画像が未ロードならロードする
        if formatted_path not in self._images:
            self._load_and_cache(formatted_path)

        base_surface = self._images[formatted_path]

        # 3. リサイズ指定がある場合は拡縮処理を行ってキャッシュに登録
        if size is not None:
            scaled_surface = pygame.transform.scale(base_surface, size)
            self._images[cache_key] = scaled_surface
            return scaled_surface

        return base_surface

    def _load_and_cache(self, relative_path: str) -> None:
        """
        画像ファイルをディスクから読み込み、Pygameの高速描画形式に変換してキャッシュする
        """
        full_path = os.path.join(self._base_dir, relative_path)

        # ファイルが存在しない場合のエラーハンドリング
        if not os.path.exists(full_path):
            print(f"[Warning] 画像ファイルが見つかりません: {full_path}")
            self._images[relative_path] = self._create_dummy_surface()
            return

        try:
            surface = pygame.image.load(full_path)
            
            # Pygameの画面転送を高速化するためのフォーマット変換
            if surface.get_alpha() is not None or relative_path.endswith(".png"):
                surface = surface.convert_alpha()
            else:
                surface = surface.convert()

            self._images[relative_path] = surface

        except Exception as e:
            print(f"[Error] 画像の読み込みに失敗しました ({full_path}): {e}")
            self._images[relative_path] = self._create_dummy_surface()

    def preload_directory(self, sub_dir: str = "") -> None:
        """
        指定したフォルダ内の画像を事前にすべて一括読み込みする（ゲームロード時など）
        
        :param sub_dir: Assets/Image 以下のフォルダ名 (例: "player")
        """
        target_dir = os.path.join(self._base_dir, sub_dir)
        if not os.path.exists(target_dir):
            return

        for root, _, files in os.walk(target_dir):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, self._base_dir)
                    rel_path = rel_path.replace("\\", "/")
                    if rel_path not in self._images:
                        self._load_and_cache(rel_path)

    def _create_dummy_surface(self, width: int = 32, height: int = 32) -> pygame.Surface:
        """
        読み込み失敗時に目立つピンク色の四角形（ダミー画像）を生成する
        """
        surface = pygame.Surface((width, height))
        surface.fill((255, 0, 255))  # マゼンタ（ピンク）
        return surface

    def clear_cache(self) -> None:
        """保持しているキャッシュをクリアする"""
        self._images.clear()