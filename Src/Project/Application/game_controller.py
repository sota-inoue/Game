import pygame

from Input.command_converter import Command

# 入力処理を管理するクラス
from Input.input_manager import Input

# ゲーム内の状態を管理するクラス
from Application.state import State
from Domain.game_flag import GamePhase

# ゲームの進行や内部処理を管理するクラス
from System.system_manager import System

# 画面への出力処理を管理するクラス
from Display.display_manager import DisplayManager



class Controller:
    def __init__(self,mode):
        self.mode = mode
        pygame.init()
        
        self._display = DisplayManager(mode)

        self.input = Input(mode)
        self.system = System()
        self.state = State()

        #self.system.play_TitleBGM()
        self.loop_flug = True
        self.count = 0
        self._is_middle_draw = False

    def command_update(self):
        # 入力状態を更新する
        self.input.command_update()

        # 5カウントごとに入力結果をゲーム内部へ反映する
        if self.count % 4 == 0:

            # ボタンが押された場合は効果音を再生する
            if self.input.get_is_click():
                self.system.play_PushButton()

            # 現在の入力コマンドを取得して保存する
            command = self.input.get_command()
            self.state.set_game_command(command)

    def progress_update(self):
        # 現在のゲーム進行状態と操作情報を取得する
        game_state = self.state.get_game_phase()
        game_flag = self.state.get_game_flag()
        command = self.state.get_game_command()

        # 現在のゲーム状態に応じた進行処理を行う
        if game_state == GamePhase.TITLE:
            self.loop_flug = self.system.title_update(command, game_flag)
        elif game_state == GamePhase.OPENING:
            self.system.opening_update(command, game_flag)
        elif game_state == GamePhase.STAGE:
            self.system.stage_update(game_flag)
        elif game_state == GamePhase.GAMEOVER:
            self.system.gameover_update(command, game_flag)
        elif game_state == GamePhase.CLEAR:
            self.system.gameclear_update(command, game_flag)

        # 進行処理後のゲーム状態を取得する
        new_game_state = self.state.get_game_phase()

        # ゲーム状態が変化した場合のみ遷移後の初期化を行う
        if game_state != new_game_state:
            self.count = 0
            # ステージへ遷移した場合
            if new_game_state == GamePhase.STAGE:
                self.state.set_game_command(Command.NONE)
                self.state.stage_reset()
                player = self.state.get_player_data()
            # タイトル画面へ遷移した場合
            elif new_game_state == GamePhase.TITLE:
                self.state.title_reset()
 
    def stage_update(self):
        # ステージ処理に必要な内部データを取得する
        command = self.state.get_game_command()
        player = self.state.get_player_data()
        objects = self.state.get_objects_data()
        stage = self.state.get_stage_number()

        # 敵オブジェクトとお札の当たり判定の処理を行う
        # if self.count % 5 == 3:
        #     self.system.object_hit_check(objects)

        # 4カウントごとにゲーム内部の主要な更新処理を行う
        if self.count == 0 or self.count % 4 == 0:
            # マップを更新し、ステージクリア条件を判定する
            is_gameclear = self.system.map_update(self.count, objects, stage)
            self.state.set_is_gameclear(is_gameclear)

            # マップ更新直後は通常レーンを描画する
            self._is_middle_draw = False

            # 入力コマンドに応じてプレイヤーの当たり判定位置を更新する
            self.system.player_move_state_update(command, player)


            # プレイヤーとステージオブジェクトの当たり判定を行う
            self.system.player_hit_check(self.count, player, objects)

            # 現在の切迫度からゲームオーバー条件を判定する
            hp = self.state.get_urgency_level()
            is_gameover = hp >= 100
            self.state.set_is_gameover(is_gameover)

            # 攻撃入力があった場合は攻撃データを生成する
            # if command == Command.ATTACK:
            #     attack = self.system.player_attack(player, objects)
            #     self.state.set_attack_data(attack)

        # プレイヤーの描画座標を毎カウント更新する
        self.system.player_move(player)
        self.system.player_position_update(player)


    def system_update(self):
        # 5カウントごとにゲーム全体の進行状態を更新する
        if self.count % 4 == 0:
            self.progress_update()

        # 進行状態更新後に現在のゲーム状態を取得する
        game_state = self.state.get_game_phase()

        # ステージ中の場合のみステージ内部処理を実行する
        if game_state == GamePhase.STAGE:
            self.stage_update()

        # ゲーム全体で使用するカウントを更新する
        self.count += 1

    def draw(self):
        # 現在のゲーム進行状態を取得する
        game_state = self.state.get_game_phase()

        # タイトル画面を描画する
        if game_state == GamePhase.TITLE:
            title = self.state.get_title_scene_selection()
            self._display.draw_title(title)

        # オープニング画面を描画する
        elif game_state == GamePhase.OPENING:
            opening= self.state.get_opening_page()
            self._display.draw_opening(opening)

        # ゲームステージを描画する
        elif game_state == GamePhase.STAGE:
            # ステージの背景を描画する
            self._display.draw_stage()

            # ステージ内の描画に必要なデータを取得する
            map_data = self.state.get_objects_data()
            player_data = self.state.get_player_data()
            # attack_data = self.state.get_attack_draw_data()


            if self.count % 4 == 2:
                self._is_middle_draw = True

            if not self._is_middle_draw:
                self._display.draw_stage_object(player_data, map_data)
            else:
                self._display.draw_stage_middle_object(player_data, map_data)


            # 切迫度などのUIを描画する
            urgency_level = self.state.get_urgency_level()
            self._display.draw_urgency_level(urgency_level)

        # ゲームクリア画面を描画する
        elif game_state == GamePhase.CLEAR:
            clear = self.state.get_gameclear_scene_selection()
            self._display.draw_game_clear(clear)

        # ゲームオーバー画面を描画する
        elif game_state == GamePhase.GAMEOVER:
            over = self.state.get_gameover_scene_selection()
            self._display.draw_game_over(over)

        # エンディング画面を描画する
        elif game_state == GamePhase.ENDING:
            self._display.draw_ending()

        # self.renderer.touch_render()
        self._display.touch_iamge_render()

    def loop(self):
        self.command_update()
        self.system_update()
        self.draw()
        self._display.output()
        if self.state.get_game_phase()== GamePhase.ENDING:
            if self.count > 30:
                return False
        return self.loop_flug

    
    def close(self):
        if self.mode:
            self._display.fb_close()
        pygame.quit()