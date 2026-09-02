from enum import Enum, auto
from StageObject.player import Player

class Command(Enum):
    LEFT = auto()
    JUMP = auto()
    RIGHT = auto()
    ATTACK = auto()
    POSE = auto()
    STAY = auto()

class TitleState(Enum):
    START = auto()
    START_DECIDE = auto()
    SETTING = auto()
    SETTINGT_DECIDE = auto()
    EXIT = auto()
    EXIT_DECIDE = auto()

class GameState(Enum):
    TITLE = auto()
    OP = auto()
    STAGE = auto()
    OVER = auto()
    CLEAR = auto()

class State:
    def __init__(self, width):
        self.game_state = GameState.TITLE
        self.game_command = Command.STAY
        self.title_state = TitleState.START

        # 7レーン × 5マスのオブジェクトデータを生成する
        self._objects = [ [None for _ in range(5)] for _ in range(7)]
        self._player = Player(width)
        self._attack = [None for _ in range(5)]


    def get_objects_data(self):
        return self._objects

    def get_player_data(self):
        return self._player

    def set_attack_data(self, data):
        self._attack = data

    def get_urgency_level(self) -> int:
        return self._player.get_urgency_level()

    def get_attack_draw_data(self, count: int) -> dict | None:
        index = count % 5
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
        # 5個目の描画データを取得した後にリセット
        if index == 4:
            self._attack = [None for _ in range(5)]
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
    

    # game_state
    def get_game_state(self):
        return self.game_state

    def set_game_state(self, game_state: GameState):
        if not isinstance(game_state, GameState):
            raise TypeError(
                f"game_stateにはGameState型を指定してください。"
                f"受け取った値: {game_state}、型: {type(game_state).__name__}"
            )
        if self.game_state != game_state:
            self.game_state = game_state

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

    # title_state
    def get_title_state(self):
        return self.title_state

    def set_title_state(self, title_state: TitleState):
        if not isinstance(title_state, TitleState):
            raise TypeError(
                f"title_stateにはTitleState型を指定してください。"
                f"受け取った値: {title_state}、型: {type(title_state).__name__}"
            )
        self.title_state = title_state


