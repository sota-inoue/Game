from Domein.config import (
    TOUCH_WIDTH,
    TOUCH_HEIGHT,
    TOUCH_X_MAX,
    TOUCH_Y_MAX,
    TOUCH_SCREEN_TOP_X,
    TOUCH_SCREEN_TOP_Y,
)

def driver_to_game(x, y):
        """ドライバから取得した座標をゲーム内座標に変換する"""
        if (x == -1 and y == -1):
            return -1, -1
        # 生の座標(0～4095)を画面座標(0～480)へ変換
        x = x* TOUCH_WIDTH // TOUCH_X_MAX
        # 生の座標(0～4095)を画面座標(0～320)へ変換
        y = y* TOUCH_HEIGHT // TOUCH_Y_MAX
        return x, y

def pygame_to_game(x, y):
        """Pygameから取得した座標をゲーム内座標に変換する"""
        # タッチパネル内をクリックしたかどうかを判定
        if (TOUCH_SCREEN_TOP_X <= x <= TOUCH_SCREEN_TOP_X + TOUCH_WIDTH) and (
            TOUCH_SCREEN_TOP_Y <= y <= TOUCH_SCREEN_TOP_Y + TOUCH_HEIGHT):
            # タッチ状態取得し、タッチパネル内座標へ変換
            x = x - TOUCH_SCREEN_TOP_X
            y = y - TOUCH_SCREEN_TOP_Y
            return x, y
        return -1, -1