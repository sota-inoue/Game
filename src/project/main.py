import pygame
import time

from Screen.Touch import TouchDisplay
from Screen.fb import FrameBuffer
from Screen.input import TouchInput

class App:
    FB = "/dev/fb1"
    FPS = 10

    def __init__(self):
        pygame.init()
        self.touch = TouchDisplay()
        self.fb = FrameBuffer(self.FB, self.touch.WIDTH, self.touch.HEIGHT)
        self.input = TouchInput()
        self.count = 0
        self.run()

    def run(self):
        self.draw()
        while self.count < 30:
            self.input.update()
            print(self.count, self.input.x, self.input.y, self.input.touch_down)
            self.count += 1
            time.sleep(1 / self.FPS)
        self.fb.close()
        pygame.quit()

    def draw(self):
        try:
            self.touch.draw()
            self.fb.draw(self.touch.surface)

        finally:
            self.fb.close()
            pygame.quit()


App()
