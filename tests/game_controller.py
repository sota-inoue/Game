from display import Display
from renderer import Renderer


class GameController:
    """
    RendererとDisplayに指示を出し、
    1フレーム分の描画処理を管理するクラス
    """

    def __init__(self, width, height):
        # 画面出力を担当するDisplayを生成する
        self.display = Display(width, height)

        # 描画処理を担当するRendererを生成する
        self.renderer = Renderer(width, height)

    def update(self):
        """
        1フレーム分の処理を実行する
        """

        # Rendererへ描画を指示する
        surface = self.renderer.render()

        # pygameウィンドウを黒色で消去する
        self.display.clear((0, 0, 0))

        # 描画済みSurfaceをウィンドウへ配置する
        self.display.draw(surface, 0, 0)

        # 描画内容を画面へ反映する
        self.display.update()