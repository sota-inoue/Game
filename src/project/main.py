import pygame

from Screen.Touch import TouchDisplay
from Screen.fb import FrameBuffer

class App:
    FB = "/dev/fb1"

    def __init__(self):
        pygame.init()
        self.touch = TouchDisplay()
        self.fb = FrameBuffer(self.FB, self.touch.WIDTH, self.touch.HEIGHT)
        self.run()

    def run(self):
        try:
            self.touch.draw()
            self.fb.draw(self.touch.surface)

        finally:
            self.fb.close()
            pygame.quit()


App()
