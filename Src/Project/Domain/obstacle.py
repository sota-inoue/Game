#StageObject/obstacle.py
from Domain.stage_object import StageObject, ObjectType

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

from asset_paths import OBSTACLE_IMAGE_PATH

class Obstacle(StageObject):
    def __init__(self, damage : int, image_path : str, is_jumpable: bool, id: int) -> None:
        super().__init__(object_type=ObjectType.OBSTACLE)
        self._id: int = id
        self._damage: int = damage
        self.set_image_path(image_path)
        self._is_jumpable: bool = is_jumpable
        self.set_id(id)

    # _idのgetterとsetter
    def get_id(self) -> int:
        return self._id

    def set_id(self, id: int) -> None:
        if not isinstance(id, int):
            raise TypeError(f"受け取った型 {type(id).__name__} : int型を指定してください。")
        self._id = id

    # _damageのgetterとsetter
    def get_damage(self) -> int:
        return self._damage

    def set_damage(self, damage: int) -> None:
        if not isinstance(damage, int):
            raise TypeError(f"受け取った型 {type(damage).__name__} : int型を指定してください。")
        self._damage = damage

    # _is_jumpableのgetterとsetter
    def get_is_jumpable(self) -> bool:
        return self._is_jumpable

    def set_is_jumpable(self, is_jumpable: bool) -> None:
        if not isinstance(is_jumpable, bool):
            raise TypeError(f"受け取った型 {type(is_jumpable).__name__} : bool型を指定してください。")
        self._is_jumpable = is_jumpable

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