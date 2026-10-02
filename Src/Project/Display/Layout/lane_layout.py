class LaneLayout:
    def __init__(self, width: int, x: int, y: int):
        self._width = width
        # このレーンにあるマス共通のY座標
        self._grid_y = y

        self._grid_x = [
            x + self._width // 6,      # 左端のx座標
            x + self._width * 2 // 6,  # 左から2番目のx座標
            x + self._width * 3 // 6,  # 中央のx座標
            x + self._width * 4 // 6,  # 左から4番目のx座標
            x + self._width * 5 // 6,  # 右端のx座標
        ]

        # 敵の縦幅と横幅の比率は 5:3
        self._enemy_width = self._width // 8
        self._enemy_height = self._enemy_width * 5 // 3

        # 敵の描画処理用の座標
        self._enemy_x = [
            self._grid_x[0] - (self._enemy_width // 2),
            self._grid_x[1] - (self._enemy_width // 2),
            self._grid_x[2] - (self._enemy_width // 2),
            self._grid_x[3] - (self._enemy_width // 2),
            self._grid_x[4] - (self._enemy_width // 2)
        ]
        self._enemy_y = y - self._enemy_height

        # 障害物の横幅と縦幅の比率は 1:1
        self._obstacle_width = self._enemy_width
        self._obstacle_height = self._obstacle_width

        # 障害物の描画処理用の座標
        self._obstacle_x = [
            self._grid_x[0] - (self._obstacle_width // 2),
            self._grid_x[1] - (self._obstacle_width // 2),
            self._grid_x[2] - (self._obstacle_width // 2),
            self._grid_x[3] - (self._obstacle_width // 2),
            self._grid_x[4] - (self._obstacle_width // 2)
        ]
        self._obstacle_y = y - self._obstacle_height


        # 攻撃物の横幅と縦幅の比率は 1:1
        self._attack_width = self._enemy_width // 2
        self._attack_height = self._attack_width

        # 攻撃物の中心が敵の中心に重なるように左上座標を求める
        self._attack_x = [
            self._grid_x[0] - (self._attack_width // 2),
            self._grid_x[1] - (self._attack_width // 2),
            self._grid_x[2] - (self._attack_width // 2),
            self._grid_x[3] - (self._attack_width // 2),
            self._grid_x[4] - (self._attack_width // 2)
        ]

        self._attack_y = y - ( (self._enemy_height // 2) + (self._attack_height // 2) )

    def get_enemy_layout(self, cell_index: int, width_in_cells: int = 1):
        # 指定された横マス番号と占有マス数に応じた敵の左上描画座標とサイズを返す
        if width_in_cells == 1:
            # 1マス敵は従来通りのサイズと前計算座標を使用
            return {
                "x": self._enemy_x[cell_index],
                "y": self._enemy_y,
                "width": self._enemy_width,
                "height": self._enemy_height
            }
        # 多マス敵のサイズ算出
        enemy_width = (self._width // 6) * width_in_cells
        enemy_height = enemy_width // 2  # 横長敵用の高さ比率 (2:1)

        # 占有領域の中心 X 座標を計算
        start_x = self._grid_x[cell_index]
        end_cell_idx = min(cell_index + width_in_cells - 1, 4)
        end_x = self._grid_x[end_cell_idx]
        center_x = (start_x + end_x) // 2

        # 左上描画座標の決定
        top_left_x = center_x - (enemy_width // 2)
        top_left_y = self._grid_y - enemy_height
        return {
            "x": top_left_x,
            "y": top_left_y,
            "width": enemy_width,
            "height": enemy_height
        }


    def get_obstacle_layout(self, x: int):
        # 指定された横マス番号に配置する障害物の左上座標と描画サイズを返す
        return {
            "x": self._obstacle_x[x],
            "y": self._obstacle_y,
            "width": self._obstacle_width,
            "height": self._obstacle_height
        }


    def get_attack_layout(self, x: int):
        # 指定された横マス番号に配置する攻撃物の左上座標と描画サイズを返す
        return {
            "x": self._attack_x[x],
            "y": self._attack_y,
            "width": self._attack_width,
            "height": self._attack_height
        }