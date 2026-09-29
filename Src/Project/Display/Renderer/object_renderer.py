import pygame
from Display.Renderer.image_manager import ImageManager
from Display.Layout.layout_manager import Layout
from State.attack_data import Attack

from State.player import Player
from State.stage_object_data import StageObjectManager

from asset_paths import OHUDA_IMAGE


class StageObjectDraw:
    def __init__(self, surface: pygame.Surface, image: ImageManager, layout: Layout):
        self._surface = surface
        self._image = image
        self._layout = layout
        

    def draw(self, player: Player, map_data: StageObjectManager, attack: Attack) -> None:
        self.object_draw(map_data, player)
        self.attack_draw(attack)


    def attack_draw(self, attack: Attack) -> None:

        # 攻撃中でない場合は描画しない
        if not attack.get_is_attack():
            return

        # 現在の攻撃描画データを取得する
        attack_data = attack.get_attack_data()

        # 攻撃画像を取得する
        path = attack_data["path"]
        attack_x = attack_data["x"]
        attack_y = attack_data["y"]

        if path == None:
            path = OHUDA_IMAGE
            layout = self._layout.get_lane_attack_layout(attack_x, attack_y)
        else:
            layout = self._layout.get_middle_lane_enemy_layout(attack_x, attack_y + 1)


        image = self._image.get_image(path)

        x = layout["x"]
        y = layout["y"]
        width = layout["width"]
        height = layout["height"]

        # 描画サイズに合わせて画像をリサイズする
        image = pygame.transform.scale(image, (width, height) )

        # x, yを左上座標として画像を描画する
        self._surface.blit(image, (x, y))


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


    def object_draw(self, map_data: StageObjectManager, player: Player) -> None:

        # 中間レーンに描画するかを取得する
        is_middle_draw = map_data.get_draw_on_middle_lane()

        # 一番奥のレーンから手前に向かって描画する
        lane_index = 6

        while lane_index >= 0:
            
            # 左端のマスから順番に描画する
            cell_index = 0
            while cell_index < 5:

                # 現在のマスに配置されているオブジェクトを取得する
                data = map_data.get_object(lane_index, cell_index)

                # オブジェクトが存在しない場合は次のマスへ進む
                if data is None:
                    cell_index += 1
                    continue

                if not data.get_is_draw():
                    cell_index += 1
                    continue


                # ジャンプ可能なオブジェクトか取得する
                is_jumpable = data.get_is_jumpable()

                # オブジェクトの種類と描画位置に応じたレイアウトを取得する
                if is_jumpable:
                    if is_middle_draw:
                        layout = self._layout.get_middle_lane_obstacle_layout(cell_index, lane_index)
                    else:
                        layout = self._layout.get_lane_obstacle_layout(cell_index, lane_index)
                else:
                    if is_middle_draw:
                        layout = self._layout.get_middle_lane_enemy_layout(cell_index, lane_index)
                    else:
                        layout = self._layout.get_lane_enemy_layout(cell_index, lane_index)

                # 描画位置とサイズを取得する
                x = layout["x"]
                y = layout["y"]
                width = layout["width"]
                height = layout["height"]

                # オブジェクト画像を取得する
                image = self._image.get_image(data.get_image_path())

                # 描画サイズに合わせて画像をリサイズする
                image = pygame.transform.scale(image, (width, height))

                # オブジェクトを描画する
                self._surface.blit(image, (x, y))

                # 次のマスへ進む
                cell_index += 1

            if lane_index == 1:
                self.player_draw(player)

            # 1つ手前のレーンへ進む
            lane_index -= 1