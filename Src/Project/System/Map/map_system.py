
from System.file_load_system import load_text

from System.Map.object_converter import ObjectConverter
from System.Map.object_layout import ObjectLayout

from StageObject.stage_object import StageObject, ObjectType

from Domain.state import StageState
from Domain.asset_paths import STAGE1_PATH, STAGE2_PATH, STAGE3_PATH

class Map:
    def __init__(self, width: int, height: int):
        self._stage1_data = load_text(STAGE1_PATH)
        self._stage2_data = load_text(STAGE2_PATH)
        self._stage3_data = load_text(STAGE3_PATH)
        self._stage1_count = len(self._stage1_data)
        self._stage2_count = len(self._stage2_data)
        self._stage3_count = len(self._stage3_data)
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

    def stage_update(self, objects: list[list[StageObject | None]], count: int, stage_state: StageState) -> bool:

        if count == 0:
            return True

        index = (count // 5) - 1

        # ステージに対応するデータを取得
        if stage_state == StageState.STAGE1:
            stage_data = self._stage1_data
            stage_count = self._stage1_count
        elif stage_state == StageState.STAGE2:
            stage_data = self._stage2_data
            stage_count = self._stage2_count
        elif stage_state == StageState.STAGE3:
            stage_data = self._stage3_data
            stage_count = self._stage3_count
        else:
            return False

        # ステージの最後まで進んだ場合
        if index >= stage_count:
            return False

        # 数値データのマップデータを取得
        new_data = stage_data[index]

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
