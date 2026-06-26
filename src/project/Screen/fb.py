import mmap

class FrameBuffer:
    def __init__(self, device, width, height):
        self.device = device
        self.width = width
        self.height = height
        self.size = width * height * 2

        self.file = open(self.device, "r+b")
        self.map = mmap.mmap(self.file.fileno(), self.size)

    def draw(self, surface):
         # Surface が 16bit RGB565 である前提
        raw = surface.get_view("2")

        self.map.seek(0)
        self.map.write(raw)

    def close(self):
        self.map.close()
        self.file.close()