import pygame
import time
from enum import Enum

from Screen.Touch import TouchDisplay, TouchScene
from Screen.Display import GameDisplay, GameScene
from System.fb import FbManager
from System.input import TouchInput
from Game.player import Command
from System.Textreader import TextReader

class GameState(Enum):
    TITLE = 0
    OP = 1
    STAGE = 2
    OVER = 3
    CLEAR = 4

class App:
    # 背景色（黒）
    BACK_COLOR = (0, 0, 0)
    # FPS（1秒あたりの更新回数）
    FPS = 10
    # Windous用のゲーム画面サイズ
    DISPLAY_WIDTH = 600
    DISPLAY_HEIGHT = 450
    # pygameのウィンドウサイズ
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 800

    def __init__(self, mode):
        # True : Raspberry Pi（フレームバッファ描画）
        # False: PC（pygameウィンドウ描画）
        self.mode = mode
        # pygameを初期化
        pygame.init()

        # fpsを管理するためのClockオブジェクトを生成
        self.clock = pygame.time.Clock()

        self.map = TextReader()
        self.start = 0

        # タッチ画面を生成
        self.touch = TouchDisplay()
        # Raspberry Piモードで使用するインスタンスを生成
        if self.mode:
            # pygameウィンドウは使用しない
            self.screen = None
            # フレームバッファへ直接描画するFbManagerクラスのインスタンスを生成
            self.fb = FbManager()
            # Raspberry Pi用ゲーム画面の生成
            # fbの宣言時に動的にゲーム画面のサイズが決まるため、fbの宣言後にゲーム画面のサイズを決める
            self.game = GameDisplay(self.fb.HDMI_WIDTH, self.fb.HDMI_HEIGHT)
            # タッチ入力を取得するTouchInputクラスのインスタンスを生成
            self.input_device = TouchInput()
        # Windowsモードで使用するインスタンスを生成
        else:
            # Windows用ゲーム画面の生成
            self.game = GameDisplay(self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT)
            # pygameウィンドウを生成
            self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
            # Windowsでは使用しない
            self.fb = None
            self.input_device = None

        # タッチパネルの表示位置の頂点座標
        self.TOUCH_SCREEN_TOP_X = (self.SCREEN_WIDTH - self.touch.WIDTH) // 2
        self.TOUCH_SCREEN_TOP_Y = self.SCREEN_HEIGHT - self.touch.HEIGHT - 15

        # フレームカウンタ
        self.count = 0

        # ゲームの状態
        self.state = GameState.TITLE

        # タッチ入力情報
        self.is_touching = False
        self.input_x = 0
        self.input_y = 0

        # メインループを継続するためのフラグ
        self.running = True

        # メインループ開始
        self.run()
       
    def run(self):
        """
        メインループ
        入力取得 → ゲーム更新 → 描画
        を繰り返す
        """
        while self.running:
            prestart = self.start
            self.start = time.perf_counter()

            # 前フレームから今回のフレーム開始までの経過時間
            loop_time = self.start - prestart

            # 入力取得
            self.get_event()

            # ゲーム更新
            self.update()

            # 描画処理
            self.draw()

            # フレーム数を更新
            self.count += 1

            end = time.perf_counter()

            # 今フレームの処理時間
            processing_time = end - self.start

            print(f"ループ間隔: {loop_time:.6f} 秒 : 処理時間: {processing_time:.6f} 秒")

            # FPS調整
            self.clock.tick(self.FPS)

        # 終了処理
        self.close()

    def update(self):
        """
        ゲームの進行を管理する
        """
        # タイトル画面でタッチされた場合
        if self.state == GameState.TITLE and self.is_touching == True:
            # 左半分が押されたらオープニング画面へ遷移
            if self.input_x < self.touch.WIDTH //2 :
                self.state = GameState.OP
                self.game.set_state(GameScene.OP)
                self.touch.set_state(TouchScene.CONTROLLER)
                self.count = 0

            # 右半分が押されたらゲームを終了
            elif self.input_x > self.touch.WIDTH //2 :
                self.running = False

        # オープニング画面を2秒表示したらゲーム画面へ遷移
        elif self.state == GameState.OP and self.count > 20:
            self.state = GameState.STAGE
            self.game.set_state(GameScene.STAGE)
            self.touch.set_state(TouchScene.CONTROLLER)
            self.count = 0

        # ゲーム画面を表示している間の処理
        elif self.state == GameState.STAGE:
            # 入力されたコマンドを取得し、ゲーム画面に渡す
            cmd = self.get_command()
            self.game.set_player_cmd(cmd)
            if self.count % 5 == 0:
                self.game.mapupdate(self.map.get_mapdata1(self.count // 5))

            # ゲーム画面を一定時間表示したらクリア画面へ遷移する
            if self.count > 100:
                self.state = GameState.CLEAR
                self.game.set_state(GameScene.CLEAR)
                self.touch.set_state(TouchScene.CONTINUE)
                self.count = 0

        # クリア画面でタッチされたらタイトル画面へ戻る
        elif self.state == GameState.CLEAR and self.is_touching == True:
            self.state = GameState.TITLE
            self.game.set_state(GameScene.TITLE)
            self.touch.set_state(TouchScene.START)
            self.count = 0
        

    def get_event(self):
        """
        タッチ入力を取得する
        ラズパイでは入力デバイス、
        PCではpygameイベントから取得する
        """
        # 入力情報を初期化
        self.is_touching = False
        self.input_x = 0
        self.input_y = 0

        # Raspberry Piモードでのタッチ座標の取得
        if self.mode:
            # タッチデバイスの現在の入力座上を更新
            self.input_device.update()

             # タッチ状態取得
            self.is_touching = self.input_device.touch_down
            self.input_x = self.input_device.x
            self.input_y = self.input_device.y

        # Windowsモードでのタッチ座標の取得
        else:
            # pygameイベント取得
            events = pygame.event.get()
            for event in events:
                 # ウィンドウを閉じた場合の処理
                if event.type == pygame.QUIT:
                    self.close()
                    exit()
                # マウスクリックの場合の処理(仕様でマウスクリックをタッチ入力として拾ってくれ、Windows上でのデバックも楽なため)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                     # タッチパネル内をクリックしたかどうかを判定
                    if (self.TOUCH_SCREEN_TOP_X <= x <= self.TOUCH_SCREEN_TOP_X + self.touch.WIDTH
                        and self.TOUCH_SCREEN_TOP_Y <= y <= self.TOUCH_SCREEN_TOP_Y + self.touch.HEIGHT):

                        # タッチ状態取得し、タッチパネル内座標へ変換
                        self.is_touching = True
                        self.input_x = x - self.TOUCH_SCREEN_TOP_X
                        self.input_y = y - self.TOUCH_SCREEN_TOP_Y


    def get_command(self):
        """
        入力座標からコマンドを決定する
        """
        # タッチされていない場合
        if not self.is_touching:
            return Command.STAY
        
        if 0 <= self.input_x < self.touch.WIDTH // 3:
            return Command.LEFT
        elif self.touch.WIDTH // 3 <= self.input_x < self.touch.WIDTH * 2 // 3:
            return Command.JUMP
        elif self.touch.WIDTH * 2 // 3 <= self.input_x <= self.touch.WIDTH:
            return Command.RIGHT
        return Command.STAY
    

    def draw(self):
        """
        ゲーム画面とタッチパネルを出力先に描画する
        """
        # タッチパネル描画
        self.touch.draw()
        # ゲーム画面描画
        self.game.draw()
        # Raspberry Piモードでの描画処理
        if self.mode:
            # HDMIへゲーム画面を描画
            self.fb.hdmi_draw(self.game.surface)
            # SPI液晶へタッチ画面を描画
            self.fb.spi_draw(self.touch.surface)
        # Windowsモードでの描画処理
        else:
            # 背景を塗りつぶす
            self.screen.fill(self.BACK_COLOR)
            # ゲーム画面描画
            self.screen.blit(self.game.surface, (0, 0))
            # タッチパネル描画
            self.screen.blit(self.touch.surface,(self.TOUCH_SCREEN_TOP_X, self.TOUCH_SCREEN_TOP_Y))
            # 画面更新
            pygame.display.flip()

    def close(self):
        """
        終了処理
        """
        # ラズパイではフレームバッファを閉じる
        if self.mode:
            self.fb.close()

        # pygame終了
        pygame.quit()
