import pygame

from System.player_system import Player
from System.map_system import Map
from System.progress_system import progress_system


class System:
    def __init__(self,DISPLAY_WIDTH, DISPLAY_HEIGHT):
        self.player_system = Player(DISPLAY_WIDTH, DISPLAY_HEIGHT)
        self.map = Map()

    
    def player_update(self, x, y):
        return self.player_system.update(x, y)

    def map_update(self, datas, count):
        return self.map.map_update(datas, count)

    def progress_update(self, state, x, y, count):
        return progress_system(state, x, y, count)
