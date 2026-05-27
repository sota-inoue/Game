import pyxel
import math

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120
class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps=30)
        pyxel.mouse(True)
        pyxel.load("my_resource.pyxres")

        self.player_x = SCREEN_WIDTH*4//5
        self.player_y = SCREEN_HEIGHT//2
        self.target_x = self.player_x
        self.target_y = self.player_y
        self.speed = 2

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        # 左クリックを長押ししている間
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            self.target_x = pyxel.mouse_x
            self.target_y = pyxel.mouse_y

        # プレイヤーを目標座標に少しずつ近づける
        dx = self.target_x - self.player_x
        dy = self.target_y - self.player_y
        distance = math.sqrt(dx * dx + dy * dy)

        if distance > self.speed:
            self.player_x += dx / distance * self.speed
            self.player_y += dy / distance * self.speed
        else:
            self.player_x = self.target_x
            self.player_y = self.target_y

    def draw(self):
        pyxel.cls(pyxel.COLOR_GRAY)
        # 目標地点
        pyxel.circ(self.target_x, self.target_y, 2, 8)
        pyxel.blt(self.player_x ,self.player_y, 0, 0, 0, 16, 16, pyxel.COLOR_BLACK)

App()