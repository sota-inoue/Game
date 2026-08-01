import pygame

from Application.game_controller import Controller


class App:
    def __init__(self, mode):
        self.controller = Controller(mode)
        self.clock = pygame.time.Clock()
        self.run()

    def run(self):
        while self.controller.loop():
            # 指定したフレームレートになるように処理速度を調整する
            self.clock.tick(10)

        self.controller.close()

