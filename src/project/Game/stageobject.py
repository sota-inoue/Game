import pygame

class StageObject:
    def __init__(self, color):
        self.color = color

    def draw(self, x, y, width, height, surface):
        # オブジェクトを描画する
        pygame.draw.rect(surface, self.color, (x, y, width, height))

class Enemy(StageObject):
    def __init__(self):
        super().__init__((255, 0, 0))   # 赤色


class Obstacle(StageObject):
    def __init__(self):
        super().__init__((128, 128, 128))   # 灰色