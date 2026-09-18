#StageObject/enemy.py
from StageObject.stage_object import Enemy

from Domain.object_parameters import(
    OJISAN_HP,
    OJISAN_DAMAGE,
    OJISAN_IS_JUMPABLE,
    OJISAN_ID,
    OJISAN_ADD_SCORE,
    OJISAN_SUB_SCORE,
    STRONG_OJISAN_HP,
    STRONG_OJISAN_DAMAGE,
    STRONG_OJISAN_IS_JUMPABLE,
    STRONG_OJISAN_ID,
    STRONG_OJISAN_ADD_SCORE,
    STRONG_OJISAN_SUB_SCORE,
    SMARTPHONE_USER_HP,
    SMARTPHONE_USER_DAMAGE,
    SMARTPHONE_USER_IS_JUMPABLE,
    SMARTPHONE_USER_ID,
    SMARTPHONE_USER_ADD_SCORE,
    SMARTPHONE_USER_SUB_SCORE,
    FUROCAN_KAIWAI_HP,
    FUROCAN_KAIWAI_DAMAGE,
    FUROCAN_KAIWAI_IS_JUMPABLE,
    FUROCAN_KAIWAI_ID,
    FUROCAN_KAIWAI_ADD_SCORE,
    FUROCAN_KAIWAI_SUB_SCORE,
    CARRY_CASE_PERSON_HP,
    CARRY_CASE_PERSON_DAMAGE,
    CARRY_CASE_PERSON_IS_JUMPABLE,
    CARRY_CASE_PERSON_ID,
    CARRY_CASE_PERSON_ADD_SCORE,
    CARRY_CASE_PERSON_SUB_SCORE,
    YANCHA_GROUP_HP,
    YANCHA_GROUP_DAMAGE,
    YANCHA_GROUP_IS_JUMPABLE,
    YANCHA_GROUP_ID,
    YANCHA_GROUP_ADD_SCORE,
    YANCHA_GROUP_SUB_SCORE,
    CIVILIAN_HP,
    CIVILIAN_DAMAGE,
    CIVILIAN_IS_JUMPABLE,
    CIVILIAN_ID,
    CIVILIAN_ADD_SCORE,
    CIVILIAN_SUB_SCORE
)

from Domain.asset_paths import (
    OJISAN_IMAGE_PATH,
    STRONG_OJISAN_IMAGE_PATH,
    SMARTPHONE_USER_IMAGE_PATH,
    FUROCAN_KAIWAI_IMAGE_PATH,
    CARRY_CASE_PERSON_IMAGE_PATH,
    YANCHA_GROUP_IMAGE_PATH,
    CIVILIAN_IMAGE_PATH,
)

class Ojisan(Enemy):
    def __init__(self) -> None:
        # IDは一意の初期値を割り当て（ID範囲: 1~3）
        # 初期値のIDを割り当て（後で見た目バリエーション用に複数ID選択可能にする予定）
        super().__init__(
            hp=OJISAN_HP,
            damage=OJISAN_DAMAGE,
            image_path=OJISAN_IMAGE_PATH,
            is_jumpable=OJISAN_IS_JUMPABLE,
            id=OJISAN_ID,
            add_score=OJISAN_ADD_SCORE,
            sub_score=OJISAN_SUB_SCORE
        )
        # TODO: 左右1マスの当たり判定ロジックを後で実装

class StrongOjisan(Enemy):
    def __init__(self) -> None:
        # IDは一意の初期値を割り当て（ID範囲: 4~6）
        super().__init__(
            hp=STRONG_OJISAN_HP,
            damage=STRONG_OJISAN_DAMAGE,
            image_path=STRONG_OJISAN_IMAGE_PATH,
            is_jumpable=STRONG_OJISAN_IS_JUMPABLE,
            id=STRONG_OJISAN_ID,
            add_score=STRONG_OJISAN_ADD_SCORE,
            sub_score=STRONG_OJISAN_SUB_SCORE
        )
        # TODO: 左右1マスの当たり判定ロジックを後で実装


class SmartphoneUser(Enemy):
    def __init__(self) -> None:
        # IDは一意の初期値を割り当て（ID範囲: 11~14）
        super().__init__(
            hp=SMARTPHONE_USER_HP,
            damage=SMARTPHONE_USER_DAMAGE,
            image_path=SMARTPHONE_USER_IMAGE_PATH,
            is_jumpable=SMARTPHONE_USER_IS_JUMPABLE,
            id=SMARTPHONE_USER_ID,
            add_score=SMARTPHONE_USER_ADD_SCORE,
            sub_score=SMARTPHONE_USER_SUB_SCORE
        )


class FurocanKaiwai(Enemy):
    def __init__(self) -> None:
        # IDは一意の初期値を割り当て（ID範囲: 16~19）
        super().__init__(
            hp=FUROCAN_KAIWAI_HP,
            damage=FUROCAN_KAIWAI_DAMAGE,
            image_path=FUROCAN_KAIWAI_IMAGE_PATH,
            is_jumpable=FUROCAN_KAIWAI_IS_JUMPABLE,
            id=FUROCAN_KAIWAI_ID,
            add_score=FUROCAN_KAIWAI_ADD_SCORE,
            sub_score=FUROCAN_KAIWAI_SUB_SCORE
        )
        # TODO: 左右2マスの当たり判定およびダメージ分岐（本人20、左右5）のロジックを後で実装

class CarryCasePerson(Enemy):
    def __init__(self) -> None:
        # IDは一意の初期値を割り当て（ID範囲: 21~24）
        super().__init__(
            hp=CARRY_CASE_PERSON_HP,
            damage=CARRY_CASE_PERSON_DAMAGE,
            image_path=CARRY_CASE_PERSON_IMAGE_PATH,
            is_jumpable=CARRY_CASE_PERSON_IS_JUMPABLE,
            id=CARRY_CASE_PERSON_ID,
            add_score=CARRY_CASE_PERSON_ADD_SCORE,
            sub_score=CARRY_CASE_PERSON_SUB_SCORE
        )
        # TODO: 2マス分の当たり判定ロジックを後で実装


class YanchaGroup(Enemy):
    def __init__(self) -> None:
        # IDは一意の初期値を割り当て（ID = 26）
        super().__init__(
            hp=YANCHA_GROUP_HP,
            damage=YANCHA_GROUP_DAMAGE,
            image_path=YANCHA_GROUP_IMAGE_PATH,
            is_jumpable=YANCHA_GROUP_IS_JUMPABLE,
            id=YANCHA_GROUP_ID,
            add_score=YANCHA_GROUP_ADD_SCORE,
            sub_score=YANCHA_GROUP_SUB_SCORE
        )
        # TODO: 横4マス分の当たり判定ロジックを後で実装

class Civilian(Enemy):
    def __init__(self) -> None:
        # IDは一意の初期値を割り当て（ID範囲: 41~45）
        super().__init__(
            hp=CIVILIAN_HP,
            damage=CIVILIAN_DAMAGE,
            image_path=CIVILIAN_IMAGE_PATH,
            is_jumpable=CIVILIAN_IS_JUMPABLE,
            id=CIVILIAN_ID,
            add_score=CIVILIAN_ADD_SCORE,
            sub_score=CIVILIAN_SUB_SCORE
        )
        # TODO: 攻撃不可（判定・ダメージロジック）を後で実装
    