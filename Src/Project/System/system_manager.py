from System.player_system import Player
from System.map_system import Map
from System.player_position_system import PositionSystem
from System.command_change_system import CommandChangeSystem
from System.collision_system import CollisionSystem
from System.progress_system import progress_system
from System.health_system import health_system
from System.sound_system import SoundSystem


class System:
    def __init__(self,DISPLAY_WIDTH, DISPLAY_HEIGHT):
        self.player_system = Player(DISPLAY_WIDTH, DISPLAY_HEIGHT)
        self.position_system = PositionSystem()
        self.change_command_system = CommandChangeSystem()
        self.collision_system = CollisionSystem()
        self.map = Map()
        self.sound = SoundSystem()

    def command_update(self, input_x, input_y):
        return self.change_command_system.update(input_x, input_y)
    
    def player_update(self):
        return self.player_system.update()

    def player_set_locate(self, command):
        self.player_system.set_locate(command)

    def map_update(self, datas, count):
        return self.map.map_update(datas, count)

    def get_map_date(self, count):
        return self.map.get_map_date(count)

    def progress_update(self, state, x, y, count):
        return progress_system(state, x, y, count)

    def player_position_update(self, command, position_x, position_y):
        return self.position_system.update(command, position_x, position_y)

    def collision_update(self, stage_data, x, y):
        return self.collision_system.check_collision(stage_data, x, y)

    def health_update(self, hp, count, collision):
        return health_system(hp, count, collision)

    def play_PushButton(self):
        self.sound.play_se_push_button()

    def play_TitleBGM(self):
        self.sound.play_bgm_title()

    def set_se_volume(self, volume):
        self.sound.set_se_volume(volume)

    def set_bgm_volume(self, volume):
        self.sound.set_bgm_volume(volume)
