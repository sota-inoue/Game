
class CoordinateManager:
    def __init__(self, width, height):

        # 各レーンの横幅
        # 手前のレーンほど大きく、奥のレーンほど小さくする
        self.lane_width = [
            width * 10 // 10,
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
            (width - self.lane_width[0]) // 2,
            (width - self.lane_width[1]) // 2,
            (width - self.lane_width[2]) // 2,
            (width - self.lane_width[3]) // 2,
            (width - self.lane_width[4]) // 2,
            (width - self.lane_width[5]) // 2,
            (width - self.lane_width[6]) // 2,
        ]

        # 各レーンのY座標の比率
        # heightで割って比率にすることで、
        # 画面の縦幅が変わっても相対的な位置を保てるようにする
        #
        # width // 10:
        #   敵やプレイヤーの基準サイズとして使う
        #
        # width // 20:
        #   一番手前のレーン下側に少し余白を作るために使う
        #
        # width * 3 // 20:
        #   奥側のレーン全体を少し上に配置するための基準値
        #
        # height * n // 50:
        #   レーンごとの縦方向の間隔を作るための値
        lane_y_rate = [
            ((height - width // 10) - width // 20) / height,
            ((height - width * 3 // 20) - (height * 7 // 50)) / height,
            ((height - width * 3 // 20) - (height * 6 // 50)) / height,
            ((height - width * 3 // 20) - (height * 5 // 50)) / height,
            ((height - width * 3 // 20) - (height * 4 // 50)) / height,
            ((height - width * 3 // 20) - (height * 3 // 50)) / height,
            ((height - width * 3 // 20) - (height * 2 // 50)) / height,
        ]

        # 各レーンの座標情報を作成して配列に保存
        # LaneCoordinateには、
        # レーン幅・レーンの左上X座標・レーンのY座標を渡す
        self.lanes = [
            LaneCoordinate(self.lane_width[0], self.lane_x[0], lane_y_rate[0] * height),  # Lane1
            LaneCoordinate(self.lane_width[1], self.lane_x[1], lane_y_rate[1] * height),  # Lane2
            LaneCoordinate(self.lane_width[2], self.lane_x[2], lane_y_rate[2] * height),  # Lane3
            LaneCoordinate(self.lane_width[3], self.lane_x[3], lane_y_rate[3] * height),  # Lane4
            LaneCoordinate(self.lane_width[4], self.lane_x[4], lane_y_rate[4] * height),  # Lane5
            LaneCoordinate(self.lane_width[5], self.lane_x[5], lane_y_rate[5] * height),  # Lane6
            LaneCoordinate(self.lane_width[6], self.lane_x[6], lane_y_rate[6] * height),  # Lane7
        ]

    def get_Coordinate(self, x, y):
        # 指定されたマスの座標を返す
        #
        # x:
        #   横方向のマス番号
        #   1〜5で指定する
        #
        # y:
        #   奥行き方向のレーン番号
        #   1〜7で指定する
        #
        # self.lanesの並びは、
        #   self.lanes[0] = Lane1 一番手前
        #   self.lanes[6] = Lane7 一番奥
        #
        # ゲーム上のyは、
        #   y = 1 が一番手前
        #   y = 7 が一番奥
        #
        # そのため、yの値とself.lanesのindexを逆順に対応させる
        if y == 1:
            return self.lanes[0].get_Coordinate(x)
        elif y == 2:
            return self.lanes[1].get_Coordinate(x)
        elif y == 3:
            return self.lanes[2].get_Coordinate(x)
        elif y == 4:
            return self.lanes[3].get_Coordinate(x)
        elif y == 5:
            return self.lanes[4].get_Coordinate(x)
        elif y == 6:
            return self.lanes[5].get_Coordinate(x)
        elif y == 7:
            return self.lanes[6].get_Coordinate(x)



class LaneCoordinate:
    def __init__(self, width, x, y):
        # このレーンにあるマス共通のY座標
        self.cell_y = y

        # このレーンにある5マス分のX座標
        #
        # レーンの左端を基準に、
        # レーン幅を6等分した位置へマスを配置する
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

    def get_Coordinate(self, x):
        # 指定された横マス番号の座標を返す
        #
        # x:
        #   1〜5で指定する
        #
        # 戻り値:
        #   (X座標, Y座標)
        return self.cell_x[x - 1], self.cell_y