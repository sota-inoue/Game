
from System.file_load_system import load_text

from StageObject.object_converter import ObjectConverter

from StageObject.stage_object import StageObject
from State.stage_object_data import StageObjectManager
from State.player import Player

from State.game_flag import GamePhase
from asset_paths import STAGE1_PATH, STAGE2_PATH

class Map:
    def __init__(self):
        self._stage1_data = load_text(STAGE1_PATH)
        self._stage2_data = load_text(STAGE2_PATH)
        self._stage1_count = len(self._stage1_data)
        self._stage2_count = len(self._stage2_data)
        self._converter = ObjectConverter()

        self._draw_pattern = self._draw_pattern = [ False, False, True, True ]
        self._count = 0

    def draw_is_middle_lane_update(
        self,
        objects: StageObjectManager,
        player: Player,
        count: int
    ) -> None:

        # 現在の描画パターンを取得する
        pattern_index = count % len(self._draw_pattern)
        draw_pattern = self._draw_pattern[pattern_index]

        # 中間レーンに描画するかを設定する
        objects.set_draw_on_middle_lane(draw_pattern)

        if pattern_index == 2:
            objects.remove_hit_enemy_position()
            player.set_is_attack(False)
            player.set_is_hit(False)

            lane_num = 0
            cell_num = 0

            while cell_num < 4:
                obj = objects.get_object(lane_num, cell_num)

                if obj is not None:
                    if not obj.get_is_draw():
                        obj.set_is_draw(True)

                cell_num += 1


    def stage_update(self, objects: StageObjectManager, count: int, game_phase: GamePhase, boss_hp: int) -> bool:

        # ゲーム開始時はステージを更新しない
        if count == 0:
            return False

        # ステージ2のボス戦でボスのHPが0になった場合はステージクリア
        if game_phase == GamePhase.BOSS_STAGE and boss_hp <= 0:
            return True
        
        # 4カウントごとの進行回数から、次に読み込むレーンの位置を求める
        index = (count // 4) - 1

        # 現在のステージに対応する次のレーンデータを取得する
        new_lane = self._get_new_lane(index, game_phase)


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


    def _get_new_lane(self, index: int, game_phase: GamePhase ) -> list[StageObject | None] | None:
        # ステージに対応するデータを取得
        if game_phase == GamePhase.STAGE:
            stage_data = self._stage1_data
            stage_count = self._stage1_count
        elif game_phase == GamePhase.BOSS_STAGE:
            stage_data = self._stage2_data
            stage_count = self._stage2_count
        else:
            return None
        # ステージの最後まで進んだ場合
        if index >= stage_count:
            return None
        # 数値データをオブジェクトへ変換する
        return self._converter.convert(stage_data[index])