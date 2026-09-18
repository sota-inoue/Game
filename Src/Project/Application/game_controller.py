import pygame
from Domain.state import Command

# 入力処理を管理するクラス
from Input.input_manager import Input

# ゲーム内の状態を管理するクラス
from Domain.state import State, GameState, TitleState, Command, ClearState, StageState, OverState

# 描画処理を管理するクラス
from Renderer.renderer_manager import Renderer

# ゲームの進行や内部処理を管理するクラス
from System.system_manager import System

# 画面への出力処理を管理するクラス
from Display.display_manager import Display



class Controller:
    def __init__(self,mode):
        self.mode = mode
        pygame.init()
        
        self.display = Display(mode)
        GAME_SCREEN_WIDTH = self.display.GAME_SCREEN_WIDTH
        GAME_SCREEN_HEIGHT = self.display.GAME_SCREEN_HEIGHT
        TOUCH_SCREEN_WIDTH = self.display.TOUCH_SCREEN_WIDTH
        TOUCH_SCREEN_HEIGHT = self.display.TOUCH_SCREEN_HEIGHT

        self.input = Input(mode)
        self.renderer = Renderer(GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT, TOUCH_SCREEN_WIDTH, TOUCH_SCREEN_HEIGHT)
        self.system = System(GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT)
        self.state = State(GAME_SCREEN_WIDTH)

        #self.system.play_TitleBGM()
        self.loop_flug = True
        self.count = 0
        self.prev_command = Command.STAY

    def command_update(self):
        self.input.command_update()
        # self.input.debug_log(self.count)
        if self.count % 5 == 0:
            if self.input.get_is_click():
                self.system.play_PushButton()
            command = self.input.get_command()
            self.state.set_game_command(command)

    def title_system(self):
        if self.count % 5 != 0:
            return
        
        title_state = self.state.get_title_state()
        cmd = self.state.get_game_command()
        new_state = self.system.title_update(cmd, title_state)
        if new_state == TitleState.EXIT_DECIDE:
            self.loop_flug = False
        elif new_state == TitleState.START_DECIDE:
            self.state.set_game_command(Command.STAY)
            self.state.set_title_state(TitleState.START)
            if self.state.get_is_first_play():
                self.state.set_is_first_play(False)
                self.state.set_op_page(1)
                self.state.set_game_state(GameState.OP)
                self.prev_command = cmd  # 遷移時の入力による即時ページスキップを防止
            else:
                self.state.set_game_state(GameState.STAGE)        
        else:
            self.state.set_title_state(new_state)

    def op_system(self):
        cmd = self.state.get_game_command()
        # ボタンが新たに押された瞬間（押し下げ）のみページ送りを行う
        if cmd != Command.STAY and self.prev_command == Command.STAY:
            current_page = self.state.get_op_page()
            if current_page < 3:
                self.state.set_op_page(current_page + 1)
            else:
                self.state.set_game_state(GameState.STAGE)
            self.state.set_game_command(Command.STAY)

    def clear_system(self):
        state = self.state.get_clear_state()
        cmd = self.state.get_game_command()
        stage = self.state.get_stage_state()
        # 最終ステージならエンディングへ
        if stage == StageState.STAGE3:
            self.state.set_game_state(GameState.ENDING)
        elif state == ClearState.NEXT:
            if cmd == Command.JUMP:
                # 次のステージへ進む
                self.state.set_stage_state(StageState(stage.value + 1))
                self.state.set_game_state(GameState.STAGE)
                self.state.stage_reset()
                player = self.state.get_player_data()
                self.system.player_locate_update(player)
            elif cmd == Command.RIGHT:
                self.state.set_clear_state(ClearState.TITLE)
        elif state == ClearState.TITLE:
            if cmd == Command.JUMP:
                self.state.title_reset()
                player = self.state.get_player_data()
                self.system.player_locate_update(player)
            elif cmd == Command.LEFT:
                self.state.set_clear_state(ClearState.NEXT)

    def over_system(self):
        state = self.state.get_over_state()
        cmd = self.state.get_game_command()

        if state == OverState.CONTINUE:
            if cmd == Command.JUMP:
                # ゲームを再開する
                self.state.stage_reset()
                player = self.state.get_player_data()
                self.system.player_locate_update(player)
                self.state.set_game_state(GameState.STAGE)
            elif cmd == Command.RIGHT:
                self.state.set_over_state(OverState.TITLE)
        elif state == OverState.TITLE:
            if cmd == Command.JUMP:
                # タイトル画面へ戻る
                self.state.title_reset()
                player = self.state.get_player_data()
                self.system.player_locate_update(player)
            elif cmd == Command.LEFT:
             self.state.set_over_state(OverState.CONTINUE)


    def system_update(self):
        game_state = self.state.get_game_state()

        if game_state == GameState.TITLE:
            self.title_system()

        elif game_state == GameState.OP:
            self.op_system()

        elif game_state == GameState.STAGE:

            command = self.state.get_game_command()
            player = self.state.get_player_data()
            objects = self.state.get_objects_data()
            stage = self.state.get_stage_state()

            if self.count % 5 == 3:
                self.system.object_hit_check(objects)

            if self.count == 0 or self.count % 5 == 0:
                if not self.system.map_update(self.count, objects, stage):
                    self.state.set_game_state(GameState.CLEAR)
                self.system.player_position_update(command, player)
                self.system.player_hit_check(self.count, player, objects)
                hp = self.state.get_urgency_level()
                if hp >= 100:
                    self.state.set_game_state(GameState.OVER)

                if command == Command.ATTACK:
                    attack = self.system.player_attack(player, objects)
                    self.state.set_attack_data(attack)
            self.system.player_locate_update(player)

        elif game_state == GameState.OVER:
            self.over_system()
        elif game_state == GameState.CLEAR:
            self.clear_system()

        self.prev_command = self.state.get_game_command()
        new_game_state = self.state.get_game_state()
        if game_state != new_game_state:
            self.count = 0
        else:
            self.count += 1

    def draw(self):
        game_state = self.state.get_game_state()

        if game_state == GameState.TITLE:
            title_state = self.state.get_title_state()
            self.renderer.draw_Title(title_state)

        elif game_state == GameState.OP:
            self.renderer.draw_Opening(self.state.get_op_page())

        elif game_state == GameState.STAGE:
            self.renderer.draw_Stage()

            map_data = self.state.get_draw_data()
            player_data = self.state.get_player_draw_data()
            attack_date = self.state.get_attack_draw_data()

            self.renderer.draw_stage_object(player_data, attack_date, map_data)

            self.renderer.draw_UI(self.state.get_urgency_level())

        elif game_state == GameState.CLEAR:
            clear_state = self.state.get_clear_state()
            self.renderer.draw_Clear(clear_state)

        elif game_state == GameState.OVER:
            over_state = self.state.get_over_state()
            self.renderer.draw_Over(over_state)

        elif game_state == GameState.ENDING:
            self.renderer.draw_Ending()

        self.renderer.touch_render()

    def output(self):
        self.display.update(
            self.renderer.get_game(),
            self.renderer.get_touch()
        )

    def loop(self):
        self.command_update()
        self.system_update()
        self.draw()
        self.output()
        if self.state.get_game_state()== GameState.ENDING:
            if self.count > 30:
                return False
        return self.loop_flug

    
    def close(self):
        if self.mode:
            self.display.fb_close()
        pygame.quit()