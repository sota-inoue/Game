import mmap
import pygame


class FrameBuffer:

    def __init__(self, width, height, device):
        self.width = width
        self.height = height

        self.fb = open(device, "r+b")

        self.map = mmap.mmap(
            self.fb.fileno(),
            width * height * 2
        )

    def draw(self, surface):
        self.map.seek(0)

        self.map.write(
            pygame.image.tostring(
                surface,
                "RGB565"
            )
        )

    def close(self):
        self.map.close()
        self.fb.close()