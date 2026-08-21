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

# FPS（1秒あたりの更新回数）
FPS = 10

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


