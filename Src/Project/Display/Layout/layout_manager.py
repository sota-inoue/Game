from Display.Layout.lane_geometry import LaneGeometry
from Display.Layout.lane_layout import LaneLayout
from Display.Layout.player_layout import PlayerLayout


class Layout:
    def __init__(self, width: int, height: int):

        lane = LaneGeometry(width, height)

        # 主要レーン
        # 0が一番手前、6が一番奥
        self._lane = [
            LaneLayout(lane.get_lane_width(0), lane.get_lane_x(0), lane.get_lane_y(0)),
            LaneLayout( lane.get_lane_width(2), lane.get_lane_x(2), lane.get_lane_y(2)),
            LaneLayout(lane.get_lane_width(4), lane.get_lane_x(4), lane.get_lane_y(4)),
            LaneLayout(lane.get_lane_width(6), lane.get_lane_x(6), lane.get_lane_y(6)),
            LaneLayout(lane.get_lane_width(8), lane.get_lane_x(8), lane.get_lane_y(8)),
            LaneLayout(lane.get_lane_width(10), lane.get_lane_x(10), lane.get_lane_y(10)),
            LaneLayout(lane.get_lane_width(12), lane.get_lane_x(12), lane.get_lane_y(12))
        ]

        # 主要レーン同士の中間レーン
        self._middle_lane = [
            LaneLayout(lane.get_lane_width(1), lane.get_lane_x(1), lane.get_lane_y(1)),
            LaneLayout(lane.get_lane_width(3), lane.get_lane_x(3), lane.get_lane_y(3)),
            LaneLayout(lane.get_lane_width(5), lane.get_lane_x(5), lane.get_lane_y(5)),
            LaneLayout(lane.get_lane_width(7), lane.get_lane_x(7),lane.get_lane_y(7)),
            LaneLayout(lane.get_lane_width(9), lane.get_lane_x(9), lane.get_lane_y(9)),
            LaneLayout(lane.get_lane_width(11), lane.get_lane_x(11), lane.get_lane_y(11))
        ]

        # プレイヤーは一番手前のレーンを基準にする
        self._player_lane = PlayerLayout(lane.get_lane_width(0), lane.get_lane_x(0), lane.get_lane_y(0))


    def get_lane_enemy_layout(self, cell_index: int, lane_index: int):
        # 指定された主要レーンとマスに配置する敵のレイアウトを返す
        return self._lane[lane_index].get_enemy_layout(cell_index)


    def get_lane_obstacle_layout(self, cell_index: int, lane_index: int):
        # 指定された主要レーンとマスに配置する障害物のレイアウトを返す
        return self._lane[lane_index].get_obstacle_layout(cell_index)


    def get_lane_attack_layout(self, cell_index: int, lane_index: int):
        # 指定された主要レーンとマスに配置する攻撃物のレイアウトを返す
        return self._lane[lane_index].get_attack_layout(cell_index)


    def get_middle_lane_enemy_layout(self, cell_index: int, lane_index: int):
        # 指定された中間レーンとマスに配置する敵のレイアウトを返す
        return self._middle_lane[lane_index].get_enemy_layout(cell_index)


    def get_middle_lane_obstacle_layout(self, cell_index: int, lane_index: int):
        # 指定された中間レーンとマスに配置する障害物のレイアウトを返す
        return self._middle_lane[lane_index].get_obstacle_layout(cell_index)


    def get_middle_lane_attack_layout(self, cell_index: int, lane_index: int):
        # 指定された中間レーンとマスに配置する攻撃物のレイアウトを返す
        return self._middle_lane[lane_index].get_attack_layout(cell_index)

    def get_player_layout(self, x_index: int, y_index: int):
        # 指定された位置のプレイヤーのレイアウトを返す
        return self._player_lane.get_player_layout(x_index, y_index)