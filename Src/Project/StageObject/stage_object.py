import pygame
from enum import Enum, auto
from pathlib import Path


class ObjectType(Enum):
    OBSTACLE = auto()
    ENEMY = auto()
    PLAYER = auto()
    ATTACK = auto()

class StageObject:
    def __init__(self, object_type):
        self._object_type: ObjectType = object_type
        self._id: int = 0
        self._image_path:Path | None = None
        self._x: int = 0
        self._y: int = 0
        self._width: int = 0
        self._height: int = 0

    def get_object_type(self) -> ObjectType:
        return self._object_type

    # _idのgetterとsetter
    def get_id(self) -> int:
        return self._id

    def set_id(self, id: int) -> None:
        if not isinstance(id, int):
            raise TypeError(f"受け取った型 {type(id).__name__} : int型を指定してください。")
        self._id = id

    # _image_pathのgetterとsetter
    def get_image_path(self) -> Path:
        return self._image_path
    
    def set_image_path(self, image_path: Path | None) -> None:
        self._image_path = image_path

    # _xのgetterとsetter
    def get_x(self) -> int:
        return self._x
    
    def set_x(self, x: int) -> None:
        if not isinstance(x, int):
            raise TypeError(f"受け取った型 {type(x).__name__} : int型を指定してください。")
        self._x = x

    # _yのgetterとsetter
    def get_y(self) -> int:
        return self._y
    
    def set_y(self, y: int) -> None:
        if not isinstance(y, int):
            raise TypeError(f"受け取った型 {type(y).__name__} : int型を指定してください。")
        self._y = y

    # _widthのgetterとsetter
    def get_width(self) -> int:
        return self._width
    
    def set_width(self, width: int) -> None:
        if not isinstance(width, int):
            raise TypeError(f"受け取った型 {type(width).__name__} : int型を指定してください。")
        self._width = width

    # _heightのgetterとsetter
    def get_height(self) -> int:
        return self._height
    
    def set_height(self, height: int) -> None:
        if not isinstance(height, int):
            raise TypeError(f"受け取った型 {type(height).__name__} : int型を指定してください。")
        self._height = height


class Obstacle(StageObject):
    def __init__(self, damage : int, image_path : str, is_jumpable: bool, id: int) -> None:
        super().__init__(object_type=ObjectType.OBSTACLE)
        self._damage: int = damage
        self.set_image_path(image_path)
        self._is_jumpable: bool = is_jumpable
        self.set_id(id)

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


class Enemy(StageObject):
    def __init__(self, hp : int, damage : int, image_path : str, is_jumpable: bool, id: int) -> None:
        super().__init__(object_type=ObjectType.ENEMY)
        self._hp: int = hp
        self._damage: int = damage
        self.set_image_path(image_path)
        self._is_jumpable: bool = is_jumpable
        self.set_id(id)
        self.is_hit: bool = False

    def set_is_hit(self, is_hit: bool) -> None:
        self.is_hit = is_hit

    def get_is_hit(self) -> bool:
        return self.is_hit

    # _hpのgetterとsetter
    def get_hp(self) -> int:
        return self._hp
    
    def set_hp(self, hp: int) -> None:
        if not isinstance(hp, int):
            raise TypeError(f"受け取った型 {type(hp).__name__} : int型を指定してください。")
        self._hp = hp
    
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

class Attack(StageObject):
    def __init__(self, x : int, y : int, width : int, height : int, image_path : str) -> None:
        super().__init__(object_type=ObjectType.ATTACK)
        self.set_x(x)
        self.set_y(y)
        self.set_width(width)
        self.set_height(height)
        self.set_image_path(image_path)

