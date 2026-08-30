from Domain.StageObject.player import Player

from System.map_system import Map

from System.player_position_system import PositionSystem

class StageObjectManager:
    def __init__(self, width, height):
        # 7レーン × 5マスのオブジェクトデータを生成する
        self._objects = [
            [None for _ in range(5)]
            for _ in range(7)
        ]
        self._player = Player(width)

        self._map = Map(width, height)

        self.position_system = PositionSystem()

    def set_player_locate(self, x: int,y: int) -> None:
        self._player.set_x(x)
        self._player.set_y(y)

    def player_hitbox_update(self, cmd):
        grid_x = self._player.get_grid_x()
        grid_y = self._player.get_grid_y()
        new_grid_x, new_grid_y = self.position_system.update(cmd, grid_x, grid_y)
        self._player.set_grid_x(new_grid_x)
        self._player.set_grid_y(new_grid_y)

    def player_hit_check(self) -> None:
        # プレイヤーのマス目上の位置を取得する
        grid_x = self._player.get_grid_x()
        grid_y = self._player.get_grid_y()

        # プレイヤーと同じ位置のオブジェクトを取得する
        front_lane = self._objects[0]
        obj = front_lane[grid_x]

        # オブジェクトが存在しない場合は処理を終了する
        if obj is None:
            return
        
        # ジャンプ中かつ飛び越えられるオブジェクトの場合は接触しない
        if grid_y == 1 and obj.get_is_jumpable():
            return

        # オブジェクトの攻撃力を取得し、プレイヤーのHPを計算し更新する
        damage = obj.get_damage()
        urgency_level = self._player.get_urgency_level() + damage
        self._player.set_urgency_level(urgency_level)

    def get_urgency_level(self) -> int:
        return self._player.get_urgency_level()

    def map_update(self, count: int):
        self._map.map_update(self._objects, count)
    
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