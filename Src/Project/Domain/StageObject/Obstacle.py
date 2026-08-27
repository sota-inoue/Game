from Domain.StageObject.StageObject import Obstacle

from Domain.StageObject.object_parameters import(
    BANANA_HP,
    BANANA_DAMAGE
)

from Domain.asset_paths import OBSTACLE_IMAGE_PATH

class Banana(Obstacle):
    super().__init__(
        hp = BANANA_HP,
        damage = BANANA_DAMAGE,
        image_path = OBSTACLE_IMAGE_PATH
    )