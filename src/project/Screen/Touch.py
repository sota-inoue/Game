import pygame
from enum import Enum

class TouchScene(Enum):
    START = 0
    CONTROLLER = 1
    CONTINUE = 2

class TouchDisplay:
    BACK_COLOR = (90, 90, 90)
    LINE_COLOR = (255, 255, 255)
    TEXT_COLOR = (0, 0, 0)
    LINE_WIDTH = 2
    WIDTH = 480
    HEIGHT = 320

    def __init__(self):
        self.surface = pygame.Surface((self.WIDTH, self.HEIGHT), depth=16)
        self.font = pygame.font.Font(None, 50)
        self.state = TouchScene.START

    # 外部からゲーム画面の状態を変更する機能
    def set_state(self, state):
        self.state = state

    def DrawText(self, text, x, y):
        # 指定した文字列を作成
        text_surface = self.font.render(text, True, self.TEXT_COLOR)
        # 描画する文字列の幅と高さを取得
        text_width = text_surface.get_width()
        text_height = text_surface.get_height()
        # 指定された座標を文字列の中心として描画
        self.surface.blit( text_surface, (x - text_width // 2, y - text_height // 2) )

    def draw(self):
        # BACK_COLORでsurfaceを塗りつぶす
        self.surface.fill(self.BACK_COLOR)

        # 現在のstateに応じたスクリーンを描画を行う
        if self.state == TouchScene.START:
            self.draw_Start()
        elif self.state == TouchScene.CONTROLLER:
            self.draw_Controller()
        elif self.state == TouchScene.CONTINUE:
            self.draw_Continue()


    def draw_Start(self):
        # 画面の中心にStartの文字列を描画
        self.DrawText("Start", self.WIDTH//2, self.HEIGHT//2)

    def draw_Controller(self):
        #文字の描画
        self.DrawText("L", self.WIDTH//6, self.HEIGHT//2)
        self.DrawText("J", self.WIDTH*3//6, self.HEIGHT//2)
        self.DrawText("R", self.WIDTH*5//6, self.HEIGHT//2)
        # 線の描画
        pygame.draw.line(self.surface, self.LINE_COLOR, (self.WIDTH//3, 0), (self.WIDTH//3, self.HEIGHT), self.LINE_WIDTH)
        pygame.draw.line(self.surface, self.LINE_COLOR, (self.WIDTH*2//3, 0), (self.WIDTH*2//3, self.HEIGHT), self.LINE_WIDTH)

    def draw_Continue(self):
        # 画面の中心にContinueの文字列を描画
        self.DrawText("Continue", self.WIDTH//2, self.HEIGHT//2)

