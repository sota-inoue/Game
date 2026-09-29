from State.stage_object_data import StageObjectManager
from State.player import Player, Player_Position_y, Player_Move_State_y, Player_Layout_y

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
            # ジャンプで回避できない場合はダメージを加算する
            if not (player_position_y == Player_Position_y.Y2 and obj.get_is_jumpable()):
                urgency_level += obj.get_damage()
                player.set_is_hit(True)
                obj.set_is_draw(False)
                if player.get_state_y() == Player_Move_State_y.JUMP and player.get_layout_y() == Player_Layout_y.Y1_0:
                    player.set_state_y(Player_Move_State_y.STAY)

                if player.get_state_y() == Player_Move_State_y.DOWN:
                    player.set_layout_y(Player_Layout_y.Y1_2)


            

        # 一定時間ごとに切迫度を増加させる
        if count - self.last_count >= 100:
            urgency_level += 5
            self.last_count = count

        # 切迫度を更新する
        player.set_urgency_level(urgency_level)
