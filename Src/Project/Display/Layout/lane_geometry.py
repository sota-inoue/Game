class LaneGeometry:
    def __init__(self, width: int, height: int):

        # 画面中央のX座標
        self._center_x = width // 2

        # 一番手前のレーン
        self._bottom_lane_width = width * 9 // 10
        self._bottom_lane_left_x = (width - self._bottom_lane_width) // 2
        self._bottom_lane_y = height * 14 // 15

        # 一番奥のレーン
        self._top_lane_width = width * 4 // 10
        self._top_lane_left_x = (width - self._top_lane_width) // 2
        self._top_lane_y = height * 4 // 15

        # 一番手前から一番奥までのY方向の距離
        lane_y_range = self._bottom_lane_y - self._top_lane_y

        # 各主要レーン間の間隔比率、奥に進むほど間隔を狭くする
        lane_gap_rates = [12, 10, 8, 6, 4, 2]

        # 一番手前のレーンを基準とした、各主要レーンまでの間隔比率の累積値
        cumulative_rates = [
            lane_gap_rates[0],
            lane_gap_rates[0] + lane_gap_rates[1],
            lane_gap_rates[0] + lane_gap_rates[1] + lane_gap_rates[2],
            lane_gap_rates[0] + lane_gap_rates[1] + lane_gap_rates[2] + lane_gap_rates[3],
            lane_gap_rates[0] + lane_gap_rates[1] + lane_gap_rates[2] + lane_gap_rates[3] + lane_gap_rates[4],
            lane_gap_rates[0] + lane_gap_rates[1] + lane_gap_rates[2] + lane_gap_rates[3] + lane_gap_rates[4] + lane_gap_rates[5],
        ]

        # 一番手前と一番奥を除いた5本の主要レーンのY座標
        inner_lane_y = [
            self._bottom_lane_y - lane_y_range * cumulative_rates[0] // cumulative_rates[5],
            self._bottom_lane_y - lane_y_range * cumulative_rates[1] // cumulative_rates[5],
            self._bottom_lane_y - lane_y_range * cumulative_rates[2] // cumulative_rates[5],
            self._bottom_lane_y - lane_y_range * cumulative_rates[3] // cumulative_rates[5],
            self._bottom_lane_y - lane_y_range * cumulative_rates[4] // cumulative_rates[5]
        ]

        # 各主要レーンの中間に配置するレーンのY座標
        # 敵の移動を滑らかに見せるために使用する
        middle_lane_y = [
            self._bottom_lane_y - lane_y_range * (lane_gap_rates[0] // 2) // cumulative_rates[5],
            self._bottom_lane_y - lane_y_range * (cumulative_rates[0] + lane_gap_rates[1] // 2) // cumulative_rates[5],
            self._bottom_lane_y - lane_y_range * (cumulative_rates[1] + lane_gap_rates[2] // 2) // cumulative_rates[5],
            self._bottom_lane_y - lane_y_range * (cumulative_rates[2] + lane_gap_rates[3] // 2) // cumulative_rates[5],
            self._bottom_lane_y - lane_y_range * (cumulative_rates[3] + lane_gap_rates[4] // 2) // cumulative_rates[5],
            self._bottom_lane_y - lane_y_range * (cumulative_rates[4] + lane_gap_rates[5] // 2) // cumulative_rates[5]
        ]

        # 手前から奥までの全13レーンのY座標、主要レーンと中間レーンを交互に配置する
        self._lane_y = [
            self._bottom_lane_y,
            middle_lane_y[0],
            inner_lane_y[0],
            middle_lane_y[1],
            inner_lane_y[1],
            middle_lane_y[2],
            inner_lane_y[2],
            middle_lane_y[3],
            inner_lane_y[3],
            middle_lane_y[4],
            inner_lane_y[4],
            middle_lane_y[5],
            self._top_lane_y
        ]

        # 各レーンのY座標を基準に、左右の境界線に沿ったレーン幅を求める
        self._lane_width = [
            self._bottom_lane_width,
            self._get_lane_width(self._lane_y[1]),
            self._get_lane_width(self._lane_y[2]),
            self._get_lane_width(self._lane_y[3]),
            self._get_lane_width(self._lane_y[4]),
            self._get_lane_width(self._lane_y[5]),
            self._get_lane_width(self._lane_y[6]),
            self._get_lane_width(self._lane_y[7]),
            self._get_lane_width(self._lane_y[8]),
            self._get_lane_width(self._lane_y[9]),
            self._get_lane_width(self._lane_y[10]),
            self._get_lane_width(self._lane_y[11]),
            self._top_lane_width
        ]

        # 手前から奥までの全13レーンのX座標
        self._lane_x = [
            self._bottom_lane_left_x,
            (width - self._lane_width[1]) // 2,
            (width - self._lane_width[2]) // 2,
            (width - self._lane_width[3]) // 2,
            (width - self._lane_width[4]) // 2,
            (width - self._lane_width[5]) // 2,
            (width - self._lane_width[6]) // 2,
            (width - self._lane_width[7]) // 2,
            (width - self._lane_width[8]) // 2,
            (width - self._lane_width[9]) // 2,
            (width - self._lane_width[10]) // 2,
            (width - self._lane_width[11]) // 2,
            (width - self._lane_width[12]) // 2,
        ]

    def _get_lane_width(self, y: int) -> int:
        # 指定したY座標が、一番手前から一番奥までのどの位置にあるかを0.0〜1.0の割合で求める
        rate = (self._bottom_lane_y - y) / (self._bottom_lane_y - self._top_lane_y)

        # 手前と奥の左端座標を基準に、指定したY座標での左端X座標を直線補間で求める
        left_x = self._bottom_lane_left_x + (self._top_lane_left_x - self._bottom_lane_left_x) * rate

        # 画面中央から左端までの距離をレーン幅の半分として求める
        half_width = self._center_x - left_x

        # レーンは左右対称のため、半分の幅を2倍してレーン全体の横幅を求める
        lane_width = int(half_width * 2)

        return lane_width

    def get_lane_width(self, index: int):
        return self._lane_width[index],

    def get_lane_x(self, index: int):
        return  self._lane_x[index]

    def get_lane_y(self, index: int):
        return self._lane_y[index]

