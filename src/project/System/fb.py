import mmap
import subprocess

class FbManager:
    spi_fb = None  # 解像度が低い方
    hdmi_fb = None  # 解像度が高い方

    def __init__(self):
        self.spi_fb, self.hdmi_fb = self.find_framebuffers()
        self.fb1 = FrameBuffer(self.spi_fb, 480, 320)
        self.fb2 = FrameBuffer(self.hdmi_fb, 1920, 1080)

    def spi_draw(self, surface):
        self.fb1.draw(surface)

    def hdmi_draw(self, surface):
        self.fb2.draw(surface)

    def close(self):
        self.fb1.close()
        self.fb2.close()

    def find_framebuffers(self):
        framebuffers = []

        for fb in ["/dev/fb0", "/dev/fb1", "/dev/fb2"]:
            try:
                result = subprocess.check_output(
                    ["fbset", "-fb", fb],
                    text=True
                )

                for line in result.splitlines():
                    if "geometry" in line:
                        data = line.split()
                        width = int(data[1])
                        height = int(data[2])

                        framebuffers.append(
                            (width * height, fb)
                        )
                        break

            except Exception:
                pass

        if len(framebuffers) < 2:
            raise RuntimeError("必要なフレームバッファが見つかりません")

        framebuffers.sort(key=lambda x: x[0])

        low_fb = framebuffers[0][1]
        high_fb = framebuffers[-1][1]

        print("Low Resolution :", low_fb)
        print("High Resolution:", high_fb)

        return low_fb, high_fb

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