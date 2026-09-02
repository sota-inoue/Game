import pygame
from Renderer.image_manager import ImageManager


class StageObjectDraw:
    def __init__(self, surface: pygame.Surface, image : ImageManager):
        self._surface = surface
        self._image = image
        

    def draw(
            self, 
            player_data: dict, 
            attack_date: dict | None , 
            map_data: list[ list [ dict|None ] ]
        ) -> None:
        self.object_draw(map_data)
        self.player_draw(player_data)
        self.attck_draw(attack_date)

    def attck_draw(self, draw_data: dict | None) -> None:

        if draw_data == None:
            return
        
        x = draw_data["x"]
        y = draw_data["y"]
        width = draw_data["width"]
        height = draw_data["height"]
            
        # 画像を取得する
        image = self._image.get_image(draw_data["image_path"])
            
        # 描画サイズに変更する
        image = pygame.transform.scale(image, (width, height))
            
        # x, yを中心座標として画像を描画する
        self._surface.blit(image, (x - (width // 2) , y - height ))

    

    def player_draw(self, draw_data: dict) -> None:
        x = draw_data["x"]
        y = draw_data["y"]
        width = draw_data["width"]
        height = draw_data["height"]
        
        # 画像を取得する
        image = self._image.get_image(draw_data["image_path"])
        
        # 描画サイズに変更する
        image = pygame.transform.scale(image, (width, height))
        
        # x, yを中心座標として画像を描画する
        self._surface.blit(image, (x - (width // 2) , y - height ))


    def object_draw(self, draw_data: list[ list [ dict|None ] ] ) -> None:
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
                    image = pygame.transform.scale(image, (width, height))
                            
                    # x, yを中心座標として画像を描画する
                    self._surface.blit(image, (x - (width // 2) , y - height ))

                # 次のマスへ進む
                j += 1

            # 1つ手前のレーンへ進む
            i -= 1
