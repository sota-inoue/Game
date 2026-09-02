from enum import Enum, auto

from StageObject.stage_object import StageObject, ObjectType

from Domain.asset_paths import PLAYER_IMAGE_PATH

class Player_Move_State_x(Enum):
    STAY = auto()
    LEFT = auto()
    RIGHT = auto()

class Player_Move_State_y(Enum):
    STAY = auto()
    JUMP = auto()
    DOWN = auto()

class Player_Position_x(Enum):
    X1 = auto()
    X2 = auto()
    X3 = auto()
    X4 = auto()
    X5 = auto()

class Player_Position_y(Enum):
    Y1 = auto()
    Y2 = auto()



class Player(StageObject):
    def __init__(self, width) -> None:
        super().__init__(object_type = ObjectType.PLAYER)

        self.set_image_path(PLAYER_IMAGE_PATH)

        player_width = width // 10
        player_height = player_width * 5 // 3
        self.set_width(player_width)
        self.set_height(player_height)

        self._power: int = 1
        self._urgency_level: int = 0
        self._state_x: Player_Move_State_x = Player_Move_State_x.STAY
        self._state_y: Player_Move_State_y = Player_Move_State_y.STAY
        self._plaer_position_x: Player_Position_x = Player_Position_x.X3
        self._player_position_y: Player_Position_y = Player_Position_y.Y1

    # power
    def get_power(self):
        return self._power

    def set_power(self, power: int):
        if not isinstance(power, int):
            raise TypeError(f"受け取った値: {type(power).__name__}: int型を指定してください。")
        self._power = power

    # urgency_level
    def get_urgency_level(self):
        return self._urgency_level
    
    def set_urgency_level(self, urgency_level: int):
        if not isinstance(urgency_level, int):
            raise TypeError(f"受け取った値: {type(urgency_level).__name__}: int型を指定してください。")
    
        if urgency_level < 0:
            urgency_level = 0
        elif urgency_level > 100:
            urgency_level = 100
    
        self._urgency_level = urgency_level

    # _state_xのgetterとsetter
    def get_state_x(self):
        return self._state_x

    def set_state_x(self, state_x: Player_Move_State_x):
        if not isinstance(state_x, Player_Move_State_x):
            raise TypeError(f"受け取った値: {type(state_x).__name__}: Player_Move_State_x型を指定してください。")
        self._state_x = state_x

    # _state_yのgetterとsetter
    def get_state_y(self):
        return self._state_y

    def set_state_y(self, state_y: Player_Move_State_y):
        if not isinstance(state_y, Player_Move_State_y):
            raise TypeError(f"受け取った値: {type(state_y).__name__}: Player_Move_State_y型を指定してください。")
        self._state_y = state_y
        

    # _player_position_xのgetterとsetter
    def get_position_x(self):
        return self._plaer_position_x
    
    def set_position_x(self, position_x: Player_Position_x):
        if not isinstance(position_x, Player_Position_x):
            raise TypeError(f"受け取った値: {type(position_x).__name__}: Player_Position_x型を指定してください。")
        self._plaer_position_x = position_x
    
    # _player_position_yのgetterとsetter
    def get_position_y(self):
        return self._player_position_y  
    
    def set_position_y(self, position_y: Player_Position_y):
        if not isinstance(position_y, Player_Position_y):
            raise TypeError(f"受け取った値: {type(position_y).__name__}: Player_Position_y型を指定してください。")
        self._player_position_y = position_y