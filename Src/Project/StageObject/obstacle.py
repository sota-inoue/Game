#StageObject/obstacle.py
from StageObject.stage_object import Obstacle

from Domain.object_parameters import(
    BANANA_DAMAGE,
    BANANA_IS_JUMPABLE,
    BANANA_ID,
    COLOR_CONE_DAMAGE,
    COLOR_CONE_IS_JUMPABLE,
    COLOR_CONE_ID,
    CARRY_CASE_OBSTACLE_DAMAGE,
    CARRY_CASE_OBSTACLE_IS_JUMPABLE,
    CARRY_CASE_OBSTACLE_ID
)

from Domain.asset_paths import OBSTACLE_IMAGE_PATH

class Banana(Obstacle):
    def __init__(self) -> None:
        # IDは一意の初期値を割り当て（ID = 51）
        super().__init__(
            damage=BANANA_DAMAGE,
            image_path=OBSTACLE_IMAGE_PATH,
            is_jumpable=BANANA_IS_JUMPABLE,
            id=BANANA_ID
        )
        # TODO: スコア減算(300)の処理を後で実装
        
class ColorCone(Obstacle):
    def __init__(self) -> None:
        # IDは一意の初期値を割り当て（ID = 56）
        super().__init__(
            damage=COLOR_CONE_DAMAGE,
            image_path=OBSTACLE_IMAGE_PATH,
            is_jumpable=COLOR_CONE_IS_JUMPABLE,
            id=COLOR_CONE_ID
        )
        # TODO: スコア減算(300)の処理を後で実装

class CarryCaseObstacle(Obstacle):
    def __init__(self) -> None:
        # IDは一意の初期値を割り当て（ID = 61）
        super().__init__(
            damage=CARRY_CASE_OBSTACLE_DAMAGE,
            image_path=OBSTACLE_IMAGE_PATH,
            is_jumpable=CARRY_CASE_OBSTACLE_IS_JUMPABLE,
            id=CARRY_CASE_OBSTACLE_ID
        )
        # TODO: 2マス分の当たり判定ロジックを後で実装
        # TODO: スコア減算(300)の処理を後で実装