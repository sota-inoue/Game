from Domain.StageObject.stage_object import StageObject, ObjectType
from Domain.StageObject.player import Player


class PlayerAttack:
    def attack(self, player: Player, stage_objects: list[list[StageObject | None]]) -> None:

        # プレイヤーがいる横方向のマス位置を取得する
        # PlayerPositionは1始まりのため、配列の添字に合わせて1を引く
        x = player.get_position_x().value - 1

        y = 0
        while y < len(stage_objects):
            obj = stage_objects[y][x]
            # 敵が見つかった場合は探索を終了する
            if obj is not None and obj.get_object_type() == ObjectType.ENEMY:
                break
            y += 1

        # 同じ列に敵がいない場合は攻撃処理を終了する
        if y >= len(stage_objects):
            return

        # 攻撃対象の敵を取得する
        target_obj = stage_objects[y][x]

        # プレイヤーの攻撃力分だけ敵のHPを減らす
        hp = target_obj.get_hp() - player.get_power()
        target_obj.set_hp(hp)

        # HPが0以下になった敵をマップ上から削除する
        if target_obj.get_hp() <= 0:
            stage_objects[y][x] = None

