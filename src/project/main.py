import pygame

from Screen.Touch import TouchDisplay
from Screen.fb import FrameBuffer


FB = "/dev/fb1"
W = 480
H = 320


def main():
    pygame.init()

    fb = FrameBuffer(FB, W, H)
    screen = TouchDisplay(W, H)

    try:
        screen.draw()
        fb.draw(screen.surface)

    finally:
        fb.close()
        pygame.quit()


main()
