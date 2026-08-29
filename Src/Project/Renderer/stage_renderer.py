import pygame
from Renderer.object_renderer import Player
from Renderer.image_manager import ImageManager

class PlayerDraw:
    def __init__(self, width, height, image):
        self.player_width = width // 10
        self.player_height = self.player_width * 5 // 3
        self.player = Player(image)

    def draw(self, surface, player_x, player_y):
        # プレイヤーの描画
        self.player.draw(player_x, player_y, self.player_width, self.player_height, surface)


class StageObjectDraw:
    def __init__(self, image : ImageManager):
        self._image = image

    def draw(self, surface: pygame.Surface, draw_data: list[ list [ dict|None ] ] ) -> None:
        # レーン数を取得
        lane_num = len(draw_data)

        # 1レーンあたりのマス数を取得
        cell_num = len(draw_data[0])

        # 奥のレーンから順番に描画する
        i = lane_num - 1
        while i >= 0:

            # 左端のマスから順番に描画する
            j = 0
            while j < cell_num:

                # 現在のマスの描画データを取得
                data = draw_data[i][j]

                # オブジェクトが存在する場合のみ描画する
                if data is not None:
                    x = data["x"]
                    y = data["y"]
                    width = data["width"]
                    height = data["height"]

                    # 画像を取得する
                    image = self._image.get_image(data["image_path"])

                    # 描画サイズに変更する
                    image = pygame.transform.scale(
                        image,
                        (width, height)
                    )

                    # x, yを中心座標として画像を描画する
                    surface.blit(
                        image,
                        (
                            x - (width // 2),
                            y - (height // 2)
                        )
                    )

                # 次のマスへ進む
                j += 1

            # 1つ手前のレーンへ進む
            i -= 1