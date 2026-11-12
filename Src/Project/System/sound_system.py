import pygame

from System.file_load_system import load_audio, load_bgm
import pygame

from asset_paths import (
    DECIDE_BUTTON_SOUND_PATH,
    BOSS_INTRO_SOUND,
    BOSS_DEFEAT_SOUND,
    GAMEOVER_SOUND_PATH,
    PLAYER_HIT_SOUND,
    OHUDA_THROW_SOUND,
    ENDING_SOUND,
    TITLE_BGM_PATH,
    STAGE_BGM_PATH,
    BOSS_STAGE_BGM_PATH,
)


class SoundSystem:
    def __init__(self):
        self.se_volume = 1.0
        self.bgm_volume = 1.0

        # 効果音をロードする
        self.se = {
            "decide_button": load_audio(DECIDE_BUTTON_SOUND_PATH),
            "boss_intro": load_audio(BOSS_INTRO_SOUND),
            "boss_defeat": load_audio(BOSS_DEFEAT_SOUND),
            "gameover": load_audio(GAMEOVER_SOUND_PATH),
            "player_hit": load_audio(PLAYER_HIT_SOUND),
            "ohuda_throw": load_audio(OHUDA_THROW_SOUND),
            "ending": load_audio(ENDING_SOUND),
        }

        # BGMのパスを管理する
        self.bgms = {
            "title": TITLE_BGM_PATH,
            "stage": STAGE_BGM_PATH,
            "boss": BOSS_STAGE_BGM_PATH,
        }

    def set_se_volume(self, volume):
        if 0.0 <= volume <= 1.0:
            self.se_volume = volume

    def set_bgm_volume(self, volume):
        if 0.0 <= volume <= 1.0:
            self.bgm_volume = volume
            pygame.mixer.music.set_volume(volume)

    def play_se(self, name):
        """効果音を1回再生する。"""
        sound = self.se.get(name)
        if sound is not None:
            sound.set_volume(self.se_volume)
            sound.play()

    def play_bgm(self, name, loops=-1):
        """指定したBGMを再生する。loops=-1でループ再生。"""
        path = self.bgms.get(name)
        if path is None:
            return

        pygame.mixer.music.stop()
        load_bgm(path)
        pygame.mixer.music.set_volume(self.bgm_volume)
        pygame.mixer.music.play(loops)

    def play_bgm_title(self):
        self.play_bgm("title")

    def play_bgm_stage(self):
        self.play_bgm("stage")

    def play_bgm_boss(self):
        self.play_bgm("boss")

    def stop_bgm(self):
        if pygame.mixer.get_init() is not None:
            pygame.mixer.music.stop()

    def pause_bgm(self):
        if pygame.mixer.get_init() is not None:
            pygame.mixer.music.pause()

    def resume_bgm(self):
        if pygame.mixer.get_init() is not None:
            pygame.mixer.music.unpause()

    # 効果音を名前付きで呼び出すためのメソッド
    def play_se_decide_button(self):
        self.play_se("decide_button")

    def play_se_boss_intro(self):
        self.play_se("boss_intro")

    def play_se_boss_defeat(self):
        self.play_se("boss_defeat")

    def play_se_gameover(self):
        self.play_se("gameover")

    def play_se_player_hit(self):
        self.play_se("player_hit")

    def play_se_ohuda_throw(self):
        self.play_se("ohuda_throw")

    def play_se_ending(self):
        self.play_se("ending")