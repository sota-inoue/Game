class PlayerLayout:
    def __init__(self, width: int, x: int, y: int):

        # 各マスの中心X座標
        grid_x = [
            x + width // 6,
            x + width * 2 // 6,
            x + width * 3 // 6,
            x + width * 4 // 6,
            x + width * 5 // 6,
        ]

        # プレイヤーの縦横比は 横:縦 = 3:5
        self._player_width = width // 8
        self._player_height = self._player_width * 5 // 3

        # 各マスにいるときのプレイヤーの左上X座標
        position_x = [
            grid_x[0] - (self._player_width // 2),
            grid_x[1] - (self._player_width // 2),
            grid_x[2] - (self._player_width // 2),
            grid_x[3] - (self._player_width // 2),
            grid_x[4] - (self._player_width // 2)
        ]

        # 隣のマスまでの距離を4分割した値を、
        # 1フレームごとのX方向の移動量とする
        player_speed_x = ( position_x[1] - position_x[0] ) // 4

        # 左端から右端までのプレイヤーの描画X座標
        self.player_x = [
            position_x[0],                                                    # 0
            position_x[0] + player_speed_x,                                  # 1
            position_x[0] + player_speed_x * 2,                              # 2
            position_x[0] + player_speed_x * 3,                              # 3

            position_x[1],                                                    # 4
            position_x[1] + player_speed_x,                                  # 5
            position_x[1] + player_speed_x * 2,                              # 6
            position_x[1] + player_speed_x * 3,                              # 7

            position_x[2],                                                    # 8
            position_x[2] + player_speed_x,                                  # 9
            position_x[2] + player_speed_x * 2,                              # 10
            position_x[2] + player_speed_x * 3,                              # 11

            position_x[3],                                                    # 12
            position_x[3] + player_speed_x,                                  # 13
            position_x[3] + player_speed_x * 2,                              # 14
            position_x[3] + player_speed_x * 3,                              # 15

            position_x[4]                                                     # 16
        ]

        # 通常時とジャンプ最高点の左上Y座標
        position_y = [ y - self._player_height, y - self._player_height * 2 ]

        # 通常位置からジャンプ最高点までを8分割する
        player_speed_y = ( position_y[1] - position_y[0] ) // 8

        # ジャンプ上昇時のY座標
        self.player_y = [
            position_y[0],
            position_y[0] + player_speed_y,
            position_y[0] + player_speed_y * 2,
            position_y[0] + player_speed_y * 3,
            position_y[0] + player_speed_y * 4,
            position_y[0] + player_speed_y * 5,
            position_y[0] + player_speed_y * 6,
            position_y[0] + player_speed_y * 7,
            position_y[1]
        ]

    def get_player_layout(self, x_index: int, y_index: int):
        # プレイヤーの左上座標と描画サイズを返す
        return {
            "x": self.player_x[x_index],
            "y": self.player_y[y_index],
            "width": self._player_width,
            "height": self._player_height
        }