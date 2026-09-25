from enum import Enum, auto
from pathlib import Path

class ObjectType(Enum):
    OBSTACLE = auto()
    ENEMY = auto()
    PLAYER = auto()
    ATTACK = auto()

class Object_Position_x(Enum):
    X1 = 0
    X2 = 1
    X3 = 2
    X4 = 3
    X5 = 4
    NONE = -1


class Object_Position_y(Enum):
    Y1 = 0
    Y2 = 1
    Y3 = 2
    Y4 = 3
    Y5 = 4
    Y6 = 5
    Y7 = 6
    NONE = -1

class StageObject:
    def __init__(self, object_type):
        self._object_type: ObjectType = object_type
        self._image_path: Path | None = None
        self._Object_Position_x: Object_Position_x = Object_Position_x.NONE
        self._Object_Position_y: Object_Position_y = Object_Position_y.NONE

    # _object_typeのgetterとsetter
    def set_object_type(self, object_type: ObjectType) -> None:
        if not isinstance(object_type, ObjectType):
            raise TypeError( f"受け取った型 {type(object_type).__name__} : ObjectType型を指定してください。")
        self._object_type = object_type

    def get_object_type(self) -> ObjectType:
        return self._object_type

    # _image_pathのgetterとsetter
    def get_image_path(self) -> Path:
        return self._image_path
    
    def set_image_path(self, image_path: Path | None) -> None:
        self._image_path = image_path

    # X方向の位置情報のgetterとsetter
    def get_position_x(self) -> Object_Position_x:
        return self._object_position_x

    def set_position_x(self, position_x: Object_Position_x) -> None:
        if not isinstance(position_x, Object_Position_x):
            raise TypeError(f"受け取った型 {type(position_x).__name__} : Object_Position_x型を指定してください。" )
        self._object_position_x = position_x

    # Y方向の位置情報のgetterとsetter
    def get_position_y(self) -> Object_Position_y:
        return self._object_position_y

    def set_position_y(self, position_y: Object_Position_y) -> None:
        if not isinstance(position_y, Object_Position_y):
            raise TypeError( f"受け取った型 {type(position_y).__name__} : Object_Position_y型を指定してください。")
        self._object_position_y = position_y



class Attack(StageObject):
    def __init__(self, x : int, y : int, width : int, height : int, image_path : str) -> None:
        super().__init__(object_type=ObjectType.ATTACK)
        self.set_x(x)
        self.set_y(y)
        self.set_width(width)
        self.set_height(height)
        self.set_image_path(image_path)

