import pygame

class Renderer:
    """
    Surfaceへの描画処理を担当するクラス
    """

    def __init__(self, width, height):
        # 描画用Surfaceを生成する
        self.surface = pygame.Surface((width, height))

        # 文字描画用フォントを生成する
        self.font = pygame.font.Font(None, 50)

    def render(self):
        """
        Surfaceにテスト用の内容を描画する
        """

        # Surfaceを白色で塗りつぶす
        self.surface.fill((255, 255, 255))

        # 赤い四角形を描画する
        pygame.draw.rect(
            self.surface,
            (255, 0, 0),
            (100, 100, 200, 150)
        )

        # 文字列を作成する
        text = self.font.render(
            "pygame test",
            True,
            (0, 0, 0)
        )

        # 文字列をSurfaceへ描画する
        self.surface.blit(text, (150, 300))

        return self.surface