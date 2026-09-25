class LaneLayout:
    def __init__(self, width: int, x: int, y: int):
        # このレーンにあるマス共通のY座標
        self._grid_y = y

        grid_x = [
            x + width // 6,      # 左端のx座標
            x + width * 2 // 6,  # 左から2番目のx座標
            x + width * 3 // 6,  # 中央のx座標
            x + width * 4 // 6,  # 左から4番目のx座標
            x + width * 5 // 6,  # 右端のx座標
        ]

        # 敵の縦幅と横幅の比率は 5:3
        self._enemy_width = width // 8
        self._enemy_height = self._enemy_width * 5 // 3

        # 敵の描画処理用の座標
        self._enemy_x = [
            grid_x[0] - (self._enemy_width // 2),
            grid_x[1] - (self._enemy_width // 2),
            grid_x[2] - (self._enemy_width // 2),
            grid_x[3] - (self._enemy_width // 2),
            grid_x[4] - (self._enemy_width // 2)
        ]
        self._enemy_y = y - self._enemy_height

        # 障害物の横幅と縦幅の比率は 1:1
        self._obstacle_width = self._enemy_width
        self._obstacle_height = self._obstacle_width

        # 障害物の描画処理用の座標
        self._obstacle_x = [
            grid_x[0] - (self._obstacle_width // 2),
            grid_x[1] - (self._obstacle_width // 2),
            grid_x[2] - (self._obstacle_width // 2),
            grid_x[3] - (self._obstacle_width // 2),
            grid_x[4] - (self._obstacle_width // 2)
        ]
        self._obstacle_y = y - self._obstacle_height


        # 攻撃物の横幅と縦幅の比率は 1:1
        self._attack_width = self._enemy_width // 2
        self._attack_height = self._attack_width

        # 攻撃物の中心が敵の中心に重なるように左上座標を求める
        self._attack_x = [
            grid_x[0] - (self._attack_width // 2),
            grid_x[1] - (self._attack_width // 2),
            grid_x[2] - (self._attack_width // 2),
            grid_x[3] - (self._attack_width // 2),
            grid_x[4] - (self._attack_width // 2)
        ]

        self._attack_y = y - ( (self._enemy_height // 2) + (self._attack_height // 2) )

    def get_enemy_layout(self, x: int):
        # 指定された横マス番号に配置する敵の左上座標と描画サイズを返す
        return (
            self._enemy_x[x],
            self._enemy_y,
            self._enemy_width,
            self._enemy_height
        )

    def get_obstacle_layout(self, x: int):
        # 指定された横マス番号に配置する障害物の左上座標と描画サイズを返す
        return (
            self._obstacle_x[x],
            self._obstacle_y,
            self._obstacle_width,
            self._obstacle_height
        )

    def get_attack_layout(self, x: int):
        # 指定された横マス番号に配置する攻撃物の左上座標と描画サイズを返す
        return (
            self._attack_x[x],
            self._attack_y,
            self._attack_width,
            self._attack_height
        )