import pygame
from enum import Enum

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 450
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 100
PLAYER_SPEED = 5
FPS = 20
INPUT_WAIT_FRAME = 3
BACK_COLOR = (120, 120, 120)
PLAYER_COLOR = (0, 200, 80)

class State(Enum):
    STAY = 0
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

class Locate_x(Enum): 
    X1 = SCREEN_WIDTH//6 
    X2 = SCREEN_WIDTH*2//6 
    X3 = SCREEN_WIDTH*3//6 
    X4 = SCREEN_WIDTH*4//6 
    X5 = SCREEN_WIDTH*5//6

class Locate_y(Enum):
    Y1 = SCREEN_HEIGHT*6//9
    Y2 = SCREEN_HEIGHT*4//9


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        # プレイヤーの座標
        self.player_x = Locate_x.X3.value 
        self.player_y = Locate_y.Y1.value
        # 移動の状態
        self.state = State.STAY
        # 移動予定の座標
        self.location_x = Locate_x.X3.value
        self.location_y = Locate_y.Y1.value
        # 入力待機タイマー
        # 左右同時入力を検知するために、2フレーム以内に右と左入力を検知した場合に上移動状態になる
        self.right_timer = 0
        self.left_timer = 0

        self.run()

    # 次の移動先を決める関数
    def set_locate(self):
        if self.state == State.RIGHT:
            if Locate_x.X1.value <= self.player_x < Locate_x.X2.value:
                self.location_x = Locate_x.X2.value
            elif Locate_x.X2.value <= self.player_x < Locate_x.X3.value:
                self.location_x = Locate_x.X3.value
            elif Locate_x.X3.value <= self.player_x < Locate_x.X4.value:
                self.location_x = Locate_x.X4.value
            elif Locate_x.X4.value <= self.player_x < Locate_x.X5.value:
                self.location_x = Locate_x.X5.value
        elif self.state == State.LEFT:
            if Locate_x.X4.value < self.player_x <= Locate_x.X5.value:
                self.location_x = Locate_x.X4.value
            elif Locate_x.X3.value < self.player_x <= Locate_x.X4.value:
                self.location_x = Locate_x.X3.value
            elif Locate_x.X2.value < self.player_x <= Locate_x.X3.value:
                self.location_x = Locate_x.X2.value
            elif Locate_x.X1.value < self.player_x <= Locate_x.X2.value:
                self.location_x = Locate_x.X1.value
    
    # プレイヤーの座標を移動させる関数
    def move(self):
        # ステイ状態の場合何もしない
        if self.state == State.STAY:
            return
        # 左移動状態の場合の処理
        elif self.state == State.LEFT:
            # プレイヤーのX座標が左端の場合にステイ状態にして終了
            if self.player_x == Locate_x.X1.value:
                self.state = State.STAY
                return
            # 次の移動先を決める
            self.set_locate()
            # プレイヤーのX座標を移動先に近づける
            self.player_x-= PLAYER_SPEED
            # 移動先の座標とプレイヤーのX座標が同じ場合ステイ状態にする
            if self.player_x == self.location_x:
                self.state = State.STAY
        # 右移動状態の場合の処理
        elif self.state == State.RIGHT:
            # プレイヤーの座標が右端の場合にステイ状態にして終了
            if self.player_x == Locate_x.X5.value:
                self.state = State.STAY
                return
            # 次の移動先を決める
            self.set_locate()
            # プレイヤーのX座標を移動先に近づける
            self.player_x += PLAYER_SPEED
            # 移動先の座標とプレイヤーのX座標が同じ場合ステイ状態にする
            if self.player_x == self.location_x:
                self.state = State.STAY
        # 上移動状態の場合の処理
        elif self.state == State.UP:
            # プレイヤーのY座標を上方向に移動させる
            self.player_y -= PLAYER_SPEED
            # プレイヤーのY座標が一番上になった場合に下移動状態にする
            if self.player_y == Locate_y.Y2.value:
                self.state = State.DOWN
        # 下移動状態の場合の処理
        elif self.state == State.DOWN:
            # プレイヤーのY座標を下方向に移動させる
            self.player_y += PLAYER_SPEED
            # プレイヤーのY座標が一番下になった場合にステイ状態にする
            if self.player_y == Locate_y.Y1.value:
                self.state = State.STAY
        
    # 入力を検知し、それに応じた処理を行う関数
    def update(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

            # ステイ状態の場合にのみ入力を検知する
            if self.state == State.STAY:
                # 入力がキーボードの場合の処理
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a and self.left_timer == 0:
                        self.left_timer = INPUT_WAIT_FRAME
                    if event.key == pygame.K_d and self.right_timer == 0:
                        self.right_timer = INPUT_WAIT_FRAME
                # 入力がタッチの場合の処理
                elif event.type == pygame.FINGERDOWN:
                    # タッチの座標が0～1で取得するためスクリーンの横幅を掛ける
                    x = event.x * SCREEN_WIDTH
                    # 画面の左側のタッチを検出
                    if x < SCREEN_WIDTH // 2 and self.left_timer == 0:
                        self.left_timer = INPUT_WAIT_FRAME
                    # 画面の右側のタッチを検出
                    elif x > SCREEN_WIDTH // 2 and self.right_timer == 0:
                        self.right_timer = INPUT_WAIT_FRAME

        # 右入力と左入力が押された場合上移動状態になる
        if self.left_timer > 0 and self.right_timer > 0:
            self.state = State.UP
            self.left_timer = 0
            self.right_timer = 0

        if self.left_timer > 0:
            self.left_timer -= 1
            if self.left_timer == 0:
                self.state = State.LEFT
        
        if self.right_timer > 0:
            self.right_timer -= 1
            if self.right_timer == 0:
                self.state = State.RIGHT

        self.move()

        

    def draw(self):
        self.screen.fill(BACK_COLOR)

        # プレイヤーを描画
        pygame.draw.rect(
            self.screen,
            PLAYER_COLOR,
            ((self.player_x - (PLAYER_WIDTH//2)), self.player_y, PLAYER_WIDTH, PLAYER_HEIGHT),
        )

        pygame.display.flip()

    def run(self):
        while self.running:
            events = pygame.event.get()
            self.update(events)
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()


App()
