import mmap
import pygame

FB = "/dev/fb2"
W, H = 480, 320

pygame.init()

screen = pygame.Surface((W, H))
screen.fill((0, 0, 0))

pygame.draw.rect(screen, (255, 0, 0), (50, 50, 150, 100))
pygame.draw.circle(screen, (0, 255, 0), (300, 160), 50)

raw = pygame.image.tostring(screen, "RGB")

with open(FB, "r+b") as f:
    fb = mmap.mmap(f.fileno(), W * H * 2)

    # RGB888 → RGB565
    data = bytearray()
    for i in range(0, len(raw), 3):
        r, g, b = raw[i], raw[i+1], raw[i+2]
        rgb565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
        data += rgb565.to_bytes(2, "little")

    fb.seek(0)
    fb.write(data)
    fb.close()
