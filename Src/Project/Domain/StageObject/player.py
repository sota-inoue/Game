from Domain.StageObject.stage_object import StageObject, ObjectType

from Domain.asset_paths import PLAYER_IMAGE_PATH

class Player(StageObject):
    def __init__(self, width) -> None:
        super().__init__(object_type = ObjectType.PLAYER)
        
        self.set_image_path(PLAYER_IMAGE_PATH)

        player_width = width // 10
        player_height = player_width * 5 // 3
        self.set_width(player_width)
        self.set_height(player_height)

        self._urgency_level: int = 0
        self._player_grid_x: int = 0
        self._player_grid_y: int = 0

        

    # urgency_level
    def get_urgency_level(self):
        return self.urgency_level
    
    def set_urgency_level(self, urgency_level: int):
        if not isinstance(urgency_level, int):
            raise TypeError(f"受け取った値: {type(urgency_level).__name__}: int型を指定してください。")
    
        if urgency_level < 0:
            urgency_level = 0
        elif urgency_level > 100:
            urgency_level = 100
    
        self.urgency_level = urgency_level

    # _player_grid_xのgetterとsetter
    def get_player_grid_x(self) -> int:
        return self._player_grid_x

    def set_player_grid_x(self, grid_x: int) -> None:
        if not isinstance(grid_x, int):
            raise TypeError(f"受け取った型 {type(grid_x).__name__} : int型を指定してください。")
        if grid_x < 0:
            grid_x = 0
        elif grid_x > 4:
            grid_x = 4
        self._player_grid_x = grid_x


    # _player_grid_yのgetterとsetter
    def get_player_grid_y(self) -> int:
        return self._player_grid_y

    def set_player_grid_y(self, grid_y: int) -> None:
        if not isinstance(grid_y, int):
            raise TypeError(f"受け取った型 {type(grid_y).__name__} : int型を指定してください。")
        if grid_y < 0:
            grid_y = 0
        elif grid_y > 1:
            grid_y = 1
        self._player_grid_y = grid_y