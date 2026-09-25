class LaneGeometry:
    def __init__(self, width: int, height: int):

        # 画面中央のX座標
        self._center_x = width // 2

        # 一番手前のレーン
        self._bottom_lane_width = width * 9 // 10
        self._bottom_lane_left_x = (width - self._bottom_lane_width) // 2
        self._bottom_lane_y = height * 14 // 15

        # 一番奥のレーン
        self._top_lane_width = width * 2 // 10
        self._top_lane_left_x = (width - self._top_lane_width) // 2
        self._top_lane_y = height * 4 // 15

        # 一番手前から一番奥までのY方向の距離
        lane_y_range = self._bottom_lane_y - self._top_lane_y

        # 各主要レーン間の間隔比率
        # 手前ほど広く、奥ほど狭くする
        lane_gap_rates = [12, 10, 8, 6, 4, 2]

        # 一番手前を基準とした各主要レーンまでの累積値
        cumulative_rates = [
            lane_gap_rates[0],
            lane_gap_rates[0] + lane_gap_rates[1],
            lane_gap_rates[0] + lane_gap_rates[1] + lane_gap_rates[2],
            lane_gap_rates[0] + lane_gap_rates[1] + lane_gap_rates[2] + lane_gap_rates[3],
            lane_gap_rates[0] + lane_gap_rates[1] + lane_gap_rates[2] + lane_gap_rates[3] + lane_gap_rates[4],
            lane_gap_rates[0] + lane_gap_rates[1] + lane_gap_rates[2] + lane_gap_rates[3] + lane_gap_rates[4] + lane_gap_rates[5]
        ]

        # 一番手前と一番奥を除いた主要レーンのY座標
        inner_lane_y = [
            self._bottom_lane_y - lane_y_range * cumulative_rates[0] // cumulative_rates[5],
            self._bottom_lane_y - lane_y_range * cumulative_rates[1] // cumulative_rates[5],
            self._bottom_lane_y - lane_y_range * cumulative_rates[2] // cumulative_rates[5],
            self._bottom_lane_y - lane_y_range * cumulative_rates[3] // cumulative_rates[5],
            self._bottom_lane_y - lane_y_range * cumulative_rates[4] // cumulative_rates[5]
        ]

        # 各主要レーンの中間に配置するレーンのY座標
        middle_lane_y = [
            self._bottom_lane_y - lane_y_range * (lane_gap_rates[0] // 2) // cumulative_rates[5],
            self._bottom_lane_y - lane_y_range * (cumulative_rates[0] + lane_gap_rates[1] // 2) // cumulative_rates[5],
            self._bottom_lane_y - lane_y_range * (cumulative_rates[1] + lane_gap_rates[2] // 2) // cumulative_rates[5],
            self._bottom_lane_y - lane_y_range * (cumulative_rates[2] + lane_gap_rates[3] // 2) // cumulative_rates[5],
            self._bottom_lane_y - lane_y_range * (cumulative_rates[3] + lane_gap_rates[4] // 2) // cumulative_rates[5],
            self._bottom_lane_y - lane_y_range * (cumulative_rates[4] + lane_gap_rates[5] // 2) // cumulative_rates[5]
        ]

        # 手前から奥までの全13レーンのY座標
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

        # 各レーンの幅
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

        # 各レーンの左端X座標
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
            self._top_lane_left_x
        ]


    def _get_lane_width(self, y: int) -> int:

        # 一番手前を0.0、一番奥を1.0とした位置の割合を求める
        rate = (self._bottom_lane_y - y) / (self._bottom_lane_y - self._top_lane_y)

        # Y位置に応じて手前から奥へレーン幅を補間する
        lane_width = int(self._bottom_lane_width + (self._top_lane_width - self._bottom_lane_width) * rate )

        return lane_width


    def get_lane_width(self, index: int) -> int:
        return self._lane_width[index]


    def get_lane_x(self, index: int) -> int:
        return self._lane_x[index]


    def get_lane_y(self, index: int) -> int:
        return self._lane_y[index]

