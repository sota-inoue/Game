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
        self._image_path: Path | None = None
        self._x: int = 0
        self._y: int = 0
        self._width: int = 0
        self._height: int = 0

    def get_object_type(self) -> ObjectType:
        return self._object_type

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


class Attack(StageObject):
    def __init__(self, x : int, y : int, width : int, height : int, image_path : str) -> None:
        super().__init__(object_type=ObjectType.ATTACK)
        self.set_x(x)
        self.set_y(y)
        self.set_width(width)
        self.set_height(height)
        self.set_image_path(image_path)

