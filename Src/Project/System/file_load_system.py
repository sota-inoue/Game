from pathlib import Path
import pygame


def load_image(path):
    # 受け取ったパスをPathオブジェクトに変換する
    path = Path(path)
    # 指定されたパスが存在するか確認する
    if not path.exists():
        raise FileNotFoundError(f"パスが存在しません: {path}")
    # 指定されたパスが画像ファイルであるか確認する
    if not path.is_file():
        raise FileNotFoundError(f"画像ファイルではありません: {path}")
    try:
        # 画像を読み込み、透過情報を保持した形式に変換して返す
        return pygame.image.load(path).convert_alpha()
    except pygame.error:
        # Pygameで画像の読み込みに失敗した場合
        print(f"画像の読み込みに失敗しました: {path}")
        raise


def load_audio(path):
    # 受け取ったパスをPathオブジェクトに変換する
    path = Path(path)
    # 指定されたパスが存在するか確認する
    if not path.exists():
        raise FileNotFoundError(f"パスが存在しません: {path}")
    # 指定されたパスが音声ファイルであるか確認する
    if not path.is_file():
        raise FileNotFoundError(f"音声ファイルではありません: {path}")
    try:
        # 音声ファイルをSoundオブジェクトとして読み込んで返す
        return pygame.mixer.Sound(path)
    except pygame.error:
        # Pygameで音声の読み込みに失敗した場合
        print(f"音声の読み込みに失敗しました: {path}")
        raise


def load_bgm(path):
    # 受け取ったパスをPathオブジェクトに変換する
    path = Path(path)
    # 指定されたパスが存在するか確認する
    if not path.exists():
        raise FileNotFoundError(f"パスが存在しません: {path}")
    # 指定されたパスが音声ファイルであるか確認する
    if not path.is_file():
        raise FileNotFoundError(f"音声ファイルではありません: {path}")
    try:
        # BGMとして使用する音声ファイルを読み込む
        pygame.mixer.music.load(path)
    except pygame.error:
        # PygameでBGMの読み込みに失敗した場合
        print(f"BGMの読み込みに失敗しました: {path}")
        raise
    

def load_text(path):
    # 受け取ったパスをPathオブジェクトに変換する
    path = Path(path)
    # 指定されたパスが存在するか確認する
    if not path.exists():
        raise FileNotFoundError(f"パスが存在しません: {path}")
    # 指定されたパスがテキストファイルであるか確認する
    if not path.is_file():
        raise FileNotFoundError(f"テキストファイルではありません: {path}")
    try:
        # UTF-8形式でテキストファイルを開く
        with path.open("r", encoding="utf-8") as file:
            # 空行を除外し、各行の値を整数に変換して二次元配列として返す
            return [
                [int(x) for x in line.split()]
                for line in file
                if line.strip()
            ]
    except (OSError, ValueError):
        # ファイルの読み込み、または整数への変換に失敗した場合
        print(f"テキストファイルの読み込みに失敗しました: {path}")
        raise