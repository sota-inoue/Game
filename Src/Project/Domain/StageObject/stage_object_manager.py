from Domain.StageObject.player import Player

from Domain.StageObject.object_converter import ObjectConverter

from Domain.StageObject.object_layout import ObjectLayout

class StageObjectManager:
    def __init__(self, width, height):
        # 7レーン × 5マスのオブジェクトデータを生成する
        self._objects = [
            [None for _ in range(5)]
            for _ in range(7)
        ]
        self._player = Player(width)
        self._converter = ObjectConverter()
        self._layout = ObjectLayout(width, height)

    def map_update(self, data: list[int]) -> None:
        # レーンを1つ手前へ移動する
        i = 0
        while i < len(self._objects) - 1:
            self._objects[i] = self._objects[i + 1]
            i += 1
        # 数値データをオブジェクトへ変換する
        new_lane = self._converter.convert(data)
        # 最後のレーンに新しいレーンを設定する
        self._objects[-1] = new_lane
        # 各オブジェクトの座標とサイズを更新する
        self._layout.position_update(self._objects)

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