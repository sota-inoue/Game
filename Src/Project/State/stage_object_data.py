from StageObject.stage_object import StageObject

LANE_NUM = 7
CELL_NUM = 5


class StageObjectManager:

    def __init__(self) -> None:
        # レーン数
        self._lane_num = LANE_NUM

        # 1レーンあたりのマス数
        self._cell_num = CELL_NUM

        # ステージ上のオブジェクトを管理する2次元配列
        self._objects: list[list[StageObject | None]] = [
            [None for _ in range(CELL_NUM)]
            for _ in range(LANE_NUM)
        ]

    def get_object(self, lane: int, cell: int) -> StageObject | None:
        """指定したマスのオブジェクトを取得する"""
        return self._objects[lane][cell]



    def add_lane(self, objects: list[StageObject | None]) -> None:
        """既存のレーンを前に移動し、最後に新しいレーンを追加する"""

        if len(objects) != self._cell_num:
            raise ValueError("レーンのマス数が一致していません")

        i = 0
        while i < len(self._objects) - 1:
            self._objects[i] = self._objects[i + 1].copy()
            i += 1

        # 最後のレーンに新しいレーンを設定する
        self._objects[-1] = objects.copy()

    def clear(self) -> None:
        """ステージ上のすべてのオブジェクトを削除する"""
        self._objects = [
            [None for _ in range(self._cell_num)]
            for _ in range(self._lane_num)
        ]