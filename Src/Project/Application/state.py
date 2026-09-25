from Domain.player import Player
from Domain.game_flag import (
    GameFlag, GamePhase, TitleSceneSelection, OpeningPage,
    GameOverSceneSelection, GameClearSceneSelection, StageNumber
)
from Input.command_converter import Command



class State:
    def __init__(self):
        self.game_command = Command.NONE

        self._game_flag = GameFlag()

        # 7レーン × 5マスのオブジェクトデータを生成する
        self._objects = [ [None for _ in range(5)] for _ in range(7)]
        self._player = Player()

        self.attack_count = 0
        self._attack = [None for _ in range(5)]

    def title_reset(self):
        self.stage_reset()
        self._game_flag.reset()

    def stage_reset(self):
        self._objects = [ [None for _ in range(5)] for _ in range(7)]
        self._player.reset()
        self.attack_count = 0
        self._attack = [None for _ in range(5)]


    def get_objects_data(self):
        return self._objects

    def get_player_data(self):
        return self._player

    def get_game_flag(self):
        return self._game_flag

    # ==================================================
    # フラグのGetter
    # ==================================================

    def get_game_phase(self) -> GamePhase:
        return self._game_flag.get_game_phase()

    def get_title_scene_selection(self) -> TitleSceneSelection:
        return self._game_flag.get_title_selection()

    def get_opening_page(self) -> OpeningPage:
        return self._game_flag.get_opening_page()

    def get_gameover_scene_selection(self) -> GameOverSceneSelection:
        return self._game_flag.get_gameover_selection()

    def get_gameclear_scene_selection(self) -> GameClearSceneSelection:
        return self._game_flag.get_gameclear_selection()

    def get_stage_number(self) -> StageNumber:
        return self._game_flag.get_stage_number()

    # ==================================================
    # フラグのSetter
    # ==================================================

    def set_is_gameclear(self, value: bool) -> None:
        self._game_flag.set_is_gameclear(value)

    def set_is_gameover(self, value: bool) -> None:
        self._game_flag.set_is_gameover(value)




    def set_attack_data(self, data):
        self._attack = data

    def get_urgency_level(self) -> int:
        return self._player.get_urgency_level()

    

    # game_command
    def get_game_command(self):
        return self.game_command

    def set_game_command(self, game_command: Command):
        if not isinstance(game_command, Command):
            raise TypeError(
                f"game_commandにはCommand型を指定してください。"
                f"受け取った値: {game_command}、型: {type(game_command).__name__}"
            )
        self.game_command = game_command


