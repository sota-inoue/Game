import pygame
from Domain.state import Command

# 入力処理を管理するクラス
from Input.input_manager import Input

# ゲーム内の状態を管理するクラス
from Domain.state import State, GameState, TitleState, Command

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
            self.state.set_game_state(GameState.OP)
        else:
            self.state.set_title_state(new_state)

    def system_update(self):
        game_state = self.state.get_game_state()

        if game_state == GameState.TITLE:
            self.title_system()

        elif game_state == GameState.OP:
            if self.count == 20:
                self.state.set_game_state(GameState.STAGE)
                self.state.set_game_command(Command.STAY)

        elif game_state == GameState.STAGE:

            command = self.state.get_game_command()
            player = self.state.get_player_data()
            objects = self.state.get_objects_data()

            if self.count == 0 or self.count % 5 == 0:
                
                self.system.player_position_update(command, player)

                self.system.player_hit_check(self.count, player, objects)

                self.system.map_update(self.count, objects)

                if command == Command.ATTACK:
                    attack = self.system.player_attack(player, objects)
                    self.state.set_attack_data(attack)
            
            self.system.player_locate_update(player)

            if self.count == 100:
                self.state.set_game_state(GameState.CLEAR)

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
            self.renderer.draw_Opening()

        elif game_state == GameState.STAGE:
            self.renderer.draw_Stage()

            map_data = self.state.get_draw_data()
            player_data = self.state.get_player_draw_data()
            attack_date = self.state.get_attack_draw_data(self.count)

            self.renderer.draw_stage_object(player_data, attack_date, map_data)

            self.renderer.draw_UI(self.state.get_urgency_level())

        elif game_state == GameState.CLEAR:
            self.renderer.draw_Clear()

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
        if self.state.get_game_state()== GameState.CLEAR:
            if self.count > 30:
                return False
        return self.loop_flug

    
    def close(self):
        if self.mode:
            self.display.fb_close()
        pygame.quit()