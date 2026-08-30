from System.player_system import Player
from System.player_position_system import PositionSystem
from System.command_change_system import CommandChangeSystem
from System.sound_system import SoundSystem


class System:
    def __init__(self,DISPLAY_WIDTH, DISPLAY_HEIGHT):
        self.player_system = Player(DISPLAY_WIDTH, DISPLAY_HEIGHT)
        self.position_system = PositionSystem()
        self.change_command_system = CommandChangeSystem()
        
        self.sound = SoundSystem()

    def command_update(self, input_x, input_y):
        return self.change_command_system.update(input_x, input_y)
    
    def player_update(self):
        return self.player_system.update()

    def player_set_locate(self, command):
        self.player_system.set_locate(command)

    def player_position_update(self, command, position_x, position_y):
        return self.position_system.update(command, position_x, position_y)




    def play_PushButton(self):
        self.sound.play_se_push_button()

    def play_TitleBGM(self):
        self.sound.play_bgm_title()

    def set_se_volume(self, volume):
        self.sound.set_se_volume(volume)

    def set_bgm_volume(self, volume):
        self.sound.set_bgm_volume(volume)
