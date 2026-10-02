from enum import Enum, auto

class ObjectType(Enum):
    OBSTACLE = auto()
    ENEMY = auto()


class StageObject:
    def __init__(self, object_type, path, id, size, is_jumpable, damage):
        self._object_type: ObjectType = object_type
        self._image_path: str = path
        self._id: int = id
        self._width_size: int = size
        self._is_jumpable: bool = is_jumpable
        self._damage: int = damage

        self._is_draw: bool = True

    def get_object_type(self) -> ObjectType:
        return self._object_type
    
    def get_image_path(self) -> str:
        return self._image_path

    def get_id(self) -> int:
        return self._id

    def get_width_size(self) -> int:
        return self._width_size

    def get_is_jumpable(self) -> bool:
        return self._is_jumpable

    def get_damage(self) -> int:
        return self._damage

    def set_is_draw(self, is_draw: bool) -> None:
        self._is_draw = is_draw

    def get_is_draw(self) -> bool:
        return self._is_draw

