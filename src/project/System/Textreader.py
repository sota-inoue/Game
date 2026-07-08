from pathlib import Path

class MapManager:
    def __init__(self):
        # このファイルが置かれているフォルダのパスを取得する
        self.base_dir = Path(__file__).resolve().parent

        # stage1.txtを読み込み、ステージ1のマップデータとして保存する
        self.stage1_mapdata = self.load_mapdata("stage1.txt")

        # ステージ1のマップデータの行数を保存する
        self.stage1_size = len(self.stage1_mapdata)

    def load_mapdata(self, filename):
        # 読み込むテキストファイルのパスを作成する
        path = self.base_dir / filename

        # テキストファイルを読み込む
        with open(path, "r", encoding="utf-8") as file:
            return [
                # 1行分の文字を1文字ずつ整数に変換してリストにする
                [int(x) for x in line.strip()]

                # ファイルの各行を順番に読み込む
                for line in file
            ]

    def get_mapdata1(self, line):
        # 指定された行番号のマップデータを返す
        return self.stage1_mapdata[line]