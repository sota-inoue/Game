import pygame

class StageObject:
    def __init__(self, color):
        self.color = color

    def draw(self, x, y, width, height, surface):
        # x, yを中心座標として、オブジェクトを画面上に描画する
        pygame.draw.rect(
            surface,
            self.color,
            (
                # xを中心にして、左上のx座標を決める
                x - (width // 2),

                # yを中心にして、左上のy座標を決める
                y - (height // 2),

                # オブジェクトの横幅
                width,

                # オブジェクトの縦幅
                height
            )
        )

class Enemy(StageObject):
    def __init__(self):
        super().__init__((255, 0, 0))   # 赤色


class Obstacle(StageObject):
    def __init__(self):
        super().__init__((128, 128, 128))   # 灰色

class Player(StageObject):
    def __init__(self):
        super().__init__((0, 255, 0))   # 緑色