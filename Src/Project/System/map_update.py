
from System.file_load_system import load_text

from StageObject.object_converter import ObjectConverter

from StageObject.stage_object import StageObject
from State.stage_object_data import StageObjectManager
from State.player import Player, Player_Image_State

from State.game_flag import StageNumber
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

        self._draw_pattern = self._draw_pattern = [ False, False, True, True ]
        self._count = 0

    def draw_is_middle_lane_update(self, objects: StageObjectManager, player: Player) -> None:

        # 現在の描画パターンを取得する
        draw_pattern = self._draw_pattern[self._count]

        # 中間レーンに描画するかを設定する
        objects.set_draw_on_middle_lane(draw_pattern)

        if self._count == 2:
            objects.remove_hit_enemy_position()
            player.set_state(Player_Image_State.NORMAL)
            lane_num = 0
            cell_num = 0

            while cell_num < 4:
                obj = objects.get_object(lane_num, cell_num)

                if obj is not None:
                    if not obj.get_is_draw():
                        obj.set_is_draw(True)
                cell_num += 1

        # 次のパターンへ進む
        self._count += 1

        # 最後まで進んだら先頭に戻す
        if self._count >= len(self._draw_pattern):
            self._count = 0


    def stage_update(self, objects: StageObjectManager, count: int, stage_state: StageNumber) -> bool:

        # ゲーム開始時はステージを更新しない
        if count == 0:
            return False

        # 4カウントごとの進行回数から、
        # 次に読み込むレーンの位置を求める
        index = (count // 4) - 1

        # 現在のステージに対応する次のレーンデータを取得する
        new_lane = self._get_new_lane(index, stage_state)

        # ステージデータが終了した場合
        if new_lane is None:

            # 空レーンを追加して残っているオブジェクトを手前へ進める
            empty_lane = [None for _ in range(5)]
            objects.add_lane(empty_lane)

            # すべてのオブジェクトがなくなったらステージ終了
            if objects.is_empty():
                return True

            return False

        # 既存のオブジェクトを更新し、新しいレーンを追加する
        objects.add_lane(new_lane)

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