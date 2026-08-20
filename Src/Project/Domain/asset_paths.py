from pathlib import Path

# パスの設定

BASE_DIR = Path(__file__).resolve().parent.parent / "Assets"

STAGE1_PATH = BASE_DIR / "Map" / "stage1.txt"

PLAYER_IMAGE_PATH = BASE_DIR / "Image" / "Player" / "player.png"
ENEMY_IMAGE_PATH = BASE_DIR / "Image" / "Enemy" / "office_worker.png"
OBSTACLE_IMAGE_PATH = BASE_DIR / "Image" / "Obstacle" / "banana.png"

DECIDE_BUTTON_SOUND_PATH = BASE_DIR / "Sound" / "Se" / "decide_button.mp3"
BGM_PATH = BASE_DIR / "Sound" / "Bgm" / "Morning.mp3"