import pygame

from Input.command_converter import Command

# 入力処理を管理するクラス
from Input.input_manager import Input

# ゲーム内の状態を管理するクラス
from State.state_manager import State
from State.game_flag import GamePhase


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

        self._last_count = 0


    def progress_update(self):

        # 現在のゲーム進行状態と操作情報を取得する
        game_phase = self.state.get_game_phase()
        game_flag = self.state.get_game_flag()
        command = self.state.get_game_command()

        # 現在のゲーム状態に応じた進行処理を行う
        self.loop_flug = self.system.progress_update(command, game_flag)

        # 進行処理後のゲーム状態を取得する
        new_game_phase = self.state.get_game_phase()

        # ポーズへ遷移した場合
        if game_phase != GamePhase.PAUSE and new_game_phase == GamePhase.PAUSE:
            self._last_count = self.count
            self.count = 0
            self._display.save_surface()
            return

        # ポーズから復帰した場合
        if game_phase == GamePhase.PAUSE and new_game_phase != GamePhase.PAUSE:
            self.count = self._last_count
            self.state.set_game_command(Command.NONE)
            return

        # 通常のゲーム状態が変化した場合
        if game_phase != new_game_phase:
            self.count = 0
            self._last_count = 0

            if new_game_phase == GamePhase.STAGE:
                self.state.set_game_command(Command.NONE)
                self.state.stage_reset()
            elif new_game_phase == GamePhase.TITLE:
                self.state.title_reset()
            elif new_game_phase == GamePhase.GAMEOVER:
                self._display.save_surface()


    def stage_update(self):
        # ステージ処理に必要な内部データを取得する
        command = self.state.get_game_command()
        player = self.state.get_player_data()
        objects = self.state.get_objects_data()
        stage = self.state.get_stage_number()


        # 4カウントごとにゲーム内部の主要な更新処理を行う
        if self.count == 0 or self.count % 4 == 0:
            # マップを更新し、ステージクリア条件を判定する
            is_gameclear = self.system.map_update(self.count, objects, stage)
            self.state.set_is_gameclear(is_gameclear)

            # 入力コマンドに応じてプレイヤーの当たり判定位置を更新する
            self.system.player_move_state_update(command, player)

            # プレイヤーとステージオブジェクトの当たり判定を行う
            self.system.player_hit_check(self.count, player, objects)

            # 現在の切迫度からゲームオーバー条件を判定する
            hp = self.state.get_urgency_level()
            is_gameover = hp >= 100
            self.state.set_is_gameover(is_gameover)

            # 攻撃入力があった場合は攻撃データを生成する
            if command == Command.ATTACK:
                attack = self.state.get_attack_data()
                self.system.player_attack(player, objects, attack)

        # プレイヤーの描画座標を毎カウント更新する
        self.system.player_move(player)
        self.system.player_position_update(player)

        self.system.draw_is_middle_lane_update(objects, player)


    def draw(self):
        # 現在のゲーム進行状態を取得する
        game_state = self.state.get_game_phase()

        if game_state == GamePhase.PAUSE:
            self._display.load_surface()
            self._display.draw_black_overlay()
            pause = self.state.get_pause_scene_selection()
            self._display.draw_pause(pause)

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
            attack_data = self.state.get_attack_data()

            self._display.draw_stage_object(player_data, map_data, attack_data)


            # 切迫度などのUIを描画する
            urgency_level = self.state.get_urgency_level()
            self._display.draw_urgency_level(urgency_level)

        # ゲームクリア画面を描画する
        elif game_state == GamePhase.CLEAR:
            clear = self.state.get_gameclear_scene_selection()
            self._display.draw_clear(clear)

        # ゲームオーバー画面を描画する
        elif game_state == GamePhase.GAMEOVER:
            self._display.load_surface()
            self._display.draw_black_overlay()
            over= self.state.get_gameover_scene_selection()
            self._display.draw_over(over)

        # エンディング画面を描画する
        elif game_state == GamePhase.ENDING:
            self._display.draw_ending()

        # self.renderer.touch_render()
        self._display.touch_iamge_render()

        self._display.output()

    def loop(self):

        # 入力状態を更新する
        self.input.command_update()

        # 4カウントごとに入力とゲーム進行を更新する
        if self.count % 4 == 0:

            # 現在の入力コマンドを取得して保存する
            command = self.input.get_command()
            self.state.set_game_command(command)

            # ボタンが押された場合は効果音を再生する
            if self.input.get_is_click():
                self.system.play_PushButton()

            # ゲームフェーズを更新する
            self.progress_update()

        # フェーズ更新後の状態を取得する
        phase = self.state.get_game_phase()

        # ステージ中のみステージ内部処理を行う
        if phase == GamePhase.STAGE:
            self.stage_update()

        # 現在のゲーム状態を描画する
        self.draw()

        # エンディング終了後にゲームループを終了する
        if phase == GamePhase.ENDING:
            if self.count > 30:
                return False

        # ゲーム全体で使用するカウントを更新する
        self.count += 1

        return self.loop_flug

    
    def close(self):
        if self.mode:
            self._display.fb_close()
        pygame.quit()