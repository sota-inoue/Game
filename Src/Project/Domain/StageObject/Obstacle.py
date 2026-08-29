from Domain.StageObject.stage_object import Obstacle

from Domain.StageObject.object_parameters import(
    BANANA_HP,
    BANANA_DAMAGE
)

from Domain.asset_paths import OBSTACLE_IMAGE_PATH

class Banana(Obstacle):
    def __init__(self) -> None:
        super().__init__(
            hp=BANANA_HP,
            damage=BANANA_DAMAGE,
            image_path=OBSTACLE_IMAGE_PATH
        )