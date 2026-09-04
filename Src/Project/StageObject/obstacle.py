from StageObject.stage_object import Obstacle

from Domain.object_parameters import(
    BANANA_DAMAGE,
    BANANA_IS_JUMPABLE,
    BANANA_ID
)

from Domain.asset_paths import OBSTACLE_IMAGE_PATH

class Banana(Obstacle):
    def __init__(self) -> None:
        super().__init__(
            damage=BANANA_DAMAGE,
            image_path=OBSTACLE_IMAGE_PATH,
            is_jumpable=BANANA_IS_JUMPABLE,
            id=BANANA_ID
        )