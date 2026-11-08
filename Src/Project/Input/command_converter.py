
from enum import Enum, auto
from config import TOUCH_WIDTH, TOUCH_HEIGHT


class Command(Enum):
    LEFT = auto()
    JUMP = auto()
    RIGHT = auto()
    ATTACK = auto()
    PAUSE = auto()
    NONE = auto()


class CommandConverter:
    def __init__(self):
        self.touch_width = TOUCH_WIDTH
        self.touch_height = TOUCH_HEIGHT

    def convert(self, touch_x: int, touch_y: int) -> Command:
        # タッチ画面外の入力を除外する
        if not (
            0 <= touch_x < self.touch_width
            and 0 <= touch_y < self.touch_height
        ):
            return Command.NONE

        # タッチ座標を割合に変換する
        x = touch_x / self.touch_width
        y = touch_y / self.touch_height

        # ATTACK
        if 0.12 <= x <= 0.32 and 0.07 <= y <= 0.38:
            return Command.ATTACK

        # PAUSE
        if 0.69 <= x <= 0.89 and 0.07 <= y <= 0.38:
            return Command.PAUSE

        # LEFT
        if 0.00 <= x <= 0.24 and 0.40 <= y <= 0.72:
            return Command.LEFT

        # RIGHT
        if 0.78 <= x <= 1.00 and 0.40 <= y <= 0.72:
            return Command.RIGHT

        # JUMP（円形判定）
        center_x = 0.50
        center_y = 0.56

        radius_x = 0.23
        radius_y = 0.36

        dx = (x - center_x) / radius_x
        dy = (y - center_y) / radius_y

        if dx * dx + dy * dy <= 1:
            return Command.JUMP

        return Command.NONE