import pygame
from Display.Renderer.image_manager import ImageManager
from Display.Layout.layout_manager import Layout

from State.player import Player
from State.stage_object_data import StageObjectManager


class StageObjectDraw:
    def __init__(self, surface: pygame.Surface, image: ImageManager, layout: Layout):
        self._surface = surface
        self._image = image
        self._layout = layout
        

    def draw(self, player: Player, map_data: StageObjectManager) -> None:
        self.object_draw(map_data)
        self.player_draw(player)

    def middle_draw(self, player: Player, map_data: StageObjectManager) -> None:
        self.middle_object_draw(map_data)
        self.player_draw(player)


    def player_draw(self, player: Player) -> None:
        layout_x = player.get_layout_x()
        layout_y = player.get_layout_y()

        # 現在のレイアウト位置から描画情報を取得する
        layout = self._layout.get_player_layout(layout_x.value, layout_y.value)

        x = layout["x"]
        y = layout["y"]
        width = layout["width"]
        height = layout["height"]

        # プレイヤー画像を取得する
        path = player.get_image_path()
        image = self._image.get_image(path)

        # 描画サイズに合わせて画像をリサイズする
        image = pygame.transform.scale(image, (width, height))

        # x, yを左上座標として画像を描画する
        self._surface.blit(image, (x, y))


    def object_draw(self, map_data: StageObjectManager) -> None:

        # レーン数を取得する
        lane_num = 7

        # 1レーンあたりのマス数を取得する
        cell_num = 5

        # 一番奥のレーンから手前に向かって描画する
        lane_index = lane_num - 1

        while lane_index >= 0:

            # 左端のマスから順番に描画する
            cell_index = 0

            while cell_index < cell_num:

                # 現在のマスに配置されているオブジェクトを取得する
                data = map_data.get_object(lane_index, cell_index)

                # オブジェクトが存在する場合のみ描画する
                if data is not None:

                    # オブジェクトの種類に応じたレイアウトを取得する
                    if not data.get_is_jumpable():
                        layout = self._layout.get_lane_enemy_layout(cell_index, lane_index)
                    else:
                        layout = self._layout.get_lane_obstacle_layout(cell_index, lane_index)

                    # 描画位置と描画サイズを取得する
                    x = layout["x"]
                    y = layout["y"]
                    width = layout["width"]
                    height = layout["height"]

                    # オブジェクトの画像を取得する
                    path = data.get_image_path()
                    image = self._image.get_image(path)

                    # レイアウトのサイズに合わせて画像をリサイズする
                    image = pygame.transform.scale(image, (width, height))

                    # 指定された座標に画像を描画する
                    self._surface.blit(image, (x, y))

                # 次のマスへ進む
                cell_index += 1

            # 1つ手前のレーンへ進む
            lane_index -= 1

    def middle_object_draw(self, map_data: StageObjectManager) -> None:

        # レーン数を取得する
        lane_num = 7
        # 1レーンあたりのマス数を取得する
        cell_num = 5

        # 一番奥のレーンから手前に向かって描画する
        lane_index = lane_num - 1

        # レーン0より手前にはミドルレーンが存在しないため1まで
        while lane_index >= 1:

            cell_index = 0

            while cell_index < cell_num:

                # 現在のマスに配置されているオブジェクトを取得する
                data = map_data.get_object(lane_index, cell_index)

                if data is not None:

                    # 通常レーンから1つ手前のレーンとの間にある
                    # ミドルレーンを使用する
                    middle_index = lane_index - 1

                    if not data.get_is_jumpable():
                        layout = self._layout.get_middle_lane_enemy_layout(
                            cell_index,
                            middle_index
                        )
                    else:
                        layout = self._layout.get_middle_lane_obstacle_layout(
                            cell_index,
                            middle_index
                        )

                    x = layout["x"]
                    y = layout["y"]
                    width = layout["width"]
                    height = layout["height"]

                    path = data.get_image_path()
                    image = self._image.get_image(path)

                    image = pygame.transform.scale(
                        image,
                        (width, height)
                    )

                    self._surface.blit(image, (x, y))

                cell_index += 1

            lane_index -= 1