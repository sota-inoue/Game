import pygame
from Domain.config import (
    PLAYER_IMAGE_PATH,
    ENEMY_IMAGE_PATH,
    OBSTACLE_IMAGE_PATH
)

class StageObject:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path).convert_alpha()

    def draw(self, x, y, width, height, surface):
        image = pygame.transform.scale(
            self.image,
            (width, height)
        )

        # 画像を画面上に描画する
        surface.blit(
            image,
            (
                x - (width // 2),
                y - (height // 2)
            )
        )

class Enemy(StageObject):
    def __init__(self):
        super().__init__(ENEMY_IMAGE_PATH)

class Obstacle(StageObject):
    def __init__(self):
        super().__init__(OBSTACLE_IMAGE_PATH)

class Player(StageObject):
    def __init__(self):
        super().__init__(PLAYER_IMAGE_PATH)
