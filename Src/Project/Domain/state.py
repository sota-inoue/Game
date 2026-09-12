from StageObject.player import Player
from Domain.game_flag import GameFlag, GameState, TitleState, OpeningState, GameOverState, ClearState, StageState
from Input.command_converter import Command



class State:
    def __init__(self, width):
        self.game_command = Command.NONE

        self._game_flag = GameFlag()

        # 7レーン × 5マスのオブジェクトデータを生成する
        self._objects = [ [None for _ in range(5)] for _ in range(7)]
        self._player = Player(width)

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

    def get_game_state(self) -> GameState:
        return self._game_flag.get_game_state()

    def get_title_state(self) -> TitleState:
        return self._game_flag.get_title_state()

    def get_opening_state(self) -> OpeningState:
        return self._game_flag.get_opening_state()

    def get_gameover_state(self) -> GameOverState:
        return self._game_flag.get_gameover_state()

    def get_clear_state(self) -> ClearState:
        return self._game_flag.get_clear_state()

    def get_stage_state(self) -> StageState:
        return self._game_flag.get_stage_state()

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

    def get_attack_draw_data(self) -> dict | None:
        index = self.attack_count
        obj = self._attack[index]
        if obj is None:
            return None
        data = {
            "x": obj.get_x(),
            "y": obj.get_y(),
            "width": obj.get_width(),
            "height": obj.get_height(),
            "image_path": obj.get_image_path()
        }
        self.attack_count += 1
        # 5個目の描画データを取得した後にリセット
        if index == 4:
            self._attack = [None for _ in range(5)]
            self.attack_count = 0
        return data

    def get_player_draw_data(self) -> dict:
        return {
            "x": self._player.get_x(),
            "y": self._player.get_y(),
            "width": self._player.get_width(),
            "height": self._player.get_height(),
            "image_path": self._player.get_image_path()
        }

    def get_draw_data(self) -> list[list[dict | None]]:
        draw_data = []
        i = 0
        while i < len(self._objects):
            lane = []
            j = 0
            while j < len(self._objects[i]):
                obj = self._objects[i][j]

                if obj is None:
                    lane.append(None)

                else:
                    lane.append({
                        "x": obj.get_x(),
                        "y": obj.get_y(),
                        "width": obj.get_width(),
                        "height": obj.get_height(),
                        "image_path": obj.get_image_path()
                    })
                j += 1
            draw_data.append(lane)
            i += 1
        return draw_data
    

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


