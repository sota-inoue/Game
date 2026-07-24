import pygame

from System.player_system import Player
from System.map_updata import map_updata
from System.progress_system import progress_system


class SystemManager:
    def __init__(self,DISPLAY_WIDTH, DISPLAY_HEIGHT):
        # pygameの初期化
        pygame.init()

        # プレイヤーの状態を管理するオブジェクトを生成
        self.player_system = Player(DISPLAY_WIDTH, DISPLAY_HEIGHT)

    def player_update(self, x, y):
        # プレイヤーの状態を更新し、次の座標を取得する
        player_x, player_y = self.player_system.update(x, y)
        return player_x, player_y

    def map_update(self, map_datas, map_data):
        # マップの状態を更新する
        updated_map_data = map_updata(map_datas, map_data)
        return updated_map_data

    def progress_update(self, state, input_x, input_y, count):
        # ゲームの進行を管理する
        new_state = progress_system.progress_system(state, input_x, input_y, count)
        return new_state
