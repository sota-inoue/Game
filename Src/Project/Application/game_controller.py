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

from Domain.StageObject.stage_object_manager import StageObjectManager



class Controller:
    def __init__(self,mode):
        self.mode = mode
        pygame.init()
        self.state = State()
        self.display = Display(mode)
        self.input = Input(mode)
        self.renderer = Renderer(
            self.display.GAME_SCREEN_WIDTH,
            self.display.GAME_SCREEN_HEIGHT,
            self.display.TOUCH_SCREEN_WIDTH,
            self.display.TOUCH_SCREEN_HEIGHT
        )
        self.system = System()

        self.stageobject = StageObjectManager(self.display.GAME_SCREEN_WIDTH, self.display.GAME_SCREEN_HEIGHT)

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
        if self.count <= 0 or self.count % 5 != 0:
            return

        title_state = self.state.get_title_state()
        cmd = self.state.get_game_command()

        if title_state == TitleState.START:
            if cmd == Command.JUMP:
                self.state.set_game_state(GameState.OP)
                self.state.set_game_command(Command.STAY)

            elif cmd == Command.RIGHT:
                self.state.set_title_state(TitleState.SETTING)

        elif title_state == TitleState.SETTING:
            if cmd == Command.RIGHT:
                self.state.set_title_state(TitleState.EXIT)

            elif cmd == Command.LEFT:
                self.state.set_title_state(TitleState.START)

        elif title_state == TitleState.EXIT:
            if cmd == Command.JUMP:
                self.loop_flug = False

            elif cmd == Command.LEFT:
                self.state.set_title_state(TitleState.SETTING)



    def system_update(self):
        game_state = self.state.get_game_state()

        if game_state == GameState.TITLE:
            self.title_system()

        elif game_state == GameState.OP:
            if self.count == 20:
                self.state.set_game_state(GameState.STAGE)
                self.state.set_game_command(Command.STAY)

        elif game_state == GameState.STAGE:
            self.stageobject.player_locate_update()

            if self.count > 0 and self.count % 5 == 0:
                command = self.state.get_game_command()
                self.stageobject.player_position_update(command)
                self.stageobject.player_hit_check(self.count)
                self.stageobject.map_update(self.count)

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

            map_data = self.stageobject.get_draw_data()
            player_data = self.stageobject.get_player_draw_data()

            self.renderer.draw_stage_object(player_data, map_data)

            self.renderer.draw_UI(self.stageobject.get_urgency_level())

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