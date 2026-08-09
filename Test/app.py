import pygame

from game_controller import GameController


class App:
    """
    pygameの初期化、イベント処理、ゲームループ、
    終了処理を担当するクラス
    """

    def __init__(self):
        # pygameを初期化する
        pygame.init()

        # ウィンドウサイズ
        self.width = 600
        self.height = 450

        # ゲームを実行中かどうかを管理する
        self.is_running = True

        # 1フレーム分の処理を管理するControllerを生成する
        self.controller = GameController(
            self.width,
            self.height
        )

        # フレームレートを管理するClockを生成する
        self.clock = pygame.time.Clock()

        # 1秒間に実行するフレーム数
        self.fps = 10

    def run(self):
        """
        ゲームループを実行する
        """

        while self.is_running:
            # pygameのイベントを取得する
            for event in pygame.event.get():

                # ウィンドウの×ボタンが押された場合
                if event.type == pygame.QUIT:
                    self.is_running = False

            # 終了要求がない場合だけ処理する
            if self.is_running:
                # Controllerに1フレーム分の処理を指示する
                self.controller.update()

                # 指定したフレームレートに調整する
                self.clock.tick(self.fps)

        # pygameを終了する
        pygame.quit()