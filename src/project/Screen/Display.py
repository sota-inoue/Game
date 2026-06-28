import pygame
from enum import Enum

from Game.player import Player, Command

class GameScene(Enum):
    TITLE = 0
    OP = 1
    STAGE = 2
    OVER = 3
    CLEAR = 4

class GameDisplay:
    BACK_COLOR = (90, 90, 90)
    TEXT_COLOR = (0, 0, 0)

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.Surface((self.width, self.height), depth=16)
        self.font = pygame.font.Font(None, 50)
        self.state = GameScene.TITLE
        self.player = Player(width, height)
        self.player_cmd = Command.STAY

    def DrawText(self, str, x, y):
        # 指定した文字列を作成
        text = self.font.render(str, True, self.TEXT_COLOR)
        # 描画する文字列の幅と高さを取得
        text_width = text.get_width()
        text_height = text.get_height()
        # 指定された座標を文字列の中心として描画
        self.surface.blit(text, (x - text_width // 2, y - text_height // 2))

    # 外部からゲーム画面の状態を変更する機能
    def set_state(self, state):
        self.state = state

    # 外部からプレイヤー操作用コマンドを受け取り保存する機能
    def set_player_cmd(self, command):
        self.player_cmd = command

    def draw(self):
        # BACK_COLORでsurfaceを塗りつぶす
        self.surface.fill(self.BACK_COLOR)

        # 現在のstateに応じたスクリーンを描画を行う
        if self.state == GameScene.TITLE:
            self.draw_Title()
        elif self.state == GameScene.OP:
            self.draw_Opening()
        elif self.state == GameScene.STAGE:
            self.draw_Stage()
        elif self.state == GameScene.OVER:
            self.draw_Over()
        elif self.state == GameScene.CLEAR:
            self.draw_Clear()

    def draw_Title(self):
        # 画面の中心にTitleの文字列を描画
        self.DrawText("Tirle", self.width//2, self.height//2)

    def draw_Opening(self):
        # 画面の中心にOpeningの文字列を描画
        self.DrawText("Opening", self.width//2, self.height//2)

    def draw_Stage(self):
        # 保存されている入力コマンドをもとにプレイヤーを更新し、画面に描画する
        self.player.update(self.player_cmd, self.surface)

    def draw_Over(self):
        # 画面の中心にGame Overの文字列を描画
        self.DrawText("Game Over", self.width//2, self.height//2)

    def draw_Clear(self):
        # 画面の中心にGame Game Clearの文字列を描画
        self.DrawText("Game Clear", self.width//2, self.height//2)