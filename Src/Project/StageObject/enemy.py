#StageObject/enemy.py
from StageObject.stage_object import Enemy

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

from Domain.asset_paths import ENEMY_IMAGE_PATH

class Ojisan(Enemy):
    def __init__(self) -> None:
        # IDは一意の初期値を割り当て（ID範囲: 1~3）
        super().__init__(
            hp=OJISAN_HP,
            damage=OJISAN_DAMAGE,
            image_path=ENEMY_IMAGE_PATH,
            is_jumpable=OJISAN_IS_JUMPABLE,
            id=OJISAN_ID
        )
        # TODO: 左右1マスの当たり判定ロジックを後で実装
        # TODO: スコア加算(500)・減算(500)の処理を後で実装

class StrongOjisan(Enemy):
    def __init__(self) -> None:
        # IDは一意の初期値を割り当て（ID範囲: 4~6）
        super().__init__(
            hp=STRONG_OJISAN_HP,
            damage=STRONG_OJISAN_DAMAGE,
            image_path=ENEMY_IMAGE_PATH,
            is_jumpable=STRONG_OJISAN_IS_JUMPABLE,
            id=STRONG_OJISAN_ID
        )
        # TODO: 左右1マスの当たり判定ロジックを後で実装
        # TODO: スコア加算(1000)・減算(1000)の処理を後で実装


class SmartphoneUser(Enemy):
    def __init__(self) -> None:
        # IDは一意の初期値を割り当て（ID範囲: 11~14）
        super().__init__(
            hp=SMARTPHONE_USER_HP,
            damage=SMARTPHONE_USER_DAMAGE,
            image_path=ENEMY_IMAGE_PATH,
            is_jumpable=SMARTPHONE_USER_IS_JUMPABLE,
            id=SMARTPHONE_USER_ID
        )
        # TODO: スコア加算(300)・減算(300)の処理を後で実装


class FurocanKaiwai(Enemy):
    def __init__(self) -> None:
        # IDは一意の初期値を割り当て（ID範囲: 16~19）
        super().__init__(
            hp=FUROCAN_KAIWAI_HP,
            damage=FUROCAN_KAIWAI_DAMAGE,
            image_path=ENEMY_IMAGE_PATH,
            is_jumpable=FUROCAN_KAIWAI_IS_JUMPABLE,
            id=FUROCAN_KAIWAI_ID
        )
        # TODO: 左右2マスの当たり判定およびダメージ分岐（本人20、左右5）のロジックを後で実装
        # TODO: スコア加算(1000)・減算(1000)の処理を後で実装


class CarryCasePerson(Enemy):
    def __init__(self) -> None:
        # IDは一意の初期値を割り当て（ID範囲: 21~24）
        super().__init__(
            hp=CARRY_CASE_PERSON_HP,
            damage=CARRY_CASE_PERSON_DAMAGE,
            image_path=ENEMY_IMAGE_PATH,
            is_jumpable=CARRY_CASE_PERSON_IS_JUMPABLE,
            id=CARRY_CASE_PERSON_ID
        )
        # TODO: 2マス分の当たり判定ロジックを後で実装
        # TODO: スコア加算(0)・減算(500)の処理を後で実装


class YanchaGroup(Enemy):
    def __init__(self) -> None:
        # IDは一意の初期値を割り当て（ID = 26）
        super().__init__(
            hp=YANCHA_GROUP_HP,
            damage=YANCHA_GROUP_DAMAGE,
            image_path=ENEMY_IMAGE_PATH,
            is_jumpable=YANCHA_GROUP_IS_JUMPABLE,
            id=YANCHA_GROUP_ID
        )
        # TODO: 横4マス分の当たり判定ロジックを後で実装
        # TODO: スコア加算(1000)・減算(1000)の処理を後で実装

class Civilian(Enemy):
    def __init__(self) -> None:
        # IDは一意の初期値を割り当て（ID範囲: 41~45）
        super().__init__(
            hp=CIVILIAN_HP,
            damage=CIVILIAN_DAMAGE,
            image_path=ENEMY_IMAGE_PATH,
            is_jumpable=CIVILIAN_IS_JUMPABLE,
            id=CIVILIAN_ID
        )
        # TODO: 攻撃不可（判定・ダメージロジック）を後で実装
        # TODO: スコア加算(0)・減算(500)の処理を後で実装
    