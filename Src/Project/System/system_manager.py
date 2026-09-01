from System.sound_system import SoundSystem


class System:
    def __init__(self):
        self.sound = SoundSystem()

    def play_PushButton(self) -> None:
        self.sound.play_se_push_button()

    def play_TitleBGM(self) -> None:
        self.sound.play_bgm_title()

    def set_se_volume(self, volume: int) -> None:
        self.sound.set_se_volume(volume)

    def set_bgm_volume(self, volume: int) -> None:
        self.sound.set_bgm_volume(volume)
