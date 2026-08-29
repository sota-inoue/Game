
from System.file_load_system import load_text
from Domain.asset_paths import STAGE1_PATH

class Map:
    def __init__(self):
        self.map_data = load_text(STAGE1_PATH)

    def get_map_date(self, count) -> list[int]:
        return self.map_data[(count // 5) - 1]
