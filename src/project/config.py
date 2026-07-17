
# タッチパネルのドライバの名前
DEVICE_NAME = "ADS7846 Touchscreen"

# 背景色（黒）
BACK_COLOR = (0, 0, 0)

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