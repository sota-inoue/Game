import pygame

from Application.game_controller import Controller


class App:
    """
    Controllerを使用してゲーム全体を実行するクラス
    """

    def __init__(self, mode):
        """
        ゲームの実行に必要なControllerとClockを生成する。

        mode:
            True  : Raspberry Piで実行する
            False : PCで実行する

        fps:
            1秒間に実行するフレーム数
        """

        # ゲームを実行中かどうかを管理するフラグ
        self.is_running = True

        # ゲーム全体の処理を管理するControllerを生成する
        self.controller = Controller(mode)

        # ゲームのフレームレートを管理するClockを生成する
        self.clock = pygame.time.Clock()

        # ゲームのフレームレートを保存する
        self.fps = 10

    def run(self):
        """
        ゲームループを実行する。
        """
        # is_runningがTrueの間、ゲームを実行する
        while self.is_running:
            
            # Controllerの1回分の処理を実行する
            self.controller.roop()

            # 指定したフレームレートになるように処理速度を調整する
            self.clock.tick(self.fps)
