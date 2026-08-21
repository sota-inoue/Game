from enum import Enum, auto
from typing import List


class Command(Enum):
    LEFT = auto()
    JUMP = auto()
    RIGHT = auto()
    STAY = auto()


class TitleState(Enum):
    START = auto()
    SETTING = auto()
    EXIT = auto()


class GameState(Enum):
    TITLE = auto()
    OP = auto()
    STAGE = auto()
    OVER = auto()
    CLEAR = auto()


class State:
    def __init__(self):
        self.input_x = 0
        self.input_y = 0
        self.player_x = 0
        self.player_y = 0
        self.count = 0
        self.game_state = GameState.TITLE
        self.game_command = Command.STAY
        self.title_state = TitleState.START
        self.collision = False
        self.player_position = (2, 0)
        self.urgency_level = 0

        self.map_data: List[List[int]] = [
            [0 for _ in range(5)]
            for _ in range(7)
        ]

    # player_x
    def get_player_x(self):
        return self.player_x

    def set_player_x(self, x: int):
        if not isinstance(x, int):
            raise TypeError(
                f"player_xにはint型を指定してください。"
                f"受け取った値: {x}、型: {type(x).__name__}"
            )
        self.player_x = x

    # player_y
    def get_player_y(self):
        return self.player_y

    def set_player_y(self, y: int):
        if not isinstance(y, int):
            raise TypeError(
                f"player_yにはint型を指定してください。"
                f"受け取った値: {y}、型: {type(y).__name__}"
            )
        self.player_y = y

    # input_x
    def get_input_x(self):
        return self.input_x

    def set_input_x(self, x: int):
        if not isinstance(x, int):
            raise TypeError(
                f"input_xにはint型を指定してください。"
                f"受け取った値: {x}、型: {type(x).__name__}"
            )
        self.input_x = x

    # input_y
    def get_input_y(self):
        return self.input_y

    def set_input_y(self, y: int):
        if not isinstance(y, int):
            raise TypeError(
                f"input_yにはint型を指定してください。"
                f"受け取った値: {y}、型: {type(y).__name__}"
            )
        self.input_y = y

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
            self.count = 0
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
        self.count = 0
        self.title_state = title_state

    # count
    def get_count(self):
        return self.count

    def set_count(self, count: int):
        if not isinstance(count, int):
            raise TypeError(
                f"countにはint型を指定してください。"
                f"受け取った値: {count}、型: {type(count).__name__}"
            )
        self.count = count

    # map_data
    def get_map_data(self):
        return [row.copy() for row in self.map_data]

    def get_front_map_data(self):
        """ステージデータの最前列（最初の行）を返す"""
        return self.map_data[0].copy()

    def set_map_data(self, map_data: List[List[int]]):
        if not isinstance(map_data, list):
            raise TypeError(
                f"map_dataには二次元リストを指定してください。"
                f"受け取った型: {type(map_data).__name__}"
            )

        if len(map_data) != 7:
            raise ValueError(
                f"map_dataの行数は7行にしてください。"
                f"受け取った行数: {len(map_data)}"
            )

        for row in map_data:
            if not isinstance(row, list):
                raise TypeError(
                    f"map_dataの各行にはlist型を指定してください。"
                    f"受け取った型: {type(row).__name__}"
                )

            if len(row) != 5:
                raise ValueError(
                    f"map_dataの各行の要素数は5個にしてください。"
                    f"受け取った要素数: {len(row)}"
                )

            for value in row:
                if not isinstance(value, int):
                    raise TypeError(
                        f"map_dataの各要素にはint型を指定してください。"
                        f"受け取った値: {value}、型: {type(value).__name__}"
                    )

        self.map_data = [row.copy() for row in map_data]

    # collision
    def get_collision(self):
        return self.collision

    def set_collision(self, collision: bool):
        if not isinstance(collision, bool):
            raise TypeError(
                f"collisionにはbool型を指定してください。"
                f"受け取った値: {collision}、型: {type(collision).__name__}"
            )
        self.collision = collision

    # player_position
    def get_player_position(self):
        return self.player_position

    def set_player_position(self, grid_position: tuple):
        if (
            not isinstance(grid_position, tuple)
            or len(grid_position) != 2
            or not all(isinstance(value, int) for value in grid_position)
        ):
            raise TypeError(
                f"player_positionには整数2つのtupleを指定してください。"
                f"受け取った値: {grid_position}"
            )

        self.player_position = grid_position

    # urgency_level
    def get_urgency_level(self):
        return self.urgency_level

    def set_urgency_level(self, urgency_level: int):
        if not isinstance(urgency_level, int):
            raise TypeError(
                f"urgency_levelにはint型を指定してください。"
                f"受け取った値: {urgency_level}、型: {type(urgency_level).__name__}"
            )

        if urgency_level < 0:
            urgency_level = 0
        elif urgency_level > 100:
            urgency_level = 100

        self.urgency_level = urgency_level