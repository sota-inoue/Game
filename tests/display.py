import pygame

class Display:
    """
    pygameの画面生成と画面更新を担当するクラス
    """

    def __init__(self, width, height):
        # pygameを初期化する
        pygame.init()

        # pygameウィンドウを生成する
        self.screen = pygame.display.set_mode((width, height))

        # ウィンドウタイトルを設定する
        pygame.display.set_caption("Display Test")

    def clear(self, color):
        """
        画面全体を指定した色で塗りつぶす
        """
        self.screen.fill(color)

    def draw(self, surface, x, y):
        """
        Surfaceを指定した位置に描画する
        """
        self.screen.blit(surface, (x, y))

    def update(self):
        """
        描画した内容を画面へ反映する
        """
        pygame.display.flip()