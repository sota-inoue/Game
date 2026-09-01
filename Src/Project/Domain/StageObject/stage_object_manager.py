from Domain.StageObject.player import Player

from System.map_system import Map

from System.player_position import PlayerPosition

from System.player_move import PlayerMove

from System.player_hit_check import PlayerHitCheck

class StageObjectManager:
    def __init__(self, width, height):
        # 7レーン × 5マスのオブジェクトデータを生成する
        self._objects = [ [None for _ in range(5)] for _ in range(7)]

        self._player = Player(width)

        self._map = Map(width, height)

        self.player_position = PlayerPosition()

        self.player_hit_check_system = PlayerHitCheck()

        self.player_move = PlayerMove(width, height)
        self.player_move.update(self._player)

    def player_locate_update(self) -> None:
        self.player_move.update(self._player)

    def player_position_update(self, cmd) -> None:
        self.player_position.update(cmd, self._player)

    def player_hit_check(self, count: int) -> None:
        self.player_hit_check_system.update(count, self._player, self._objects)

    def map_update(self, count: int) -> None:
        self._map.map_update(self._objects, count)



    def get_urgency_level(self) -> int:
        return self._player.get_urgency_level()

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