import os
import pygame 
from System.file_load_system import load_image


class OPRenderer:
    """OP演出（挿絵画像等）の描画処理を行うクラス"""

    def __init__(self, display_width: int, display_height: int):
        self.width = display_width
        self.height = display_height
        self.op_images = {}

        base_dir = os.path.join("Assets", "Image", "OP")
        for i in range(1, 4):
            path = os.path.join(base_dir, f"op_{i}.png")
            image = load_image(path)
            if image is not None and isinstance(image, pygame.Surface):
                self.op_images[i] = pygame.transform.scale(image, (self.width, self.height))
            else:
                self.op_images[i] = None

    def draw(self, surface: pygame.Surface, op_page: int):
        """指定されたページのOP挿絵画像を画面全体に描画する"""
        image = self.op_images.get(op_page)
        if image is not None:
            surface.blit(image, (0, 0))
        else:
            # 画像のロード失敗・存在しない場合の代替描画
            surface.fill((0, 0, 0))
            font = pygame.font.Font(None, 36)
            text = font.render(f"OP Page {op_page}", True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
            surface.blit(text, text_rect)
            