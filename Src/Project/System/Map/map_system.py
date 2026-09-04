
from System.file_load_system import load_text

from System.Map.object_converter import ObjectConverter
from System.Map.object_layout import ObjectLayout

from StageObject.stage_object import StageObject, ObjectType

from Domain.asset_paths import STAGE1_PATH

class Map:
    def __init__(self, width: int, height: int):
        self._stage1_data = load_text(STAGE1_PATH)
        self._stage1_count = len(self._stage1_data)
        self._converter = ObjectConverter()
        self._layout = ObjectLayout(width, height)

    def object_hit_check(self, objects: list[list[StageObject | None]]):
        lane = len(objects)
        cell = len(objects[0])
        # HPが0以下の敵を削除する
        i = 0
        while i < lane:
            j = 0
            while j < cell:
                obj = objects[i][j]
                if obj is not None and obj.get_object_type() == ObjectType.ENEMY:
                    if objects[i][j].get_is_hit():
                        objects[i][j].set_height(0)
                        objects[i][j].set_width(0)
                        objects[i][j].set_x(0)
                        objects[i][j].set_y(0)
                j += 1
            i += 1

    def stage1_update(self, objects: list[list[StageObject | None]], count: int) -> bool:

        index = (count // 5) - 1

        if index >= self._stage1_count:
            return False

        # 数値データのマップデータを取得
        new_data = self._stage1_data[(count // 5) - 1]

        # 数値データをオブジェクトへ変換する
        new_lane = self._converter.convert(new_data)

        lane = len(objects)
        cell = len(objects[0])

        # HPが0以下の敵を削除する
        i = 0
        while i < lane:
            j = 0
            while j < cell:
                obj = objects[i][j]
                if obj is not None and obj.get_object_type() == ObjectType.ENEMY:
                    if obj.get_hp() <= 0:
                        objects[i][j] = None
                    elif obj.get_is_hit():
                        objects[i][j].set_is_hit(False)
                j += 1
            i += 1

        # レーンを1つ手前へ移動する
        i = 0
        while i < len(objects) - 1:
            objects[i] = objects[i + 1].copy()
            i += 1

        # 最後のレーンに新しいレーンを設定する
        objects[-1] = new_lane

        # 各オブジェクトの座標とサイズを更新する
        self._layout.position_update(objects)
        return True
