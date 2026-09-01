from System.command_change_system import CommandChangeSystem
from System.sound_system import SoundSystem


class System:
    def __init__(self):
        self.change_command_system = CommandChangeSystem()
        self.sound = SoundSystem()

    def command_update(self, input_x, input_y):
        return self.change_command_system.update(input_x, input_y)



    def play_PushButton(self):
        self.sound.play_se_push_button()

    def play_TitleBGM(self):
        self.sound.play_bgm_title()

    def set_se_volume(self, volume):
        self.sound.set_se_volume(volume)

    def set_bgm_volume(self, volume):
        self.sound.set_bgm_volume(volume)
