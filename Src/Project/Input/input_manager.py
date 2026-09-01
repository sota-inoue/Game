from Input.device_input import find_device, device_input
from Input.pygame_input import pygame_input
from Input.coord_converter import driver_to_game, pygame_to_game
from Input.command_converter import CommandConverter
from Domain.state import Command

class Input:
    def __init__(self, mode):
        # True : Raspberry Pi（フレームバッファ描画）
        # False: PC（pygameウィンドウ描画）
        self.mode = mode

        if self.mode:
            self.touch = find_device()

        self.command_converter = CommandConverter()

        self._is_click: bool = False
        self._saved_command: Command = Command.STAY

        self._input_x: int = -1
        self._input_y: int = -1

    def get_is_click(self) -> bool:
        return self._is_click

    def get_command(self) -> Command:
        command = self._saved_command

        self._saved_command = Command.STAY
        self._is_click = False

        return command

    def command_update(self) -> None:

        # 入力座標を取得する
        if self.mode:
            x, y = device_input(self.touch)
            self._input_x, self._input_y = driver_to_game(x, y)
        else:
            x, y = pygame_input()
            self._input_x, self._input_y = pygame_to_game(x, y)

        # 入力がなければ終了
        if self._input_x == -1 or self._input_y == -1:
            return

        # 変換後の座標からコマンドを取得
        command = self.command_converter.convert(self._input_x, self._input_y)

        # 有効なコマンドでなければ終了
        if command == Command.STAY:
            return

        self._is_click = True
        self._saved_command = command

    def debug_log(self, count: int) -> None:
        print(
            f"count = {count:03d} "
            f": input = ({self._input_x}, {self._input_y}) "
            f": click = {self._is_click} "
            f": saved = {self._saved_command.name}"
        )