from Domain.state import Command
from Domain.config import TOUCH_WIDTH,TOUCH_HEIGHT

class CommandConverter:
    def __init__(self):
        self.touch_width = TOUCH_WIDTH
        self.touch_height = TOUCH_HEIGHT

    def convert(self, touch_x, touch_y):
        if 0 <= touch_y < self.touch_height // 2:
            if 0 <= touch_x < self.touch_width // 2:
                return Command.ATTACK
            elif self.touch_width // 2 <= touch_x <= self.touch_width:
                return Command.POSE

        elif self.touch_height // 2 <= touch_y <= self.touch_height:
            if 0 <= touch_x < self.touch_width // 3:
                return Command.LEFT
            elif self.touch_width // 3 <= touch_x < self.touch_width * 2 // 3:
                return Command.JUMP
            elif self.touch_width * 2 // 3 <= touch_x <= self.touch_width:
                return Command.RIGHT

        return Command.STAY