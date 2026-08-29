import pygame
from Renderer.image_manager import ImageManager
from Domain.asset_paths import (
    URGENCY_FRAME1, URGENCY_FRAME2, URGENCY_FRAME3, URGENCY_FRAME4, URGENCY_FRAME5, 
    URGENCY_FRAME6, URGENCY_FRAME7, URGENCY_FRAME8, URGENCY_FRAME9, URGENCY_FRAME10, 
    URGENCY_FRAME11, URGENCY_FRAME12, URGENCY_FRAME13, URGENCY_FRAME14, URGENCY_FRAME15, 
    URGENCY_FRAME16, URGENCY_FRAME17, URGENCY_FRAME18, URGENCY_FRAME19, URGENCY_FRAME20, 
)

class UIRenderer:

    def __init__(self, surface: pygame.Surface, image : ImageManager):
        self._surface = surface
        self._image = image

        self.width = surface.get_width()
        self.height = surface.get_height()

        # 日本語を表示する場合は、日本語対応フォントを指定する
        self.font = pygame.font.Font(None, 50)

        self.URGENCY_FRAMES = [
            URGENCY_FRAME1, URGENCY_FRAME2, URGENCY_FRAME3, URGENCY_FRAME4, URGENCY_FRAME5, 
            URGENCY_FRAME6, URGENCY_FRAME7, URGENCY_FRAME8, URGENCY_FRAME9, URGENCY_FRAME10, 
            URGENCY_FRAME11, URGENCY_FRAME12, URGENCY_FRAME13, URGENCY_FRAME14, URGENCY_FRAME15, 
            URGENCY_FRAME16, URGENCY_FRAME17, URGENCY_FRAME18, URGENCY_FRAME19, URGENCY_FRAME20, 
        ]

        self.health_width = self.width // 20 * 5
        self.health_height = self.height // 20 * 3
        self.health_x = self.width - self.health_width
        self.health_y = 0



    def health_draw(self, urgency_level: int) -> None:

        # 5刻みでフレーム番号を求める
        if urgency_level == 0:
            index = 0
        else:
            index = (urgency_level - 1) // 5

        path = self.URGENCY_FRAMES[index]

        # 画像を取得する
        img = self._image.get_image(path)

        # 描画サイズに変更する
        image = pygame.transform.scale( img, (self.health_width, self.health_height))

        # 画像を描画する
        self._surface.blit( image,(self.health_x, self.health_y)
    )
