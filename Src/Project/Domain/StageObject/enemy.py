from Domain.StageObject.stage_object import Enemy

from Domain.StageObject.object_parameters import(
    OJISAN_HP,
    OJISAN_DAMAGE,
    OJISAN_IS_JUMPABLE,
    OJISAN_ID
)

from Domain.asset_paths import ENEMY_IMAGE_PATH

class Ojisan(Enemy):
    def __init__(self) -> None:
        super().__init__(
            hp=OJISAN_HP,
            damage=OJISAN_DAMAGE,
            image_path=ENEMY_IMAGE_PATH,
            is_jumpable=OJISAN_IS_JUMPABLE,
            id=OJISAN_ID
        )

    