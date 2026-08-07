from enum import Enum, auto
from typing import List


class Command(Enum):
    LEFT = auto()
    JUMP = auto()
    RIGHT = auto()
    STAY = auto()

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
        self.player_x= 0
        self.player_y = 0
        self.count = 0
        self.game_state = GameState.TITLE
        self.game_command = Command.STAY
        self.collision = False
        self.player_position = (2, 0)
        self.urgency_levelt = 0

        self.map_data: List[List[int]] = [
            [0 for _ in range(5)]
            for _ in range(7)
        ]


    # player_x
    def get_player_x(self):
        return self.player_x
    
    def set_player_x(self, x):
        self.player_x = x
    
    # player_y
    def get_player_y(self):
        return self.player_y
    
    def set_player_y(self, y):
        self.player_y = y

    # input_x
    def get_input_x(self):
        return self.input_x
    
    def set_input_x(self, x):
        self.input_x = x

    # input_y
    def get_input_y(self):
        return self.input_y
    
    def set_input_y(self, y):
        self.input_y = y

    # game_state
    def get_game_state(self):
        return self.game_state
    
    def set_game_state(self, game_state):
        self.game_state = game_state

    # game_command
    def get_game_command(self):
        return self.game_command
        
    def set_game_command(self, game_command):
        self.game_command = game_command

    # count
    def get_count(self):
        return self.count
    
    def set_count(self, count):
        self.count = count

    # map_data
    def get_map_data(self):
        return [row.copy() for row in self.map_data]

    def get_front_map_data(self):
        """ステージデータの最前列（最初の行）を返す"""
        return self.map_data[0].copy()

    def set_map_data(self, map_data):
        self.map_data = [row.copy() for row in map_data]


    # collision
    def get_collision(self):
        return self.collision

    def set_collision(self, collision):
        self.collision = collision

    # player_position
    def get_player_position(self):
        return self.player_position

    def set_player_position(self, grid_position):
        self.player_position = grid_position

    # urgency_level
    def get_urgency_level(self):
        return self.urgency_levelt

    def set_urgency_level(self, urgency_level):
        if urgency_level < 0:
            urgency_level = 0
        elif urgency_level > 100:
            urgency_level = 100
        else:
            self.urgency_levelt = urgency_level