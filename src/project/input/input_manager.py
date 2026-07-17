from input.device_input import find_device, device_input
from input.pygame_input import pygame_input
from input.coord_converter import driver_to_game, pygame_to_game

class Input:
    def __init__(self, mode):
        # True : Raspberry Pi（フレームバッファ描画）
        # False: PC（pygameウィンドウ描画）
        self.mode = mode
        # Raspberry Piモードで使用するインスタンスを生成
        if self.mode:
            self.touch = find_device() 
    
    def get_input(self):
        if self.mode:
            x, y = device_input(self.touch)
            x, y = driver_to_game(x, y)
        else:
            x, y = pygame_input()
            x, y = pygame_to_game(x, y)
        return x, y