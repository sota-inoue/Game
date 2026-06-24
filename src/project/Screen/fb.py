import mmap
import pygame


class FrameBuffer:
    def __init__(self, device, width, height):
        self.device = device
        self.width = width
        self.height = height

        self.file = open(self.device, "r+b")
        self.map = mmap.mmap(
            self.file.fileno(),
            self.width * self.height * 2
        )

    def draw(self, surface):
        raw = pygame.image.tostring(surface, "RGB")

        data = bytearray()

        for i in range(0, len(raw), 3):
            r = raw[i]
            g = raw[i + 1]
            b = raw[i + 2]

            rgb565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)

            data += rgb565.to_bytes(2, "little")

        self.map.seek(0)
        self.map.write(data)

    def close(self):
        self.map.close()
        self.file.close()