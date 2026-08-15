
from Load.text_loader import load_text
from Domain.config import STAGE1_PATH

class Map:
    def __init__(self):
        self.map_data = load_text(STAGE1_PATH)


    def map_update(self, datas, count):
        if not datas:
            raise ValueError("datasが空です")

        if not self.map_data:
            raise ValueError("map_dataが空です")

         # レーン2以降を1つ手前へ移動
        i = 0
        while i < len(datas) - 1:
            datas[i] = datas[i + 1].copy()
            i += 1

        # 最後のレーンに新しいマップデータを設定
        datas[-1] = self.map_data[count % len(self.map_data)].copy()
        return datas
