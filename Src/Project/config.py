# タッチパネルのドライバの名前
DEVICE_NAME = "ADS7846 Touchscreen"

# 色
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)
YELLOW  = (255, 255, 0)
CYAN    = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY    = (128, 128, 128)
LIGHT_BLUE  = (100, 180, 255)
LIGHT_GREEN = (120, 220, 120)
ORANGE      = (255, 165, 0)
PINK        = (255, 105, 180)
PURPLE      = (128, 0, 128)
BROWN       = (139, 69, 19)
NAVY        = (0, 0, 128)

# pygameのウィンドウサイズ
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# Windows用のゲーム画面サイズ
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 450

# タッチパネルの画面サイズ
TOUCH_WIDTH = 480
TOUCH_HEIGHT = 320

# pysceenに描画する用のタッチパネルの表示位置の頂点座標
TOUCH_SCREEN_TOP_X = (SCREEN_WIDTH - TOUCH_WIDTH) // 2
TOUCH_SCREEN_TOP_Y = SCREEN_HEIGHT - TOUCH_HEIGHT - 15

# タッチパネルの最大入力値
TOUCH_X_MAX = 4095
TOUCH_Y_MAX = 4095

# ステージのレイアウト設定
STAGE_TOP_LANE_WIDTH_SCALE = 2 / 10  # 上レーンの幅（画面幅に対する割合）
STAGE_BOTTOM_LANE_WIDTH_SCALE = 9 / 10  # 下レーンの幅（画面幅に対する割合）
STAGE_TOP_LANE_VERTICAL_MARGIN_SCALE = 4 / 15  # 上レーンの上端位置（画面高さに対する割合）
STAGE_BOTTOM_LANE_VERTICAL_MARGIN_SCALE = 2 / 15  # 下レーンの下端からの余白（画面高さに対する割合）

# ボスステージのレイアウト設定
BOSS_TOP_LANE_WIDTH_SCALE = 5 / 10  # 上レーンの幅（画面幅に対する割合）
BOSS_BOTTOM_LANE_WIDTH_SCALE = 9 / 10 # 下レーンの高さ（画面高さに対する割合）
BOSS_TOP_LANE_VERTICAL_MARGIN_SCALE = 4 / 15  # 上レーンの縦方向の余白（画面高さに対する割合）
BOSS_BOTTOM_LANE_VERTICAL_MARGIN_SCALE = 4 / 15 # 下レーンの縦方向の余白（画面高さに対する割合）


# プレイヤーのサイズの比率 : 縦横比 5:3
PLAYER_WIDTH_SCALE = 1 / 8  # 横幅
PLAYER_HEIGHT_SCALE = PLAYER_WIDTH_SCALE * 5 / 3  # 高さ

# 敵のサイズの比率：縦横比 5:3
ENEMY_WIDTH_SCALE = 1 / 8  # 横幅
ENEMY_HEIGHT_SCALE = ENEMY_WIDTH_SCALE * 5 / 3  # 高さ

# 障害物のサイズの比率：縦横比 1:1
OBSTACLE_WIDTH_SCALE = 1 / 8  # 横幅
OBSTACLE_HEIGHT_SCALE = OBSTACLE_WIDTH_SCALE  # 高さ

# 攻撃物のサイズの比率：縦横比 1:1
ATTACK_WIDTH_SCALE = 1 / 16  # 横幅
ATTACK_HEIGHT_SCALE = ATTACK_WIDTH_SCALE  # 高さ


# FPS（1秒あたりの更新回数）
FPS = 8

OPENING_MOVIE_COUNT = 3 * FPS  # オープニングフェーズの継続時間（秒）
GAME_CLEAR_COUNT = 2 * FPS  # ゲームクリアフェーズの継続時間（秒）
BOSS_INTRO_COUNT = 3 * FPS  # ボス登場フェーズの継続時間（秒）
BOSS_DEFEAT_COUNT = 3 * FPS  # ボス撃破フェーズの継続時間（秒）

