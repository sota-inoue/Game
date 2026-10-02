from StageObject.stage_object import StageObject, ObjectType


LANE_NUM = 7
CELL_NUM = 5


class StageObjectManager:

    def __init__(self) -> None:
        # レーン数
        self._lane_num: int = LANE_NUM

        # 1レーンあたりのマス数
        self._cell_num: int = CELL_NUM

        self._is_middle_lane_drawable: bool = False

        # ステージ上のオブジェクトを管理する2次元配列
        self._objects: list[list[StageObject | None]] = [
            [None for _ in range(CELL_NUM)]
            for _ in range(LANE_NUM)
        ]


    def search_enemy(self, cell: int) -> int:
        # 0番レーンは攻撃対象外なので、1番レーンから探索する
        lane_num = 1

        while lane_num < len(self._objects):
            # 指定した列のオブジェクトを取得する
            obj = self._objects[lane_num][cell]

            # 敵が見つかった場合は、一番手前の敵としてレーン番号を返す
            if obj is not None and obj.get_object_type() == ObjectType.ENEMY:
                return lane_num

            # 次のレーンへ進む
            lane_num += 1

        # 攻撃対象となる敵が存在しない場合
        return -1


    
    def get_object(self, lane: int, cell: int) -> StageObject | None:
        """指定したマスのオブジェクトを取得する"""
        return self._objects[lane][cell]



    def add_lane(self, objects: list[StageObject | None]) -> None:
        """既存のレーンを前に移動し、最後に新しいレーンを追加する"""

        if len(objects) != self._cell_num:
            raise ValueError("レーンのマス数が一致していません")

        # 既存のレーンを1つ手前に移動する
        i = 0
        while i < len(self._objects) - 1:
            self._objects[i] = self._objects[i + 1].copy()
            i += 1

        # 最後のレーンに新しいレーンを設定する
        self._objects[-1] = objects.copy()
        self._object_update()

    def _object_update(self) -> None:
        lane_num = 0
        while lane_num < len(self._objects):
            cell_num = 0
            while cell_num < len(self._objects[lane_num]):
                obj = self._objects[lane_num][cell_num]
                if obj is not None:
                    # 敵の場合はHPとヒット状態を確認する
                    obj.set_is_draw(True)
                    if obj.get_object_type() == ObjectType.ENEMY:
                        if obj.get_hp() <= 0:
                            self._objects[lane_num][cell_num] = None
                            cell_num += 1
                            continue
                        if obj.get_is_hit():
                            obj.set_is_hit(False)
                cell_num += 1
            lane_num += 1


    def remove_hit_enemy_position(self) -> None:
        lane_num = 0
        while lane_num < len(self._objects):
            cell_num = 0
            while cell_num < len(self._objects[lane_num]):
                obj = self._objects[lane_num][cell_num]
                if obj is not None and obj.get_object_type() == ObjectType.ENEMY:
                    if obj.get_is_hit():
                        obj.set_is_draw(False)
                cell_num += 1
            lane_num += 1


    def is_empty(self) -> bool:
        lane_num = 0
        while lane_num < len(self._objects):
            cell_num = 0
            while cell_num < len(self._objects[lane_num]):
                if self._objects[lane_num][cell_num] is not None:
                    return False
                cell_num += 1
            lane_num += 1
        return True


    def clear(self) -> None:
        """ステージ上のすべてのオブジェクトを削除する"""
        self._objects = [
            [None for _ in range(self._cell_num)]
            for _ in range(self._lane_num)
        ]

    def get_draw_on_middle_lane(self) -> bool:
        return self._draw_on_middle_lane

    def set_draw_on_middle_lane(self, value: bool) -> None:
        self._draw_on_middle_lane = value