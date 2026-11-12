import math

import cv2

from System.file_load_system import load_video

from config import FPS

from asset_paths import OPNING_VIDEO_PATH, BOSS_INTRO_VIDEO_PATH, BOSS_DEFEAT_VIDEO_PATH, ENDING_VIDEO_PATH

import pygame


class VideoManager:
    def __init__(self, width, height):

        self._width = width
        self._height = height
        self._fps = FPS

        # 動画をロード
        self._opening_video = load_video(OPNING_VIDEO_PATH)
        self._boss_intro_video = load_video(BOSS_INTRO_VIDEO_PATH)
        self._boss_defeat_video = load_video(BOSS_DEFEAT_VIDEO_PATH)
        self._ending_video = load_video(ENDING_VIDEO_PATH)

        # 動画を画像配列に変換
        self._opening_video_images = self.set_up_videos(self._opening_video)
        self._boss_intro_video_images = self.set_up_videos(self._boss_intro_video)
        self._boss_defeat_video_images = self.set_up_videos(self._boss_defeat_video)
        self._ending_video_images = self.set_up_videos(self._ending_video)


    def get_opening_video_image(self, count: int):
        if 0 <= count < len(self._opening_video_images):
            return self._opening_video_images[count]
        return -1

    def get_boss_intro_video_image(self, count: int):
        if 0 <= count < len(self._boss_intro_video_images):
            return self._boss_intro_video_images[count]
        return -1

    def get_boss_defeat_video_image(self, count: int):
        if 0 <= count < len(self._boss_defeat_video_images):
            return self._boss_defeat_video_images[count]
        return -1

    def get_ending_video_image(self, count: int):
        if 0 <= count < len(self._ending_video_images):
            return self._ending_video_images[count]
        return -1

    
    def set_up_videos(self, video):

        # 動画情報を取得
        video_fps = video.get(cv2.CAP_PROP_FPS)
        frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

        if video_fps <= 0 or frame_count <= 0 or self._fps <= 0:
            video.release()
            raise ValueError("動画情報が不正です")

        # 動画の再生時間
        duration = frame_count / video_fps

        # ゲームFPSに合わせた必要フレーム数
        required_frames = math.ceil(duration * self._fps)

        images = []
        current_frame = -1
        last_image = None

        try:
            for count in range(required_frames):

                # 保存する動画フレーム番号
                target_frame = min(int(count * video_fps / self._fps), frame_count - 1)

                # 必要なフレームまで順番に進める
                while current_frame < target_frame:

                    if not video.grab():
                        return images

                    current_frame += 1

                # 同じフレームを再利用する場合
                if last_image is not None and target_frame == previous_frame:
                    images.append(last_image)
                    continue

                # 現在のフレームを取得
                ret, frame = video.retrieve()

                if not ret:
                    break

                # 画面サイズに変更
                frame = cv2.resize(frame, (self._width, self._height))
                # BGR → RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Pygame Surfaceに変換
                image = pygame.image.frombuffer(frame.tobytes(), (self._width, self._height), "RGB")
                images.append(image)

                last_image = image
                previous_frame = target_frame

        finally:
            video.release()

        return images