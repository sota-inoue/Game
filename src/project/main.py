import pygame

from Screen.Touch import TouchDisplay
from Screen.fb import FrameBuffer


class App:
    DEVICE1 = "/dev/fb1"
    FPS = 10

    def __init__(self):
        pygame.init()

        self.touch = TouchDisplay()

        self.fb1 = FrameBuffer(
            self.touch.WIDTH,
            self.touch.HEIGHT,
            self.DEVICE1
        )

        self.clock = pygame.time.Clock()

    def run(self):
        try:
            while self.get_event():
                self.touch.Draw()

                self.fb1.draw(
                    self.touch.surface
                )

                self.clock.tick(self.FPS)

        finally:
            self.fb1.close()
            pygame.quit()

    def get_event(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                return False

            self.touch.GetEvent(event)

        return True


App()
