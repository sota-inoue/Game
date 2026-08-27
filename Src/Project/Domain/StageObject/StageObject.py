import pygame
from enum import Enum, auto


class ObjectType(Enum):
    OBSTACLE = auto()
    ENEMY = auto()

class StageObject:
    def __init__(self, object_type):
        self._object_type: ObjectType = object_type
        self._image_path: str = ""
        self._x: int = 0
        self._y: int = 0
        self._width: int = 0
        self._height: int = 0

    # _image_pathのgetterとsetter
    def get_image_path(self) -> str:
        return self._image_path
    
    def set_image_path(self, image_path: str) -> None:
        if not isinstance(image_path, str):
            raise TypeError(f"受け取った型 {type(image_path).__name__} : str型を指定してください。")
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
    def __init__(self, hp : int, damage : int, image_path : str) -> None:
        super().__init__(object_type=ObjectType.OBSTACLE)
        self._hp: int = hp
        self._damage: int = damage
        self.set_image_path(image_path)

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


class Enemy(StageObject):
    def __init__(self, hp : int, damage : int, image_path : str) -> None:
        super().__init__(object_type=ObjectType.ENEMY)
        self._hp: int = hp
        self._damage: int = damage
        self.set_image_path(image_path)

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

    
