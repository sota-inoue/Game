from Renderer.object_renderer import Enemy, Obstacle,Player
from Domain.layout import Coordinate

class PlayerDraw:
    def __init__(self, width, height, image):
        self.player_width = width // 10
        self.player_height = self.player_width * 5 // 3
        self.player = Player(image)

    def draw(self, surface, player_x, player_y):
        # プレイヤーの描画
        self.player.draw(player_x, player_y, self.player_width, self.player_height, surface)


class StageObjectDraw:
    def __init__(self, width, height, enemy_image, obstacle_image):
        # オブジェクトの座標や大きさを管理するクラス
        self.locate = Coordinate(width, height)
        # 敵と障害物の描画用インスタンス
        self.enemy = Enemy(enemy_image)
        self.obstacle = Obstacle(obstacle_image)

    def draw(self, surface, mapdata):
        # レーン数を取得
        lane_num = len(mapdata)

        # 1レーンあたりのマス数を取得
        cell_num = len(mapdata[0])

        # 奥のレーンから順番に描画する
        i = lane_num - 1
        while i >= 0:
            # 左端のマスから順番に描画する
            j = 0
            while j < cell_num:

                # 敵を描画
                if mapdata[i][j] == 1:
                    # 描画座標を取得
                    x, y0 = self.locate.get_Coordinate(j, i)

                    # 敵の大きさを取得
                    w, h = self.locate.get_enemy_size(i)

                    # 描画位置を補正
                    y = y0 - h // 2

                    # 敵を描画
                    self.enemy.draw(x, y, w, h, surface)

                # 障害物を描画
                elif mapdata[i][j] == 51:
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
