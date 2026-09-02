from StageObject.player import Player

from System.Map.map_system import Map
from System.Player.player_position import PlayerPosition
from System.Player.player_move import PlayerMove
from System.Player.player_hit_check import PlayerHitCheck
from System.Player.player_attack import PlayerAttack
from System.Player.attack_factory import AttackObjectFactory

class StageObjectManager:
    def __init__(self, width, height):
        # 7レーン × 5マスのオブジェクトデータを生成する
        self._objects = [ [None for _ in range(5)] for _ in range(7)]
        self._player = Player(width)
        self._attack = [None for _ in range(5)]

        self._map = Map(width, height)

        self.position = PlayerPosition()

        self.hit_check = PlayerHitCheck()
        self.attack = PlayerAttack()
        self.attack_factory = AttackObjectFactory(width, height)

        self.move = PlayerMove(width, height)
        self.move.update(self._player)

    def player_locate_update(self) -> None:
        self.move.update(self._player)

    def player_position_update(self, cmd) -> None:
        self.position.update(cmd, self._player)

    def player_hit_check(self, count: int) -> None:
        self.hit_check.update(count, self._player, self._objects)

    def map_update(self, count: int) -> None:
        self._map.map_update(self._objects, count)

    def player_attack(self) -> None:
        obj = self.attack.attack(self._player, self._objects)
        attack = self.attack_factory.get_attack_object(self._player, obj)
        self._attack = attack



    def get_urgency_level(self) -> int:
        return self._player.get_urgency_level()

    def get_attack_draw_data(self, count: int) -> dict | None:

        index = count % 5
        obj = self._attack[index]

        if obj is None:
            return None

        data = {
            "x": obj.get_x(),
            "y": obj.get_y(),
            "width": obj.get_width(),
            "height": obj.get_height(),
            "image_path": obj.get_image_path()
        }

        # 5個目の描画データを取得した後にリセット
        if index == 4:
            self._attack = [None for _ in range(5)]

        return data
    

    def get_player_draw_data(self) -> dict:
        return {
            "x": self._player.get_x(),
            "y": self._player.get_y(),
            "width": self._player.get_width(),
            "height": self._player.get_height(),
            "image_path": self._player.get_image_path()
        }

    
    def get_draw_data(self) -> list[list[dict | None]]:
        draw_data = []
        i = 0
        while i < len(self._objects):
            lane = []

            j = 0
            while j < len(self._objects[i]):
                obj = self._objects[i][j]

                if obj is None:
                    lane.append(None)

                else:
                    lane.append({
                        "x": obj.get_x(),
                        "y": obj.get_y(),
                        "width": obj.get_width(),
                        "height": obj.get_height(),
                        "image_path": obj.get_image_path()
                    })

                j += 1

            draw_data.append(lane)
            i += 1

        return draw_data