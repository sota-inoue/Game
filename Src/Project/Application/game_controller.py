import pygame

from Input.command_converter import Command

# 入力処理を管理するクラス
from Input.input_manager import Input

# ゲーム内の状態を管理するクラス
from State.state_manager import State
from State.game_flag import GamePhase, StageNumber


# ゲームの進行や内部処理を管理するクラス
from System.system_manager import System

# 画面への出力処理を管理するクラス
from Display.display_manager import DisplayManager



class Controller:
    def __init__(self,mode):
        self.mode = mode
        pygame.init()
        
        print("DisplayManager 開始", flush=True)
        self._display = DisplayManager(mode)
        print("DisplayManager 完了", flush=True)

        print("Input 開始", flush=True)
        self.input = Input(mode)
        print("Input 完了", flush=True)

        print("System 開始", flush=True)
        self.system = System()
        print("System 完了", flush=True)

        print("State 開始", flush=True)
        self.state = State()
        print("State 完了", flush=True)

        # self.system.play_TitleBGM()
        self.loop_flug = True
        self.count = 0

        self._last_count = 0


    def input_update(self):

        self.input.command_update()

        # 4カウントごとに入力とゲーム進行を更新する
        if self.count % 4 == 0:

            # 現在の入力コマンドを取得して保存する
            command = self.input.get_command()

            # ボタンが押された場合は効果音を再生する
            if command != Command.NONE:
                self.system.play_se_decide_button()

            self.state.set_game_command(command)


    def progress_update(self):

        # 現在のゲーム進行状態と操作情報を取得する
        game_phase = self.state.get_game_phase()
        game_flag = self.state.get_game_flag()
        command = self.state.get_game_command()

        if game_phase == GamePhase.TITLE:
            self.loop_flug = self.system.title_update(command, game_flag)

        elif game_phase == GamePhase.OPENING and command == Command.RIGHT:
            self.state.set_game_phase(GamePhase.TITLE)

        elif game_phase == GamePhase.BOSS_INTRO and command == Command.RIGHT:
            self.state.set_game_phase(GamePhase.BOSS_STAGE)

        elif game_phase in (GamePhase.STAGE, GamePhase.BOSS_STAGE):

            if command == Command.PAUSE:
                self.state.set_game_phase(GamePhase.PAUSE)
                self._last_count = self.count
                self.count = 0
                self._display.save_surface()
                return

            else:
                # ステージ内部処理
                self.stage_update()

        elif game_phase == GamePhase.GAMEOVER:
            self.system.gameover_update(command, game_flag)

        elif game_phase == GamePhase.PAUSE:
            self.system.pause_update(command, game_flag)


    def stage_update(self):
        # ステージ処理に必要な内部データを取得する
        command = self.state.get_game_command()
        player = self.state.get_player_data()
        objects = self.state.get_objects_data()
        phase = self.state.get_game_phase()
        boss_hp = self.state.get_boss_hp()
        attack = self.state.get_attack_data()

        # 4カウントごとにゲーム内部の主要な更新処理を行う
        if self.count == 0 or self.count % 4 == 0:
            # マップを更新し、ステージクリア条件を判定する
            is_gameclear = self.system.map_update(self.count, objects, phase, boss_hp)

            if is_gameclear == True:
                self.count = 0
                if phase == GamePhase.STAGE:
                    self.state.set_game_phase(GamePhase.CLEAR)
                elif phase == GamePhase.BOSS_STAGE:
                    self.state.set_game_phase(GamePhase.BOSS_DEFEAT)

            # 入力コマンドに応じてプレイヤーの当たり判定位置を更新する
            self.system.player_move_state_update(command, player)

            # プレイヤーとステージオブジェクトの当たり判定を行う
            self.system.player_hit_check(self.count, player, objects)

            # 現在の切迫度からゲームオーバー条件を判定する
            hp = self.state.get_urgency_level()
            is_gameover = hp >= 100

            if is_gameover == True:
                self.state.set_game_phase(GamePhase.GAMEOVER)
                self._display.save_surface()


            # 攻撃入力があった場合は攻撃データを生成する
            if command == Command.ATTACK:
                if phase == GamePhase.STAGE:
                    self.system.player_attack(player, objects, attack)
                elif phase == GamePhase.BOSS_STAGE:
                    new_boss_hp = self.system.player_attack(player, objects, attack, boss_hp)
                    self.state.set_boss_hp(new_boss_hp)
                    is_gameclear = new_boss_hp <= 0
                    self.state.set_is_gameclear(is_gameclear)

        # プレイヤーの描画座標を毎カウント更新する
        self.system.player_move(player)
        self.system.player_position_update(player)

        self.system.draw_is_middle_lane_update(objects, player, self.count)


    def draw(self):
        # 現在のゲーム進行状態を取得する
        game_state = self.state.get_game_phase()

        if game_state == GamePhase.PAUSE:
            pause = self.state.get_pause_scene_selection()
            self._display.draw_pause(pause)

        # オープニング画面を描画する
        elif game_state == GamePhase.OPENING:
            if self._display.draw_opening(self.count):
                self.state.set_game_phase(GamePhase.TITLE)

        # タイトル画面を描画する
        elif game_state == GamePhase.TITLE:
            title = self.state.get_title_scene_selection()
            self._display.draw_title(title)


        # ゲームステージを描画する
        elif game_state == GamePhase.STAGE:
            # ステージの背景を描画する
            self._display.draw_stage()

            # ステージ内の描画に必要なデータを取得する
            map_data = self.state.get_objects_data()
            player_data = self.state.get_player_data()
            attack_data = self.state.get_attack_data()

            self._display.draw_stage_object(player_data, map_data, attack_data)

            urgency_level = self.state.get_urgency_level()
            self._display.draw_urgency_level(urgency_level)

        elif game_state == GamePhase.BOSS_STAGE:
            self._display.draw_boss_stage()
            self._display.draw_boss()

            boss_hp = self.state.get_boss_hp()
            self._display.draw_boss_health(boss_hp)

            map_data = self.state.get_objects_data()
            player_data = self.state.get_player_data()
            attack_data = self.state.get_attack_data()
            self._display.draw_boss_object(player_data, map_data, attack_data)

            urgency_level = self.state.get_urgency_level()
            self._display.draw_urgency_level(urgency_level)


        # ゲームクリア画面を描画する
        elif game_state == GamePhase.CLEAR:
            if self.count < 8:
                self._display.draw_clear()
            else:
                self.state.set_game_phase(GamePhase.BOSS_INTRO)

        elif game_state == GamePhase.BOSS_INTRO:
            if self.count == 0:
                self.system.play_se_boss_intro()
            if self._display.draw_boss_intro(self.count):
                self.state.set_game_phase(GamePhase.BOSS_STAGE)

        elif game_state == GamePhase.BOSS_DEFEAT:
            if self.count < 8:
                self._display.draw_clear()
            else:
                if self.count == 8:
                    self.system.play_se_boss_defeat()

                defeat_count = self.count - 8
                if self._display.draw_boss_defeat(defeat_count):
                    self.state.set_game_phase(GamePhase.ENDING)
                    self.count = 0

        # エンディング画面を描画する
        elif game_state == GamePhase.ENDING:
            if self.count == 0:
                self.system.play_se_ending()
            if self._display.draw_ending(self.count):
                self.state.set_game_phase(GamePhase.TITLE)

        # ゲームオーバー画面を描画する
        elif game_state == GamePhase.GAMEOVER:
            self._display.load_surface()
            self._display.draw_black_overlay()
            over= self.state.get_gameover_scene_selection()
            self._display.draw_over(over)

        # self.renderer.touch_render()
        self._display.touch_iamge_render()

        self._display.output()

    def update_phase_transition(self, before_phase: GamePhase, after_phase: GamePhase) -> None:

        # ゲーム状態が変化していない場合
        if before_phase == after_phase:
            self.count += 1
            return

        # ポーズから復帰した場合
        if before_phase == GamePhase.PAUSE and after_phase != GamePhase.PAUSE:

            # タイトルに戻る場合
            if after_phase == GamePhase.TITLE:
                self.state.title_reset()
                self.count = 0
                self._last_count = 0

                # タイトルBGMに切り替える
                self.system.stop_bgm()
                self.system.play_bgm_title()

            # ゲームに復帰する場合
            else:
                self.count = self._last_count
                self._last_count = 0

            self.state.set_game_command(Command.NONE)
            return

        # ポーズに入る場合
        # progress_update() で保存した _last_count を消さない
        if after_phase == GamePhase.PAUSE:
            return

        # 通常のゲーム状態が変化した場合
        self.count = 0
        self._last_count = 0
        self.system.stop_bgm()

        if after_phase == GamePhase.STAGE:
            self.state.set_game_command(Command.NONE)
            self.state.stage_reset()
            self.system.play_bgm_stage()

        elif after_phase == GamePhase.BOSS_STAGE:
            self.state.set_game_command(Command.NONE)
            self.state.stage_reset()
            self.system.play_bgm_boss()

        elif after_phase == GamePhase.TITLE:
            self.state.title_reset()
            self.system.play_bgm_title()

        elif after_phase == GamePhase.GAMEOVER:
            self._display.save_surface()
            self.system.play_se_gameover()

        elif after_phase == GamePhase.CLEAR:
            self._display.save_surface()
            self.count = 0

        elif after_phase == GamePhase.BOSS_DEFEAT:
            self._display.save_surface()
            self.count = 0

    def loop(self):
        self.input_update()

        before_phase = self.state.get_game_phase()
        self.progress_update()
        self.draw()
        after_phase = self.state.get_game_phase()

        # 描画前にフェーズ変更を反映する
        self.update_phase_transition(before_phase, after_phase)

        return self.loop_flug

    
    def close(self):
        if self.mode:
            self._display.fb_close()
        pygame.quit()