import pygame
import time

from Screen.Touch import TouchDisplay
from Screen.Display import GameDisplay, Command
from System.fb import FrameBuffer
from System.input import TouchInput

class App:
    FB1 = "/dev/fb0"  # ゲーム画面
    FB2 = "/dev/fb1"  # タッチ画面
    BACK_COLOR = (0, 0, 0)
    FPS = 10
    WIDTH = 600
    HEIGHT = 850

    def __init__(self, mode):
        self.mode = mode  # Trueならラズパイfb描画
        pygame.init()
        self.touch = TouchDisplay()
        self.game = GameDisplay()

        if self.mode:
            self.screen = None
            self.fb1 = FrameBuffer(self.FB1, self.game.WIDTH, self.game.HEIGHT)
            self.fb2 = FrameBuffer(self.FB2, self.touch.WIDTH, self.touch.HEIGHT)
            self.input_device = TouchInput()
        else:
            self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
            self.fb1 = None
            self.fb2 = None
            self.input_device = None
            
        self.TOUCH_SCREEN_TOP_X = (self.WIDTH - self.touch.WIDTH) // 2
        self.TOUCH_SCREEN_TOP_Y = self.HEIGHT - self.touch.HEIGHT - 20

        self.count = 0

        self.is_touching = False
        self.input_x = 0
        self.input_y = 0
        self.run()
       
    def run(self):
        while self.count < 50:
            self.get_event()
            command = self.get_command()
            self.game.update(command)
            self.draw()
            self.count += 1
            time.sleep(1 / self.FPS)
        self.close()

    def get_command(self):
        if not self.is_touching:
            return Command.STAY
        if 0 <= self.input_x < self.touch.WIDTH // 3:
            return Command.LEFT
        elif self.touch.WIDTH // 3 <= self.input_x < self.touch.WIDTH * 2 // 3:
            return Command.JUMP
        elif self.touch.WIDTH * 2 // 3 <= self.input_x <= self.touch.WIDTH:
            return Command.RIGHT
        return Command.STAY

    def get_event(self):
        self.is_touching = False
        self.input_x = 0
        self.input_y = 0

        if self.mode:
            self.input_device.update()
            self.is_touching = self.input_device.touch_down
            self.input_x = self.input_device.x
            self.input_y = self.input_device.y
        else:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.close()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if (self.TOUCH_SCREEN_TOP_X <= x <= self.TOUCH_SCREEN_TOP_X + self.touch.WIDTH
                        and self.TOUCH_SCREEN_TOP_Y <= y <= self.TOUCH_SCREEN_TOP_Y + self.touch.HEIGHT):
                        self.is_touching = True
                        self.input_x = x - self.TOUCH_SCREEN_TOP_X
                        self.input_y = y - self.TOUCH_SCREEN_TOP_Y

    def draw(self):
        self.touch.draw_Controller()
        self.game.draw_Game()

        if self.mode:
            self.fb1.draw(self.game.surface)
            self.fb2.draw(self.touch.surface)

        else:
            self.screen.fill(self.BACK_COLOR)
            self.screen.blit(self.game.surface, (0, 0))
            self.screen.blit(self.touch.surface,(self.TOUCH_SCREEN_TOP_X, self.TOUCH_SCREEN_TOP_Y))
            pygame.display.flip()

    def close(self):
        if self.mode == True:
            self.touch.draw()
            self.game.draw()
            self.fb1.draw(self.touch.surface)
            self.fb2.draw(self.touch.surface)
            self.fb1.close()
            self.fb2.close()
            pygame.quit()
        else:
            pygame.quit()
