from StageObject.stage_object import StageObject, Attack
from StageObject.player import Player, Player_Position_x
from pathlib import Path

from Domain.asset_paths import OJISAN_DAMAGED_IMAGE, OHUDA_IMAGE
from Domain.object_parameters import OJISAN_ID

class AttackObjectFactory:
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height

        base_w = width // 20

        # レーンごとのお札の横幅
        self.ohuda_width = [
            base_w,
            base_w * 6 // 7,
            base_w * 5 // 7,
            base_w * 4 // 7,
            base_w * 3 // 7,
            base_w * 2 // 7,
            base_w * 1 // 7
        ]

        lane_7_width = width * 2 // 10
        lane_7_x = (width - lane_7_width) // 2

        self.lane_x = [
            lane_7_x + lane_7_width // 6,      # 左端のx座標
            lane_7_x + lane_7_width * 2 // 6,  # 左から2番目のx座標
            lane_7_x + lane_7_width * 3 // 6,  # 中央のx座標
            lane_7_x + lane_7_width * 4 // 6,  # 左から4番目のx座標
            lane_7_x + lane_7_width * 5 // 6,  # 右端のx座標
        ]

        lane_y1 = height - (width // 20)

        # レーン番号 → Y座標
        self.lane_y = [
            lane_y1,
            lane_y1 - (height * 8 // 50),
            lane_y1 - (height * 15 // 50),
            lane_y1 - (height * 21 // 50),
            lane_y1 - (height * 26 // 50),
            lane_y1 - (height * 30 // 50),
            lane_y1 - (height * 33 // 50),
        ]

        # Y座標 → レーン番号
        self.lane_position = {
            y: i for i, y in enumerate(self.lane_y)
        }

        self._ohuda_path = OHUDA_IMAGE

        self._paths: dict[int, Path | None] = {
            OJISAN_ID: OJISAN_DAMAGED_IMAGE
        }

    def get_attack_object(self, player: Player, obj: StageObject | None) -> list[Attack]:

        px = player.get_x()
        py = player.get_y()

        # 敵がいない場合
        if obj is None:
            attack_objects = []
            end_x = self._width // 2
            end_y = 0

            size = [
                self.ohuda_width[1],
                self.ohuda_width[2],
                self.ohuda_width[3],
                self.ohuda_width[5],
                self.ohuda_width[6]
            ]

            i = 1
            while i <= 5:
                y = py + (end_y - py) * i // 5
                x = px + (end_x - px) * i // 5
                attack_objects.append( Attack(x, y, size[i - 1], size[i - 1], self._ohuda_path ) )
                i += 1
            return attack_objects

    # -------------------------
    # 敵がいる場合
    # -------------------------

        ex = obj.get_x()
        ey = obj.get_y()

        ep = self.lane_position[ey]

        eid = obj.get_id()
        ew = obj.get_width()
        eh = obj.get_height()

        enemy_path = self._paths[eid]

        x = []
        y = []
        w = []
        h = []
        paths = []

        if ep == 0:
            return [None for _ in range(5)]
        elif ep == 1:
            # 位置
            x1 = px + (ex - px) * 1 // 2
            y1 = self.lane_y[1]
            w1 = self.ohuda_width[1]
            h1 = w1

            x = [x1,ex,ex,ex,ex]
            y = [y1,ey,ey,ey,ey]
            w = [w1,ew,ew,ew,ew]
            h = [h1,eh,eh,eh,eh]
            paths = [self._ohuda_path, enemy_path, enemy_path, enemy_path, enemy_path]
        elif ep == 2:
            x1 = px + (ex - px) * 1 // 3
            y1 = self.lane_y[1]
            w1 = self.ohuda_width[1]
            h1 = w1

            x2 = px + (ex - px) * 2 // 3
            y2 = self.lane_y[2]
            w2 = self.ohuda_width[2]
            h2 = w2

            x = [x1,x2,ex,ex,ex]
            y = [y1,y2,ey,ey,ey]
            w = [w1,w2,ew,ew,ew]
            h = [h1,h2,eh,eh,eh]
            paths = [self._ohuda_path, self._ohuda_path, enemy_path, enemy_path, enemy_path]

        elif ep == 3:
            x1 = px + (ex - px) * 1 // 4
            y1 = self.lane_y[1]
            w1 = self.ohuda_width[1]
            h1 = w1

            x2 = px + (ex - px) * 2 // 4
            y2 = self.lane_y[2]
            w2 = self.ohuda_width[2]
            h2 = w2

            x3 = px + (ex - px) * 3 // 4
            y3 = self.lane_y[3]
            w3 = self.ohuda_width[3]
            h3 = w3

            x = [x1,x2,x3,ex,ex]
            y = [y1,y2,y3,ey,ey]
            w = [w1,w2,w3,ew,ew]
            h = [h1,h2,h3,eh,eh]
            paths = [self._ohuda_path, self._ohuda_path, self._ohuda_path, enemy_path, enemy_path]
        elif ep == 4:
            x1 = px + (ex - px) * 1 // 4
            y1 = self.lane_y[1]
            w1 = self.ohuda_width[1]
            h1 = w1

            x2 = px + (ex - px) * 2 // 4
            y2 = self.lane_y[2]
            w2 = self.ohuda_width[2]
            h2 = w2

            x3 = px + (ex - px) * 3 // 4
            y3 = self.lane_y[3]
            w3 = self.ohuda_width[3]
            h3 = w3

            x = [x1,x2,x3,ex,ex]
            y = [y1,y2,y3,ey,ey]
            w = [w1,w2,w3,ew,ew]
            h = [h1,h2,h3,eh,eh]
            paths = [self._ohuda_path, self._ohuda_path, self._ohuda_path, enemy_path, enemy_path]
        elif ep == 5:
            # 位置
            x1 = px + (ex - px) * 1 // 4
            y1 = self.lane_y[1]
            w1 = self.ohuda_width[1]
            h1 = w1

            x2 = px + (ex - px) * 2 // 4
            y2 = self.lane_y[2]
            w2 = self.ohuda_width[2]
            h2 = w2

            x3 = px + (ex - px) * 3 // 4
            y3 = self.lane_y[4]
            w3 = self.ohuda_width[4]
            h3 = w3

            x = [x1,x2,x3,ex,ex]
            y = [y1,y2,y3,ey,ey]
            w = [w1,w2,w3,ew,ew]
            h = [h1,h2,h3,eh,eh]
            paths = [self._ohuda_path, self._ohuda_path, self._ohuda_path, enemy_path, enemy_path]
        elif ep == 6:
            x1 = px + (ex - px) * 1 // 4
            y1 = self.lane_y[1]
            w1 = self.ohuda_width[1]
            h1 = w1

            x2 = px + (ex - px) * 2 // 4
            y2 = self.lane_y[3]
            w2 = self.ohuda_width[3]
            h2 = w2

            x3 = px + (ex - px) * 3 // 4
            y3 = self.lane_y[5]
            w3 = self.ohuda_width[5]
            h3 = w3

            x = [x1,x2,x3,ex,ex]
            y = [y1,y2,y3,ey,ey]
            w = [w1,w2,w3,ew,ew]
            h = [h1,h2,h3,eh,eh]
            paths = [self._ohuda_path, self._ohuda_path, self._ohuda_path, enemy_path, enemy_path]

        return [
            Attack(x[0], y[0], w[0], h[0], paths[0]),
            Attack(x[1], y[1], w[1], h[1], paths[1]),
            Attack(x[2], y[2], w[2], h[2], paths[2]),
            Attack(x[3], y[3], w[3], h[3], paths[3]),
            Attack(x[4], y[4], w[4], h[4], paths[4]),
        ]