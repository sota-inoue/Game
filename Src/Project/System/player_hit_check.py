from Domain.StageObject.stage_object import StageObject
from Domain.StageObject.player import Player, Player_Position_y

class PlayerHitCheck:
    def __init__(self):
        self.last_count: int = 0

    def update(self, count: int, player: Player, stage_data: list[list[StageObject | None]]) -> None:

         # プレイヤーの現在のマス位置を取得する
        player_position_x = player.get_player_position_x()
        player_position_y = player.get_player_position_y()

        # 一番手前のレーンを取得する
        front_lane = stage_data[0]

        # プレイヤーと同じ位置のオブジェクトを取得する
        obj = front_lane[player_position_x.value - 1]

        # 現在の切迫度を取得する
        urgency_level = player.get_urgency_level()

        # オブジェクトが存在する場合
        if obj is not None:
            # ジャンプで回避できない場合はダメージを加算する
            if not (player_position_y == Player_Position_y.Y2 and obj.get_is_jumpable()):
                urgency_level += obj.get_damage()

        # 一定時間ごとに切迫度を増加させる
        if count - self.last_count >= 100:
            urgency_level += 5
            self.last_count = count

        # 切迫度を更新する
        player.set_urgency_level(urgency_level)
