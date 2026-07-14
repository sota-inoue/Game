from Game.stageobject import Enemy, Obstacle
from Screen.Coordinates import CoordinateManager


class StageDraw:
    def __init__(self, width, height):
        # 7レーン × 5マス分のオブジェクトデータ
        # objects[0]：レーン1（手前）
        # objects[6]：レーン7（奥）
        self.objects = [[0] * 5 for _ in range(7)]

        # オブジェクトの座標や大きさを管理するクラス
        self.locate = CoordinateManager(width, height)

        # 敵と障害物の描画用インスタンス
        self.enemy = Enemy()
        self.obstacle = Obstacle()

    def draw(self, surface):
        # レーン数を取得
        lane_num = len(self.objects)

        # 1レーンあたりのマス数を取得
        cell_num = len(self.objects[0])

        # 奥のレーンから順番に描画する
        i = lane_num - 1
        while i >= 0:
            # 左端のマスから順番に描画する
            j = 0
            while j < cell_num:

                # 敵を描画
                if self.objects[i][j] == 1:
                    # 描画座標を取得
                    x, y0 = self.locate.get_Coordinate(j, i)

                    # 敵の大きさを取得
                    w, h = self.locate.get_enemy_size(i)

                    # 描画位置を補正
                    y = y0 - h // 2

                    # 敵を描画
                    self.enemy.draw(x, y, w, h, surface)

                # 障害物を描画
                elif self.objects[i][j] == 51:
                    # 描画座標を取得
                    x, y0 = self.locate.get_Coordinate(j, i)

                    # 障害物の大きさを取得
                    w, h = self.locate.get_obstacle_size(i)

                    # 描画位置を補正
                    y = y0 - h // 2

                    # 障害物を描画
                    self.obstacle.draw(x, y, w, h, surface)

                # 次のマスへ
                j += 1

            # 1つ手前のレーンへ
            i -= 1

    def update(self, data):
        # レーン2～7のデータをレーン1～6へ移動する
        i = 0
        while i < len(self.objects) - 1:
            self.objects[i] = self.objects[i + 1].copy()
            i += 1

        # 一番奥のレーン7に新しいマップデータを設定する
        self.objects[6] = data.copy()