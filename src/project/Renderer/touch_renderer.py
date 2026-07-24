import pygame


class TouchDisplay:

    # 文字の色
    TEXT_COLOR = (255, 255, 255)

    # 線の色
    LINE_COLOR = (255, 255, 255)

    # 線の太さ
    LINE_WIDTH = 3

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 50)

    def DrawText(self, surface, text_string, x, y):
        # 指定した文字列を作成
        text = self.font.render(
            text_string,
            True,
            self.TEXT_COLOR
        )

        # 描画する文字列の幅と高さを取得
        text_width = text.get_width()
        text_height = text.get_height()

        # 指定された座標を文字列の中心として描画
        surface.blit(
            text,
            (
                x - text_width // 2,
                y - text_height // 2
            )
        )

    def draw_Controller(self, surface):
        # 文字を描画
        self.DrawText(
            surface,
            "L",
            self.width // 6,
            self.height // 2
        )

        self.DrawText(
            surface,
            "J",
            self.width * 3 // 6,
            self.height // 2
        )

        self.DrawText(
            surface,
            "R",
            self.width * 5 // 6,
            self.height // 2
        )

        # 区切り線を描画
        pygame.draw.line(
            surface,
            self.LINE_COLOR,
            (self.width // 3, 0),
            (self.width // 3, self.height),
            self.LINE_WIDTH
        )

        pygame.draw.line(
            surface,
            self.LINE_COLOR,
            (self.width * 2 // 3, 0),
            (self.width * 2 // 3, self.height),
            self.LINE_WIDTH
        )