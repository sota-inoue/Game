import pygame
import mmap
import subprocess

class FbManager:
    SPI_WIDTH = 480
    SPI_HEIGHT = 320
    HDMI_WIDTH = 1920
    HDMI_HEIGHT = 1080
     
    def __init__(self):
        # SPI_FBとHDMI_FBの具体的なデバイス名を調べる
        self.SPI_FB = self.find_fb(self.SPI_WIDTH, self.SPI_HEIGHT)
        if self.SPI_FB is None:
            raise RuntimeError("SPI LCD用のフレームバッファが見つかりません")
        
        self.HDMI_FB = self.find_fb(self.HDMI_WIDTH, self.HDMI_HEIGHT)
        if self.HDMI_FB is None:
            raise RuntimeError("HDMI用のフレームバッファが見つかりません")
        #フレームバッファーに直接描写するクラスを呼びだす。
        self.fb1 = FrameBuffer(self.SPI_FB, self.SPI_WIDTH , self.SPI_HEIGHT)
        self.fb2 = FrameBuffer(self.HDMI_FB, self.HDMI_WIDTH, self.HDMI_HEIGHT)

    # SPI液晶のフレームバッファーに直接描写する処理
    def spi_draw(self, surface):
        self.fb1.draw(surface)

    # HDMIのフレームバッファーに直接描写する処理
    def hdmi_draw(self, surface):
        self.fb2.draw(surface)

    def close(self):
        self.fb1.close()
        self.fb2.close()

    def find_fb(self, width, height):
        # /dev/fb0～/dev/fb2 を順番に調べる
        # 出力画面はSPI液晶とHDMI1と2があるため3つ調べる
        for fb in ["/dev/fb0", "/dev/fb1", "/dev/fb2"]:
            try:
                # PythonからLinuxコマンドを実行し、その結果をresultに入れる
                result = subprocess.check_output(
                    # Linuxコマンド「fbset -fb <デバイス名>」を実行する
                    ["fbset", "-fb", fb],
                    # 戻り値を文字列にする
                    text=True
                )
                # 実行結果の例
                # mode "480x320"
                #     geometry 480 320 480 320 16
                #     rgba 5/11,6/5,5/0,0/0
                # endmode

                # 実行結果を1行ずつ取り出して調べる
                for line in result.splitlines():
                    # 解像度が書かれているgeometry行を探す
                    if "geometry" in line:
                        # geometry行を空白で分割する
                        # ['geometry', '480', '320', '480', '320', '16']
                        data = line.split()
                        fb_width = int(data[1])
                        fb_height = int(data[2])

                        print(f"{fb}: {fb_width}x{fb_height}")

                        if width == fb_width and height == fb_height:
                            return fb

            # フレームバッファが存在しないなどのエラーは無視して次を調べる
            except Exception:
                pass


class FrameBuffer:
    def __init__(self, device, width, height):
        # 真っ黒な画面を作成
        self.surface = pygame.Surface((width, height), depth=16)
        self.surface.fill((0, 0, 0))
        # RGB565(16bit = 2Byte)のため必要なバイト数を計算
        self.size = width * height * 2
        # フレームバッファを読み書き可能モードで開く
        self.file = open(device, "r+b")
        # フレームバッファをメモリへマッピングする
        self.map = mmap.mmap(self.file.fileno(), self.size)

    def draw(self, surface):
        # Surfaceの画像データをRGB565形式で取得する
        raw = surface.get_view("2")
        # フレームバッファの先頭へ移動する
        self.map.seek(0)
        # Surfaceの画像データをフレームバッファへ書き込み、画面へ描画する
        self.map.write(raw)

    def close(self):
        # 画面を黒で塗りつぶす
        self.draw(self.surface)
        # メモリマップを閉じる
        self.map.close()
        # フレームバッファファイルを閉じる
        self.file.close()