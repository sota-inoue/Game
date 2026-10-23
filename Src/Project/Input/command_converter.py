
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

        # 上半分の入力
        if touch_y < self.touch_height // 2:
            if touch_x < self.touch_width // 2:
                return Command.ATTACK
            return Command.PAUSE

        # 下半分の入力
        if touch_x < self.touch_width // 3:
            return Command.LEFT

        if touch_x < self.touch_width * 2 // 3:
            return Command.JUMP

        return Command.RIGHT
