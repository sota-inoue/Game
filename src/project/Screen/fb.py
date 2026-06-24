import mmap

class FrameBuffer:

    def __init__(self, device, width, height):
        self.width = width
        self.height = height

        self.fb = open(device, "r+b")

        self.map = mmap.mmap(
            self.fb.fileno(),
            width * height * 2
        )

    def draw(self, surface):

        self.map.seek(0)
        self.map.write(surface.get_buffer())

    def close(self):
        self.map.close()
        self.fb.close()