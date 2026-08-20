import pygame

from System.file_load_system import load_audio, load_bgm
from Domain.asset_paths import (
    DECIDE_BUTTON_SOUND_PATH,
    BGM_PATH,
)


class SoundSystem:
    def __init__(self):
        # 効果音をロードする
        self.sounds = {
            "push_button": load_audio(DECIDE_BUTTON_SOUND_PATH),
        }

        # BGMのパスを管理する
        self.bgms = {
            "title": BGM_PATH,
        }

        # 効果音とBGMの初期音量
        self.se_volume = 1.0
        self.bgm_volume = 1.0

    def set_se_volume(self, volume):
        # 音量が0.0～1.0の範囲内の場合のみ変更する
        if 0.0 <= volume <= 1.0:
            self.se_volume = volume

    def set_bgm_volume(self, volume):
        # 音量が0.0～1.0の範囲内の場合のみ変更する
        if 0.0 <= volume <= 1.0:
            self.bgm_volume = volume
            pygame.mixer.music.set_volume(self.bgm_volume)

    def play_se_push_button(self):
        # ボタン押下時の効果音を取得する
        sound = self.sounds["push_button"]

        # 効果音の音量を設定する
        sound.set_volume(self.se_volume)

        # 効果音を再生する
        sound.play()

    def play_bgm_title(self):
        # タイトル画面用のBGMをロードする
        load_bgm(self.bgms["title"])

        # BGMの音量を設定する
        pygame.mixer.music.set_volume(self.bgm_volume)

        # BGMをループ再生する
        pygame.mixer.music.play(-1)

    def stop_bgm(self):
        # BGMを停止する
        pygame.mixer.music.stop()

    def pause_bgm(self):
        # BGMを一時停止する
        pygame.mixer.music.pause()

    def resume_bgm(self):
        # 一時停止したBGMを再開する
        pygame.mixer.music.unpause()