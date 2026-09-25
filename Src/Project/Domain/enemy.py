#StageObject/enemy.py
from Domain.stage_object import StageObject, ObjectType

from Domain.object_parameters import(
    OJISAN_HP,
    OJISAN_DAMAGE,
    OJISAN_IS_JUMPABLE,
    OJISAN_ID,
    STRONG_OJISAN_HP,
    STRONG_OJISAN_DAMAGE,
    STRONG_OJISAN_IS_JUMPABLE,
    STRONG_OJISAN_ID,
    SMARTPHONE_USER_HP,
    SMARTPHONE_USER_DAMAGE,
    SMARTPHONE_USER_IS_JUMPABLE,
    SMARTPHONE_USER_ID,
    FUROCAN_KAIWAI_HP,
    FUROCAN_KAIWAI_DAMAGE,
    FUROCAN_KAIWAI_IS_JUMPABLE,
    FUROCAN_KAIWAI_ID,
    CARRY_CASE_PERSON_HP,
    CARRY_CASE_PERSON_DAMAGE,
    CARRY_CASE_PERSON_IS_JUMPABLE,
    CARRY_CASE_PERSON_ID,
    YANCHA_GROUP_HP,
    YANCHA_GROUP_DAMAGE,
    YANCHA_GROUP_IS_JUMPABLE,
    YANCHA_GROUP_ID,
    CIVILIAN_HP,
    CIVILIAN_DAMAGE,
    CIVILIAN_IS_JUMPABLE,
    CIVILIAN_ID
)

from asset_paths import ENEMY_IMAGE_PATH

class Enemy(StageObject):
    def __init__(self, image_path: str, id: int, size: int, is_jumpable: bool, damage: int, hp: int, hit_image: str) -> None:
        super().__init__(ObjectType.ENEMY, image_path, id , size, is_jumpable, damage)

        self._hp: int = hp
        self._hit_image_path = hit_image

        self.is_hit: bool = False

    # _hpのgetterとsetter
    def get_hp(self) -> int:
        return self._hp
    
    def set_hp(self, hp: int) -> None:
        if not isinstance(hp, int):
            raise TypeError(f"受け取った型 {type(hp).__name__} : int型を指定してください。")
        self._hp = hp


    def set_is_hit(self, is_hit: bool) -> None:
        self.is_hit = is_hit

    def get_is_hit(self) -> bool:
        return self.is_hit

    
    # _image_pathのgetterとsetter
    def get_hit_image_path(self) -> str:
        return self._hit_image_path
    


class Ojisan(Enemy):
    def __init__(self) -> None:
        # IDは一意の初期値を割り当て（ID範囲: 1~3）
        super().__init__(
            image_path = ENEMY_IMAGE_PATH,
            id = OJISAN_ID,
            size = 1,
            is_jumpable = OJISAN_IS_JUMPABLE,
            damage=OJISAN_DAMAGE,
            hp=OJISAN_HP,
            hit_image=ENEMY_IMAGE_PATH
        )

# class StrongOjisan(Enemy):
#     def __init__(self) -> None:
#         # IDは一意の初期値を割り当て（ID範囲: 4~6）
#         super().__init__(
#             hp=STRONG_OJISAN_HP,
#             damage=STRONG_OJISAN_DAMAGE,
#             image_path=ENEMY_IMAGE_PATH,
#             is_jumpable=STRONG_OJISAN_IS_JUMPABLE,
#             id=STRONG_OJISAN_ID,
#             hit_image=ENEMY_IMAGE_PATH
#         )
#         # TODO: 左右1マスの当たり判定ロジックを後で実装
#         # TODO: スコア加算(1000)・減算(1000)の処理を後で実装


# class SmartphoneUser(Enemy):
#     def __init__(self) -> None:
#         # IDは一意の初期値を割り当て（ID範囲: 11~14）
#         super().__init__(
#             hp=SMARTPHONE_USER_HP,
#             damage=SMARTPHONE_USER_DAMAGE,
#             image_path=ENEMY_IMAGE_PATH,
#             is_jumpable=SMARTPHONE_USER_IS_JUMPABLE,
#             id=SMARTPHONE_USER_ID,
#             hit_image=ENEMY_IMAGE_PATH
#         )
#         # TODO: スコア加算(300)・減算(300)の処理を後で実装


# class FurocanKaiwai(Enemy):
#     def __init__(self) -> None:
#         # IDは一意の初期値を割り当て（ID範囲: 16~19）
#         super().__init__(
#             hp=FUROCAN_KAIWAI_HP,
#             damage=FUROCAN_KAIWAI_DAMAGE,
#             image_path=ENEMY_IMAGE_PATH,
#             is_jumpable=FUROCAN_KAIWAI_IS_JUMPABLE,
#             id=FUROCAN_KAIWAI_ID,
#             hit_image=ENEMY_IMAGE_PATH
#         )
#         # TODO: 左右2マスの当たり判定およびダメージ分岐（本人20、左右5）のロジックを後で実装
#         # TODO: スコア加算(1000)・減算(1000)の処理を後で実装


# class CarryCasePerson(Enemy):
#     def __init__(self) -> None:
#         # IDは一意の初期値を割り当て（ID範囲: 21~24）
#         super().__init__(
#             hp=CARRY_CASE_PERSON_HP,
#             damage=CARRY_CASE_PERSON_DAMAGE,
#             image_path=ENEMY_IMAGE_PATH,
#             is_jumpable=CARRY_CASE_PERSON_IS_JUMPABLE,
#             id=CARRY_CASE_PERSON_ID,
#             hit_image=ENEMY_IMAGE_PATH
#         )
#         # TODO: 2マス分の当たり判定ロジックを後で実装
#         # TODO: スコア加算(0)・減算(500)の処理を後で実装


# class YanchaGroup(Enemy):
#     def __init__(self) -> None:
#         # IDは一意の初期値を割り当て（ID = 26）
#         super().__init__(
#             hp=YANCHA_GROUP_HP,
#             damage=YANCHA_GROUP_DAMAGE,
#             image_path=ENEMY_IMAGE_PATH,
#             is_jumpable=YANCHA_GROUP_IS_JUMPABLE,
#             id=YANCHA_GROUP_ID,
#             hit_image=ENEMY_IMAGE_PATH
#         )
#         # TODO: 横4マス分の当たり判定ロジックを後で実装
#         # TODO: スコア加算(1000)・減算(1000)の処理を後で実装

# class Civilian(Enemy):
#     def __init__(self) -> None:
#         # IDは一意の初期値を割り当て（ID範囲: 41~45）
#         super().__init__(
#             hp=CIVILIAN_HP,
#             damage=CIVILIAN_DAMAGE,
#             image_path=ENEMY_IMAGE_PATH,
#             is_jumpable=CIVILIAN_IS_JUMPABLE,
#             id=CIVILIAN_ID,
#             hit_image=ENEMY_IMAGE_PATH
#         )
#         # TODO: 攻撃不可（判定・ダメージロジック）を後で実装
#         # TODO: スコア加算(0)・減算(500)の処理を後で実装
    