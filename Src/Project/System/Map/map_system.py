
from System.file_load_system import load_text

from System.Map.object_converter import ObjectConverter
from System.Map.object_layout import ObjectLayout

from StageObject.stage_object import StageObject

from Domain.asset_paths import STAGE1_PATH

class Map:
    def __init__(self, width: int, height: int):
        self._stage1_data = load_text(STAGE1_PATH)
        self._converter = ObjectConverter()
        self._layout = ObjectLayout(width, height)

    def map_update(self, objects: list[list[StageObject | None]], count: int) -> None:

        # 数値データのマップデータを取得
        new_data = self._stage1_data[(count // 5) - 1]

        # 数値データをオブジェクトへ変換する
        new_lane = self._converter.convert(new_data)

        # レーンを1つ手前へ移動する
        i = 0
        while i < len(objects) - 1:
            objects[i] = objects[i + 1].copy()
            i += 1

        # 最後のレーンに新しいレーンを設定する
        objects[-1] = new_lane

        # 各オブジェクトの座標とサイズを更新する
        self._layout.position_update(objects)
