# src/project/Load/sound_loader.py
"""
【呼び出しイメージ】
ゲームの各処理（System や GameController など）からこのクラスを受け取り、以下のように使用します。

例1: 効果音（SE）の再生（CollisionHandler や System 内）
--------------------------------------------------
# ダメージ音の再生
sound_loader.play_se("damage/damage.wav")

# 決定音の再生（音量を個別に指定する場合）
sound_loader.play_se("decision/decision.wav", volume=0.8)
--------------------------------------------------

例2: BGMの再生・停止（StageSystem や GameController 内）
--------------------------------------------------
# ステージBGMのループ再生（1000msかけてフェードイン）
sound_loader.play_bgm("bgm/stage1.mp3", loop=-1, fade_ms=1000)

# BGMの停止（500msかけてフェードアウト）
sound_loader.stop_bgm(fade_ms=500)
--------------------------------------------------
"""

import os
from typing import Dict, Optional
import pygame


class SoundManager:
    """
    Assets/Sound/ 内の音声ファイル（SE・BGM）の読み込み・保持・再生管理を行うクラス
    """

    def __init__(self, base_dir: Optional[str] = None):
        # 読み込んだSE（効果音）を保持するキャッシュ: { "相対パス": pygame.mixer.Sound }
        self._se_cache: Dict[str, pygame.mixer.Sound] = {}

        # 音量設定 (0.0 〜 1.0)
        self._se_volume: float = 1.0
        self._bgm_volume: float = 1.0

        # Pygame ミキサーの初期化確認（メイン等で未初期化の場合への対策）
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        # 音声ファイルが格納されているルートディレクトリ（Assets/Sound/）のパスを設定
        if base_dir is None:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # Load/ から見て 2つ上の src/project/Assets/Sound を指す
            self._base_dir = os.path.normpath(
                os.path.join(current_dir, "..", "Assets", "Sound")
            )
        else:
            self._base_dir = base_dir

    # --- SE（効果音）関連処理 ---

    def play_se(self, relative_path: str, volume: Optional[float] = None) -> None:
        """
        効果音（SE）を再生する。未ロードの場合は自動でロードしてキャッシュする。

        :param relative_path: Assets/Sound からの相対パス (例: "damage/damage.wav")
        :param volume: 個別指定したい場合の音量 (0.0 〜 1.0)
        """
        sound = self._get_se(relative_path)
        if sound is None:
            return

        # 音量設定
        play_volume = volume if volume is not None else self._se_volume
        sound.set_volume(play_volume)
        sound.play()

    def _get_se(self, relative_path: str) -> Optional[pygame.mixer.Sound]:
        """指定パスのSEをキャッシュまたは新規読み込みで取得する"""
        formatted_path = relative_path.replace("\\", "/")

        if formatted_path in self._se_cache:
            return self._se_cache[formatted_path]

        full_path = os.path.join(self._base_dir, formatted_path)

        if not os.path.exists(full_path):
            print(f"[Warning] SEファイルが見つかりません: {full_path}")
            return None

        try:
            sound = pygame.mixer.Sound(full_path)
            self._se_cache[formatted_path] = sound
            return sound
        except Exception as e:
            print(f"[Error] SEの読み込みに失敗しました ({full_path}): {e}")
            return None

    # --- BGM（背景音楽）関連処理 ---

    def play_bgm(self, relative_path: str, loop: int = -1, fade_ms: int = 0) -> None:
        """
        BGM（背景音楽）をストリーミング再生する。

        :param relative_path: Assets/Sound からの相対パス (例: "bgm/stage1.mp3")
        :param loop: ループ回数 (-1 で無限ループ)
        :param fade_ms: フェードイン時間（ミリ秒）
        """
        formatted_path = relative_path.replace("\\", "/")
        full_path = os.path.join(self._base_dir, formatted_path)

        if not os.path.exists(full_path):
            print(f"[Warning] BGMファイルが見つかりません: {full_path}")
            return

        try:
            pygame.mixer.music.load(full_path)
            pygame.mixer.music.set_volume(self._bgm_volume)
            pygame.mixer.music.play(loops=loop, fade_ms=fade_ms)
        except Exception as e:
            print(f"[Error] BGMの再生に失敗しました ({full_path}): {e}")

    def stop_bgm(self, fade_ms: int = 0) -> None:
        """
        BGMを停止する。

        :param fade_ms: フェードアウト時間（ミリ秒）
        """
        if fade_ms > 0:
            pygame.mixer.music.fadeout(fade_ms)
        else:
            pygame.mixer.music.stop()

    def pause_bgm(self) -> None:
        """BGMを一時停止する"""
        pygame.mixer.music.pause()

    def unpause_bgm(self) -> None:
        """一時停止したBGMを再開する"""
        pygame.mixer.music.unpause()

    # --- 音量一括変更処理 ---

    def set_se_volume(self, volume: float) -> None:
        """全体SE音量を設定する (0.0 〜 1.0)"""
        self._se_volume = max(0.0, min(1.0, volume))

    def set_bgm_volume(self, volume: float) -> None:
        """BGM音量を設定する (0.0 〜 1.0)"""
        self._bgm_volume = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(self._bgm_volume)

    def clear_cache(self) -> None:
        """保持しているSEのキャッシュを消去する"""
        self._se_cache.clear()