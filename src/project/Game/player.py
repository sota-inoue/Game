import pygame
from enum import Enum

class State_x(Enum):
    STAY = 0
    LEFT = 1
    RIGHT = 2

class State_y(Enum):
    STAY = 0
    JUMP = 1
    DOWN = 2

class Command(Enum):
    LEFT = "LEFT"
    JUMP = "JUMP"
    RIGHT = "RIGHT"
    STAY = "STAY"

class Player:
    def __init__(self, width, y):
        # プレイヤーの横幅と縦幅、比率は3:5
        self.player_width = width // 10
        self.player_height = self.player_width * 5 // 3

        # 障害物の高さ
        self.obstacle_size = width // 20

        # マス目のx座標
        self.X1 = width // 6
        self.X2 = width * 2 // 6
        self.X3 = width * 3 // 6
        self.X4 = width * 4 // 6
        self.X5 = width * 5 // 6

        # マス目のy座標
        self.Y1 = y
        self.Y2 = y + self.obstacle_size*2

        # プレイヤーの初期座標
        self.player_x = self.X3
        self.player_y = self.Y1

        # 移動の状態
        self.state_x = State_x.STAY
        self.state_y = State_y.STAY

        # 移動予定の座標
        self.next_locate_x = self.player_x
        self.next_locate_y = self.player_y