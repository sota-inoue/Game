from State.stage_object_data import StageObjectManager
from State.player import Player
from State.attack_data import Attack

def attack(player: Player, stage_objects: StageObjectManager, attack: Attack):

    # プレイヤーがいる横方向のマス位置を取得する
    x = player.get_position_x().value

    # プレイヤーと同じ列にいる一番手前の敵を探索する
    y = stage_objects.search_enemy(x)

    # 同じ列に敵がいない場合は攻撃処理を終了する
    if y == -1:
        attack.create_attack_date(x, y, None)
        return

    # 攻撃対象の敵を取得する
    target_obj = stage_objects.get_object(y, x)

    # プレイヤーの攻撃力分だけ敵のHPを減らす
    hp = target_obj.get_hp() - player.get_power()
    target_obj.set_hp(hp)

    # 攻撃を受けた状態にする
    target_obj.set_is_hit(True)

    path = target_obj.get_hit_image_path()
    attack.create_attack_date(x, y, path)
