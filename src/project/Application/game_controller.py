import pygame

# 入力処理を管理するクラス
from Input.input_manager import Input

# ゲーム内の状態を管理するクラス
from Domein.state import State

# 描画処理を管理するクラス
from Renderer.renderer_manager import Renderer

# ゲームの進行や内部処理を管理するクラス
from System.system_manager import SystemManager

# 画面への出力処理を管理するクラス
from Display.display_manager import Display


class Controller:
    """
    入力取得、ゲーム状態の更新、描画、画面出力を順番に実行し、
    ゲーム全体の処理を制御するクラス
    """

    def __init__(self, mode):
        """
        Controllerで使用する各クラスのインスタンスを生成する。

        mode:
            True  : Raspberry Pi（フレームバッファ描画）
            False : PC（pygameウィンドウ描画）
        """

        # 実行環境を表す値を保存する
        # True : Raspberry Pi（フレームバッファ描画）
        # False: PC（pygameウィンドウ描画）
        self.mode = mode

        # pygameを初期化する
        pygame.init()

        # ゲーム内で変化するデータを管理するStateを生成する
        self.state = State()

        # ゲーム画面やタッチ画面の出力を管理するDisplayを生成する
        self.display = Display(mode)

        # PCまたはRaspberry Piからの入力を取得するInputを生成する
        self.input = Input(mode)

        # ゲーム画面とタッチ画面の描画を管理するRendererを生成する
        # Displayが保持している各画面の幅と高さを渡す
        self.renderer = Renderer(
            self.display.GAME_SCREEN_WIDTH,
            self.display.GAME_SCREEN_HEIGHT,
            self.display.TOUCH_SCREEN_WIDTH,
            self.display.TOUCH_SCREEN_HEIGHT
        )

        # ゲームの進行やマップ更新などを管理するSystemManagerを生成する
        # ゲーム画面の高さと幅を渡す
        self.system = SystemManager(
            self.display.GAME_SCREEN_HEIGHT,
            self.display.GAME_SCREEN_WIDTH
        )

    def get_event(self):
        """
        入力座標を取得し、Stateに保存する。
        """

        # Inputから入力された横座標と縦座標を取得する
        x, y = self.input.get_input()

        # 取得した横座標をStateに保存する
        self.state.set_input_x(x)

        # 取得した縦座標をStateに保存する
        self.state.set_input_y(y)

    def system_update(self):
        """
        入力情報や経過時間を使用して、ゲーム内部の状態を更新する。
        """

        # ゲームの進行を管理する

        # 現在のゲーム進行状態をStateから取得する
        game_state = self.state.get_game_state()

        # 現在の進行状態、入力座標、経過時間を使用して、
        # 次のゲーム進行状態を取得する
        new_state = self.system.progress_update(
            game_state,
            self.state.get_input_x(),
            self.state.get_input_y(),
            self.state.get_count(),
        )

        # 更新後のゲーム進行状態をStateに保存する
        self.state.set_game_state(new_state)

        # ゲーム進行状態が切り替わった場合、
        # その状態での経過時間を0に戻す
        if new_state != game_state:
            self.state.set_count(0)

        # 現在のゲーム進行状態がステージ画面の場合、
        # プレイヤーの位置を更新する
        if self.state.get_game_state() == self.state.STAGE:

            # 入力された横座標と縦座標を使用して、
            # 更新後のプレイヤー座標を取得する
            player_x, player_y = self.state.player_update(
                self.state.get_input_x(),
                self.state.get_input_y()
            )

            # 更新後のプレイヤーの横座標をStateに保存する
            self.state.set_player_x(player_x)

            # 更新後のプレイヤーの縦座標をStateに保存する
            self.state.set_player_y(player_y)

        # マップの状態を更新する

        # ステージ画面であり、経過時間が5の倍数の場合に
        # マップの配置情報を更新する
        if self.state.get_game_state() == self.state.STAGE and self.state.get_count() % 5 == 0:

            # 現在のマップ情報を使用して、
            # 更新後のマップ情報を取得する
            updated_map_data = self.system.map_update(
                self.state.get_map_data(),
                [0,0,0,0,0]
            )

            # 更新後のマップ情報をStateに保存する
            self.state.set_map_data(updated_map_data)

    def draw(self):
        """
        現在のゲーム状態に応じて、
        ゲーム画面とタッチパネルを描画する。
        """

        # タッチパネルの内容を描画する
        self.renderer.touch_render()

        # ゲーム画面を描画する

        # タイトル状態の場合はタイトル画面を描画する
        if self.state.get_game_state() == self.state.TITLE:
            self.renderer.draw_Title()

        # オープニング状態の場合はオープニング画面を描画する
        elif self.state.get_game_state() == self.state.OP:
            self.renderer.draw_Opening()

        # ステージ状態の場合はマップとプレイヤーを描画する
        elif self.state.get_game_state() == self.state.STAGE:

            # 現在のマップ情報を使用してステージを描画する
            self.renderer.stage_render(self.state.get_map_data())

            # 現在のプレイヤー座標を使用してプレイヤーを描画する
            self.renderer.player_render(
                self.state.get_player_x(),
                self.state.get_player_y()
            )

        # ゲームオーバー状態の場合はゲームオーバー画面を描画する
        elif self.state.get_game_state() == self.state.OVER:
            self.renderer.draw_Over()

    def output(self):
        """
        Rendererで描画したゲーム画面とタッチパネルを、
        Displayを通して実際の出力先に表示する。
        """

        # ゲーム画面用Surfaceとタッチ画面用Surfaceを出力する
        self.display.update(
            self.renderer.game_surface,
            self.renderer.touch_surface
        )

    def roop(self):
        """
        ゲームの1回分の処理を順番に実行する。
        """

        # 入力を取得してStateに保存する
        self.get_event()

        # 入力情報を基にゲーム内部の状態を更新する
        self.system_update()

        # 更新されたゲーム状態を基に画面を描画する
        self.draw()

        # 描画した画面を実際の出力先に表示する
        self.output()

    def close(self):
        """
        ゲーム終了時の処理を行う。
        """

        # Raspberry Piではフレームバッファを閉じる
        # 現在はコメントアウトされている
        # if self.mode:
        #     self.fb.close()

        # pygameの機能を終了する
        pygame.quit()