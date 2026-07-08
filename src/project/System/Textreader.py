from pathlib import Path

class TextReader:
    def __init__(self):
        # Textreader.py から project フォルダまで戻る
        self.base_dir = Path(__file__).resolve().parent.parent

        # stage1.txtを読み込み、ステージ1のマップデータとして保存する
        self.stage1_mapdata = self.load_mapdata("stage1.txt")

        # ステージ1のマップデータの行数を保存する
        self.stage1_size = len(self.stage1_mapdata)

    def load_mapdata(self, filename):
        # project/Resource/Map/filename のパスを作成する
        path = self.base_dir / "Resource" / "Map" / filename

        # テキストファイルを読み込む
        with open(path, "r", encoding="utf-8") as file:
            return [
                # 1行分のデータをスペースで区切り、整数に変換してリストにする
                [int(x) for x in line.split()]

                # ファイルの各行を順番に読み込む
                for line in file
            ]

    def get_mapdata1(self, line):
        # 指定された行番号のマップデータを返す
        return self.stage1_mapdata[line]