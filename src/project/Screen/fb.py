import mmap
import pygame


class FrameBuffer:
    def __init__(self, device, width, height):
        self.device = device
        self.width = width
        self.height = height
        self.size = width * height * 2

        self.file = open(self.device, "r+b")
        self.map = mmap.mmap(self.file.fileno(), self.size)

    def draw(self, surface):
        raw = pygame.image.tostring(surface, "RGB565")

        self.map.seek(0)
        self.map.write(raw)

    def close(self):
        self.map.close()
        self.file.close()