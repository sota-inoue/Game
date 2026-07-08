class CoordinateManager:
    def __init__(self, width, height):

        # 各レーンの横幅
        # 手前のレーンほど大きく、奥のレーンほど小さくする
        self.lane_width = [
            width,
            width * 9 // 10,
            width * 8 // 10,
            width * 7 // 10,
            width * 6 // 10,
            width * 5 // 10,
            width * 4 // 10,
        ]

        # 各レーンの左上X座標
        # レーンを画面の中央に配置するため、
        # 画面幅とレーン幅の差を2で割る
        self.lane_x = [
            0,
            (width - self.lane_width[1]) // 2,
            (width - self.lane_width[2]) // 2,
            (width - self.lane_width[3]) // 2,
            (width - self.lane_width[4]) // 2,
            (width - self.lane_width[5]) // 2,
            (width - self.lane_width[6]) // 2,
        ]

        # 各レーンのY座標
        #   
        # width // 20: 一番下のレーンの余白
        #
        # width * 3 // 20: 奥側のレーン全体を少し上に配置するための基準値
        #
        # height * n // 50: レーンごとの縦方向の間隔を作るための値
        #
        lane_y = [
            (height - width // 20),
            ((height - width // 20) - (height * 7 // 50)),
            ((height - width // 20) - (height * 13 // 50)),
            ((height - width // 20) - (height * 18 // 50)),
            ((height - width // 20) - (height * 22 // 50)),
            ((height - width // 20) - (height * 25 // 50)),
            ((height - width // 20) - (height * 27 // 50))
        ]

        # 各レーンの座標情報を作成して配列に保存
        # LaneCoordinateに、レーン幅・レーンの左上X座標・レーンのY座標を渡す
        self.lanes = [
            LaneCoordinate(self.lane_width[0], self.lane_x[0], lane_y[0]),  # Lane1
            LaneCoordinate(self.lane_width[1], self.lane_x[1], lane_y[1]),  # Lane2
            LaneCoordinate(self.lane_width[2], self.lane_x[2], lane_y[2]),  # Lane3
            LaneCoordinate(self.lane_width[3], self.lane_x[3], lane_y[3]),  # Lane4
            LaneCoordinate(self.lane_width[4], self.lane_x[4], lane_y[4]),  # Lane5
            LaneCoordinate(self.lane_width[5], self.lane_x[5], lane_y[5]),  # Lane6
            LaneCoordinate(self.lane_width[6], self.lane_x[6], lane_y[6])   # Lane7
        ]

    def get_Coordinate(self, x, y):
        # 指定されたマスの座標を返す
        #
        # x座標 : 0〜4で指定する
        # y座標 : 0〜6で指定する
        #
        # ゲーム上のyは、
        #   y = 0 が一番手前
        #   y = 6 が一番奥
        return self.lanes[y].get_Coordinate(x)

    def get_enemy_size(self, y):
        # 指定されたレーンの敵のサイズを返す
        # y座標 : 0〜6で指定する
        return self.lanes[y].get_enemy_size()

    def get_obstacle_size(self, y):
        # 指定されたレーンの障害物のサイズを返す
        # y座標 : 0〜6で指定する
        return self.lanes[y].get_obstacle_size()


class LaneCoordinate:
    def __init__(self, width, x, y):
        # このレーンにあるマス共通のY座標
        self.cell_y = y

        # このレーンにある5マス分のX座標
        #
        # レーンの左端を基準に、レーン幅を6等分した位置へマスを配置する
        #
        # 5マスを配置するため、以下の位置を使う
        #   1/6, 2/6, 3/6, 4/6, 5/6
        self.cell_x = [
            x + width // 6,      # 左端のx座標
            x + width * 2 // 6,  # 左から2番目のx座標
            x + width * 3 // 6,  # 中央のx座標
            x + width * 4 // 6,  # 左から4番目のx座標
            x + width * 5 // 6,  # 右端のx座標
        ]

        # 敵の横幅と縦幅、比率は3:5
        self.enemy_width = width//10
        self.enemy_height = self.enemy_width * 5 // 3

        # 障害物の横幅と縦幅、比率は1:1
        self.obstacle_width = width//10
        self.obstacle_height = self.obstacle_width

    def get_Coordinate(self, x):
        # 指定された横マス番号の座標を返す
        # x座標 : 0〜4で指定する
        return self.cell_x[x], self.cell_y
    
    def get_enemy_size(self):
        # 敵の横幅と縦幅を返す
        return (self.enemy_width, self.enemy_height)

    def get_obstacle_size(self):
        # 障害物の横幅と縦幅を返す
        return (self.obstacle_width, self.obstacle_height)