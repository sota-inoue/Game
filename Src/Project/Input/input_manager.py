
from collections import deque

from Input.device_input import find_device, DeviceInput
from Input.pygame_input import PygameInput
from Input.coord_converter import driver_to_game, pygame_to_game
from Input.command_converter import CommandConverter, Command


class Input:
    def __init__(self, mode: bool):
        # True : Raspberry Pi
        # False: PC
        self.mode = mode

        if self.mode:
            self.touch = find_device()
            self._input = DeviceInput(self.touch)
        else:
            self._input = PygameInput()

        self.command_converter = CommandConverter()

        # 未処理コマンドを保存する
        self._commands = deque()

        self._input_x = -1
        self._input_y = -1

    def get_is_click(self) -> bool:
        return bool(self._commands)

    def get_command(self) -> Command:
        # 保存されたコマンドを順番に取得する
        if self._commands:
            return self._commands.popleft()

        return Command.NONE

    def command_update(self) -> None:
        self._input.update()

        while self._input.has_input():
            x, y = self._input.get_input()

            if self.mode:
                x, y = driver_to_game(x, y)
            else:
                x, y = pygame_to_game(x, y)

            self._input_x = x
            self._input_y = y

            # 新しい入力が来たら、古い未処理コマンドを破棄
            self._commands.clear()

            if x < 0 or y < 0:
                continue

            command = self.command_converter.convert(x, y)

            if command != Command.NONE:
                self._commands.append(command)

    def debug_log(self) -> None:
        command = (
            self._commands[0].name
            if self._commands else Command.NONE.name
        )

        print(
            f": input = ({self._input_x}, {self._input_y}) "
            f": click = {self.get_is_click()} "
            f": saved = {command} "
            f": queue = {len(self._commands)}"
        )
