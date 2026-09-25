from enum import Enum, auto

from asset_paths import PLAYER_IMAGE_PATH

class Player_Move_State_x(Enum):
    STAY = auto()
    LEFT = auto()
    RIGHT = auto()

class Player_Move_State_y(Enum):
    STAY = auto()
    JUMP = auto()
    DOWN = auto()

class Player_Position_x(Enum):
    X1 = 0
    X2 = 1
    X3 = 2
    X4 = 3
    X5 = 4

class Player_Position_y(Enum):
    Y1 = 0
    Y2 = 1


class Player_Layout_x(Enum):
    X1_0 = 0

    X1_1 = 1
    X1_2 = 2
    X1_3 = 3

    X2_0 = 4

    X2_1 = 5
    X2_2 = 6
    X2_3 = 7

    X3_0 = 8

    X3_1 = 9
    X3_2 = 10
    X3_3 = 11

    X4_0 = 12

    X4_1 = 13
    X4_2 = 14
    X4_3 = 15

    X5_0 = 16

class Player_Layout_y(Enum):
    Y1_0 = 0

    Y1_1 = 1
    Y1_2 = 2
    Y1_3 = 3

    Y2_0 = 4
    
    Y2_1 = 5
    Y2_2 = 6
    Y2_3 = 7

    Y3_0 = 8



class Player():
    def __init__(self) -> None:

        self._image_path = PLAYER_IMAGE_PATH

        self._power: int = 1
        self._urgency_level: int = 0

        self._state_x: Player_Move_State_x = Player_Move_State_x.STAY
        self._state_y: Player_Move_State_y = Player_Move_State_y.STAY

        self._player_position_x: Player_Position_x = Player_Position_x.X3
        self._player_position_y: Player_Position_y = Player_Position_y.Y1

        self._player_layout_x: Player_Layout_x = Player_Layout_x.X3_0
        self._player_layout_y: Player_Layout_y = Player_Layout_y.Y1_0


    def reset(self) -> None:
        self._urgency_level = 0

        self._state_x = Player_Move_State_x.STAY
        self._state_y = Player_Move_State_y.STAY

        self._player_position_x = Player_Position_x.X3
        self._player_position_y = Player_Position_y.Y1

        self._player_layout_x = Player_Layout_x.X3_0
        self._player_layout_y = Player_Layout_y.Y1_0


    def get_image_path(self) -> str:
        return self._image_path


    # power
    def get_power(self):
        return self._power

    def set_power(self, power: int) -> None:
        if not isinstance(power, int):
            raise TypeError(f"受け取った値: {type(power).__name__}: int型を指定してください。")
        self._power = power


    # urgency_level
    def get_urgency_level(self):
        return self._urgency_level

    def set_urgency_level(self, urgency_level: int) -> None:
        if not isinstance(urgency_level, int):
            raise TypeError(f"受け取った値: {type(urgency_level).__name__}: int型を指定してください。")

        if urgency_level < 0:
            urgency_level = 0
        elif urgency_level > 100:
            urgency_level = 100

        self._urgency_level = urgency_level


    # state_x
    def get_state_x(self):
        return self._state_x

    def set_state_x(self, state_x: Player_Move_State_x) -> None:
        if not isinstance(state_x, Player_Move_State_x):
            raise TypeError(f"受け取った値: {type(state_x).__name__}: Player_Move_State_x型を指定してください。")
        self._state_x = state_x


    # state_y
    def get_state_y(self):
        return self._state_y

    def set_state_y(self, state_y: Player_Move_State_y) -> None:
        if not isinstance(state_y, Player_Move_State_y):
            raise TypeError(f"受け取った値: {type(state_y).__name__}: Player_Move_State_y型を指定してください。")
        self._state_y = state_y


    # player_position_x
    def get_position_x(self):
        return self._player_position_x

    def set_position_x(self, position_x: Player_Position_x) -> None:
        if not isinstance(position_x, Player_Position_x):
            raise TypeError(f"受け取った値: {type(position_x).__name__}: Player_Position_x型を指定してください。")
        self._player_position_x = position_x

    # player_position_y
    def get_position_y(self):
        return self._player_position_y

    def set_position_y(self, position_y: Player_Position_y) -> None:
        if not isinstance(position_y, Player_Position_y):
            raise TypeError(f"受け取った値: {type(position_y).__name__}: Player_Position_y型を指定してください。")
        self._player_position_y = position_y


    # player_layout_x
    def get_layout_x(self):
        return self._player_layout_x

    def set_layout_x(self, layout_x: Player_Layout_x) -> None:
        if not isinstance(layout_x, Player_Layout_x):
            raise TypeError(f"受け取った値: {type(layout_x).__name__}: Player_Layout_x型を指定してください。")
        self._player_layout_x = layout_x


    # player_layout_y
    def get_layout_y(self):
        return self._player_layout_y

    def set_layout_y(self, layout_y: Player_Layout_y) -> None:
        if not isinstance(layout_y, Player_Layout_y):
            raise TypeError(f"受け取った値: {type(layout_y).__name__}: Player_Layout_y型を指定してください。")
        self._player_layout_y = layout_y
