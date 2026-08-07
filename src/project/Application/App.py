import pygame
import time

from Application.game_controller import Controller


class App:
    def __init__(self, mode):
        self.controller = Controller(mode)
        self.clock = pygame.time.Clock()
        self.pre_time = time.perf_counter()

        self.run()

    def run(self):
        while True:
            start_time = time.perf_counter()

            if not self.controller.loop():
                self.controller.close()
                break

            # controller.loop()だけの処理時間
            processing_time = time.perf_counter() - start_time

            # 前回のフレーム開始から今回のフレーム開始まで
            frame_time = start_time - self.pre_time

            if frame_time > 0:
                fps = 1 / frame_time
            else:
                fps = 0

            # デバッグログ
            print(f"処理時間 = {processing_time:.4f}s : 1フレーム時間 = {frame_time:.4f}s : FPS = {fps:.2f}")

            self.pre_time = start_time

            # 指定したフレームレートになるように処理速度を調整する
            self.clock.tick(10)

        

