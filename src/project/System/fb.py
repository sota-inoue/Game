import pygame
import mmap
import subprocess

class FbManager:
    
     
    def __init__(self):
        # SPI液晶の画面サイズとフレームバッファ名のインスタン生成と初期化
        self.SPI_FB = None
        self.SPI_WIDTH = 0
        self.SPI_HEIGHT = 0

        # HDMIの画面サイズとフレームバッファ名のインスタン生成と初期化
        self.HDMI_FB = None
        self.HDMI_WIDTH = 0
        self.HDMI_HEIGHT = 0

        # 接続されているフレームバッファを調べ、デバイス名と画面サイズを取得する
        self.find_fb()

        # SPI液晶用のフレームバッファが見つからなければ終了
        if self.SPI_FB is None:
            raise RuntimeError("SPI LCD用のフレームバッファが見つかりません")

        # HDMI用のフレームバッファが見つからなければ終了
        if self.HDMI_FB is None:
            raise RuntimeError("HDMI用のフレームバッファが見つかりません")

        # SPI液晶用のフレームバッファを操作するクラスを生成
        self.fb1 = FrameBuffer(self.SPI_FB, self.SPI_WIDTH, self.SPI_HEIGHT)

        # HDMI用のフレームバッファを操作するクラスを生成
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

    def find_fb(self):
        # フレームバッファの情報を保存するリストの生成
        framebuffers = []
        # /dev/fb0～/dev/fb2 を順番に調べる
        # Raspberry PiではSPI液晶とHDMI出力があるため3つ確認する
        for fb in ["/dev/fb0", "/dev/fb1", "/dev/fb2"]:
            try:
                # Linuxコマンド「fbset -fb <デバイス名>」を実行し、フレームバッファの情報を取得する
                result = subprocess.check_output(
                    ["fbset", "-fb", fb],
                    # 実行結果を文字列として受け取る
                    text=True
                    # 存在しないフレームバッファを指定したときのエラーメッセージを表示しない
                    stderr=subprocess.DEVNULL
                )

                # 実行結果の例
                # mode "480x320"
                #     geometry 480 320 480 320 16
                #     rgba 5/11,6/5,5/0,0/0
                # endmode

                # 実行結果を1行ずつ調べる
                for line in result.splitlines():
                    # 解像度が書かれているgeometry行を探す
                    if "geometry" in line:
                        # 空白で分割する
                        # 例：['geometry', '480', '320', '480', '320', '16']
                        data = line.split()
                        # 横幅と高さを取得する
                        width = int(data[1])
                        height = int(data[2])
                        # フレームバッファ名、解像度（画面のサイズ）
                        framebuffers.append({
                            "fb": fb,
                            "width": width,
                            "height": height,
                            # 比較用に解像度を保存する
                            "size": width * height
                        })
                        break

            # フレームバッファが存在しない場合は次を調べる
            except Exception:
                pass

        # フレームバッファが2つ未満ならエラー
        if len(framebuffers) < 2:
            raise RuntimeError("必要なフレームバッファが見つかりません")
        
        # 解像度の小さい順に並べ替える
        framebuffers.sort(key=lambda x: x["size"])

        # 解像度が低い方をSPI液晶、大きい方をHDMIとして取得する
        spi = framebuffers[0]
        hdmi = framebuffers[-1]

        # SPI液晶の情報を保存
        self.SPI_FB = spi["fb"]
        self.SPI_WIDTH = spi["width"]
        self.SPI_HEIGHT = spi["height"]

        # HDMIの情報を保存
        self.HDMI_FB = hdmi["fb"]
        self.HDMI_WIDTH = hdmi["width"]
        self.HDMI_HEIGHT = hdmi["height"]
    
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