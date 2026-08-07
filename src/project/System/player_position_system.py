from Domain.state import Command

class PositionSystem:

    def __init__(self):
        self.is_jumping = False
        self.jump_count = 0
        self.jump_pattern = (0, 1, 1, 0)

    def update(self, command, position_x, position_y):
        x = position_x
        y = position_y

        if command == Command.LEFT:
            x -= 1

        elif command == Command.RIGHT:
            x += 1

        elif command == Command.JUMP and not self.is_jumping:
            self.is_jumping = True
            self.jump_count = 0

        if self.is_jumping:
            y = self.jump_pattern[self.jump_count]
            self.jump_count += 1

            if self.jump_count >= len(self.jump_pattern):
                self.is_jumping = False
                self.jump_count = 0
        else:
            y = 0

        x = max(0, min(4, x))

        return x, y