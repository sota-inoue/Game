import pygame

class StageObject:
    def __init__(self, image):
        self.image = image

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
    def __init__(self, image):
        super().__init__(image)

class Obstacle(StageObject):
    def __init__(self, image):
        super().__init__(image)

class Player(StageObject):
    def __init__(self, image):
        super().__init__(image)
