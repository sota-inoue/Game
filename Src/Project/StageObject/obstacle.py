#StageObject/obstacle.py
from StageObject.stage_object import Obstacle

from Domain.object_parameters import(
    BANANA_DAMAGE,
    BANANA_IS_JUMPABLE,
    BANANA_ID,
    BANANA_ADD_SCORE,
    BANANA_SUB_SCORE,
    COLOR_CONE_DAMAGE,
    COLOR_CONE_IS_JUMPABLE,
    COLOR_CONE_ID,
    COLOR_CONE_ADD_SCORE,
    COLOR_CONE_SUB_SCORE,
    CARRY_CASE_OBSTACLE_DAMAGE,
    CARRY_CASE_OBSTACLE_IS_JUMPABLE,
    CARRY_CASE_OBSTACLE_ID,
    CARRY_CASE_OBSTACLE_ADD_SCORE,
    CARRY_CASE_OBSTACLE_SUB_SCORE
)

from Domain.asset_paths import (
    BANANA_IMAGE_PATH,
    COLOR_CONE_IMAGE_PATH,
    CARRY_CASE_OBSTACLE_IMAGE_PATH,
)
class Banana(Obstacle):
    def __init__(self) -> None:
        # IDは一意の初期値を割り当て（ID = 51）
        super().__init__(
            damage=BANANA_DAMAGE,
            image_path=BANANA_IMAGE_PATH,
            is_jumpable=BANANA_IS_JUMPABLE,
            id=BANANA_ID,
            add_score=BANANA_ADD_SCORE,
            sub_score=BANANA_SUB_SCORE
        )
        
class ColorCone(Obstacle):
    def __init__(self) -> None:
        # IDは一意の初期値を割り当て（ID = 56）
        super().__init__(
            damage=COLOR_CONE_DAMAGE,
            image_path=COLOR_CONE_IMAGE_PATH,
            is_jumpable=COLOR_CONE_IS_JUMPABLE,
            id=COLOR_CONE_ID,
            add_score=COLOR_CONE_ADD_SCORE,
            sub_score=COLOR_CONE_SUB_SCORE
        )
class CarryCaseObstacle(Obstacle):
    def __init__(self) -> None:
        # IDは一意の初期値を割り当て（ID = 61）
        super().__init__(
            damage=CARRY_CASE_OBSTACLE_DAMAGE,
            image_path=CARRY_CASE_OBSTACLE_IMAGE_PATH,
            is_jumpable=CARRY_CASE_OBSTACLE_IS_JUMPABLE,
            id=CARRY_CASE_OBSTACLE_ID,
            add_score=CARRY_CASE_OBSTACLE_ADD_SCORE,
            sub_score=CARRY_CASE_OBSTACLE_SUB_SCORE
        )
        # TODO: 2マス分の当たり判定ロジックを後で実装
        