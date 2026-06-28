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
    LEFT = 0
    JUMP = 1
    RIGHT = 2
    STAY = 3

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

    # 外部から受け取った入力コマンドに応じて、プレイヤーの横方向・縦方向の状態を変更する
    def set_command(self, command):
        
        # 左移動の入力を受け取った場合、横方向の状態をLEFTにする
        if command == Command.LEFT:
            self.state_x = State_x.LEFT

        # 右移動の入力を受け取った場合、横方向の状態をRIGHTにする
        elif command == Command.RIGHT:
            self.state_x = State_x.RIGHT

        # ジャンプ入力を受け取った場合、プレイヤーが地上にいるときだけジャンプ状態にする
        elif command == Command.JUMP:
            if self.state_y == State_y.STAY:
                self.state_y = State_y.JUMP

        # 入力がない場合は状態を変更しない
        elif command == Command.STAY:
            pass

    # プレイヤーの状態と現在位置をもとに、次の移動先を決める関数
    def set_locate(self):
        
        # 横方向の状態がRIGHTの場合、右隣の座標を次の移動先にする
        if self.state_x == State_x.RIGHT:

            # 左端にいる場合は、これ以上左に移動できないため、次の移動先を決めない
            if self.player_x == self.X1:
                    return

            # 現在位置がX1以上X2未満の場合、次の移動先をX2にする
            if self.X1 <= self.player_x < self.X2:
                self.next_locate_x = self.X2

            # 現在位置がX2以上X3未満の場合、次の移動先をX3にする
            elif self.X2 <= self.player_x < self.X3:
                self.next_locate_x = self.X3

            # 現在位置がX3以上X4未満の場合、次の移動先をX4にする
            elif self.X3 <= self.player_x < self.X4:
                self.next_locate_x = self.X4

            # 現在位置がX4以上X5未満の場合、次の移動先をX5にする
            elif self.X4 <= self.player_x < self.X5:
                self.next_locate_x = self.X5

        # 横方向の状態がLEFTの場合、左隣の座標を次の移動先にする
        elif self.state_x == State_x.LEFT:

            # 右端にいる場合は、これ以上左に移動できないため、次の移動先を決めない
            if self.player_x == self.X5:
                    return

            # 現在位置がX4より大きくX5以下の場合、次の移動先をX4にする
            if self.X4 < self.player_x <= self.X5:
                self.next_locate_x = self.X4

            # 現在位置がX3より大きくX4以下の場合、次の移動先をX3にする
            elif self.X3 < self.player_x <= self.X4:
                self.next_locate_x = self.X3

            # 現在位置がX2より大きくX3以下の場合、次の移動先をX2にする
            elif self.X2 < self.player_x <= self.X3:
                self.next_locate_x = self.X2

            # 現在位置がX1より大きくX2以下の場合、次の移動先をX1にする
            elif self.X1 < self.player_x <= self.X2:
                self.next_locate_x = self.X1