from Domain.StageObjectClass.stage_object import StageObject

from System.StageObject.object_converter_system import ObjectConverter

from System.StageObject.object_layout_system import ObjectLayout

class StageObjectManager:
    def __init__(self, width, height):
        # 7レーン × 5マスのオブジェクトデータを生成する
        self._objects = [
            [None for _ in range(5)]
            for _ in range(7)
        ]

        self._converter = ObjectConverter()
        self._layout = ObjectLayout(width, height)

    def map_update(self, data: list[int]) -> None:
        # レーンを1つ手前へ移動する
        i = 0
        while i < len(self._objects) - 1:
            self._objects[i] = self._objects[i + 1]
            i += 1

        # 数値データをオブジェクトへ変換する
        new_lane = self._converter.convert(data)

        # 最後のレーンに新しいレーンを設定する
        self._objects[-1] = new_lane

        # 各オブジェクトの座標とサイズを更新する
        self._layout.position_update(self._objects)



         
