from enum import Enum
from typing import List

class GameState(Enum):
    TITLE = 0
    OP = 1
    STAGE = 2
    OVER = 3
    CLEAR = 4

class State:
    """ゲーム内で変化する内部データを管理するクラス"""

    def __init__(self) -> None:

        self.player_x: int = 0
        self._player_y: int = 0

        self.input_x: int = 0
        self.input_y: int = 0

        self.map_data: List[List[int]] = [
            [0 for _ in range(7)]
            for _ in range(5)
        ]

        self.game_state: GameState = GameState.TITLE
        self.count: int = 0
        self.is_colliding: bool = False
        self.urgency_level: int = 0

    # player_x

    def get_player_x(self) -> int:
        return self.player_x

    def set_player_x(self, player_x: int) -> None:
        self.player_x = player_x

    # player_y

    def get_player_y(self) -> int:
        return self.player_y

    def set_player_y(self, player_y: int) -> None:
        self.player_y = player_y

    # input_x

    def get_input_x(self) -> int:
        return self.input_x

    def set_input_x(self, input_x: int) -> None:
        self.input_x = input_x

    # input_y

    def get_input_y(self) -> int:
        return self.input_y

    def set_input_y(self, input_y: int) -> None:
        self.input_y = input_y

    # map_data

    def get_map_data(self) -> List[List[int]]:
        return [row.copy() for row in self.map_data]

    def set_map_data(self, map_data: List[List[int]]) -> None:
        if len(map_data) != 5:
            raise ValueError("map_dataの行数は5にしてください。")

        if any(len(row) != 7 for row in map_data):
            raise ValueError("map_dataの列数は7にしてください。")

        self.map_data = [row.copy() for row in map_data]

    # game_state

    def get_game_state(self) -> GameState:
        return self.game_state

    def set_game_state(self, game_state: GameState) -> None:
        if not isinstance(game_state, GameState):
            raise TypeError("game_stateにはGameState型を指定してください。")

        self.game_state = game_state

    # count

    def get_count(self) -> int:
        return self.count

    def set_count(self, count: int) -> None:
        if count < 0:
            raise ValueError("countには0以上の値を指定してください。")

        self.count = count

    # is_colliding

    def get_is_colliding(self) -> bool:
        return self.is_colliding

    def set_is_colliding(self, is_colliding: bool) -> None:
        self.is_colliding = is_colliding

    # urgency_level

    def get_urgency_level(self) -> int:
        return self.urgency_level

    def set_urgency_level(self, urgency_level: int) -> None:
        if not 0 <= urgency_level <= 100:
            raise ValueError(
                "urgency_levelには0から100までの値を指定してください。"
            )

        self.urgency_level = urgency_level