from State.stage_object_data import StageObjectManager
from State.player import Player, Player_Move_State_y

from StageObject.object_parameters import BOSS_HOMING_ATTACK_ID, OJISAN_ID

class PlayerHitCheck:
    def __init__(self):
        self.last_count: int = 0

    def update(self, count: int, player: Player, stage_data: StageObjectManager) -> None:

         # プレイヤーの現在のマス位置を取得する
        player_position_x = player.get_position_x()
        player_position_y = player.get_position_y()

        # 一番手前のレーンを取得する
        lane_num = 0
        cell_num = player_position_x.value

        # プレイヤーと同じ位置のオブジェクトを取得する
        obj = stage_data.get_object(lane_num, cell_num)

        # 現在の切迫度を取得する
        urgency_level = player.get_urgency_level()

        # オブジェクトが存在する場合
        if obj is not None:

            # ジャンプ中かどうか
            is_jump = player.get_state_y() == Player_Move_State_y.JUMP
            
            is_jumpable = obj.get_is_jumpable()

            # ジャンプしていない、またはジャンプで回避できない場合
            if not is_jump or not is_jumpable:

                urgency_level += obj.get_damage()
                player.set_is_hit(True)
                obj.set_is_draw(False)


        # プレイヤーの左隣のマス
        left_cell = cell_num - 1

        if left_cell >= 0:
            obj1 = stage_data.get_object(lane_num, left_cell)

            if obj1 is not None:
                if obj1.get_id() == BOSS_HOMING_ATTACK_ID or obj1.get_id() == OJISAN_ID:
                    urgency_level += obj1.get_damage()
                    player.set_is_hit(True)

                    obj1.set_is_side_move(True)
                    obj1.set_cell_num(left_cell)


        # プレイヤーの右隣のマス
        right_cell = cell_num + 1

        if right_cell < 5:
            obj2 = stage_data.get_object(lane_num, right_cell)

            if obj2 is not None:
                if obj2.get_id() == BOSS_HOMING_ATTACK_ID or obj2.get_id() == OJISAN_ID:
                    urgency_level += obj2.get_damage()
                    player.set_is_hit(True)

                    obj2.set_is_side_move(True)
                    obj2.set_cell_num(cell_num)

            

        # 一定時間ごとに切迫度を増加させる
        if count - self.last_count >= 100:
            urgency_level += 5
            self.last_count = count

        # 切迫度を更新する
        player.set_urgency_level(urgency_level)
