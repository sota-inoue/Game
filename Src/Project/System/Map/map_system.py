
from System.file_load_system import load_text

from System.Map.object_converter import ObjectConverter

from Domain.stage_object import StageObject, Object_Position_x, Object_Position_y

from Domain.game_flag import StageNumber
from asset_paths import STAGE1_PATH, STAGE2_PATH, STAGE3_PATH

class Map:
    def __init__(self):
        self._stage1_data = load_text(STAGE1_PATH)
        self._stage2_data = load_text(STAGE2_PATH)
        self._stage3_data = load_text(STAGE3_PATH)
        self._stage1_count = len(self._stage1_data)
        self._stage2_count = len(self._stage2_data)
        self._stage3_count = len(self._stage3_data)
        self._converter = ObjectConverter()


    def stage_update(self, objects: list[list[StageObject | None]], count: int, stage_state: StageNumber) -> bool:
        # ゲーム開始時はステージを更新しない
        if count == 0:
            return False

        # 5カウントごとの進行回数から、次に読み込むレーンの位置を求める
        index = (count // 4) - 1

        # 現在のステージに対応する次のレーンデータを取得する
        new_lane = self._get_new_lane(index, stage_state)

        # 次のレーンが存在しない場合は、ステージ終了を通知する
        if new_lane is None:
            return True

        # 既存のオブジェクトを更新し、新しいレーンを追加する
        self._lane_update(objects, new_lane)

        # ステージが継続していることを通知する
        return False


    def _get_new_lane(self, index: int, stage_state: StageNumber ) -> list[StageObject | None] | None:
        # ステージに対応するデータを取得
        if stage_state == StageNumber.STAGE_1:
            stage_data = self._stage1_data
            stage_count = self._stage1_count
        elif stage_state == StageNumber.STAGE_2:
            stage_data = self._stage2_data
            stage_count = self._stage2_count
        elif stage_state == StageNumber.STAGE_3:
            stage_data = self._stage3_data
            stage_count = self._stage3_count
        else:
            return None
        # ステージの最後まで進んだ場合
        if index >= stage_count:
            return None
        # 数値データをオブジェクトへ変換する
        return self._converter.convert(stage_data[index])


    def _lane_update(self, objects: list[list[StageObject | None]], new_lane: list[StageObject | None]) -> None:
        # レーンを1つ手前へ移動する
        i = 0
        while i < len(objects) - 1:
            objects[i] = objects[i + 1].copy()
            i += 1

        # 最後のレーンに新しいレーンを設定する
        objects[-1] = new_lane

        # 配列の位置に合わせて、 各オブジェクトのX・Y位置情報を更新する
        y = 0
        while y < len(objects):
            x = 0
            while x < len(objects[y]):
                obj = objects[y][x]
                if obj is not None:
                    obj.set_position_x(Object_Position_x(x))
                    obj.set_position_y(Object_Position_y(y))
                x += 1
            y += 1