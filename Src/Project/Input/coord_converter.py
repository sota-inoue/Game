
from config import (
    TOUCH_WIDTH,
    TOUCH_HEIGHT,
    TOUCH_X_MAX,
    TOUCH_Y_MAX,
    TOUCH_SCREEN_TOP_X,
    TOUCH_SCREEN_TOP_Y,
)


def driver_to_game(x: int, y: int) -> tuple[int, int]:
    # 無効な入力を除外する
    if x < 0 or y < 0:
        return -1, -1

    # ドライバ座標をタッチ画面座標へ変換する
    x = x * TOUCH_WIDTH // TOUCH_X_MAX
    y = y * TOUCH_HEIGHT // TOUCH_Y_MAX

    # 座標を画面内に制限する
    x = max(0, min(x, TOUCH_WIDTH - 1))
    y = max(0, min(y, TOUCH_HEIGHT - 1))

    return x, y


def pygame_to_game(x: int, y: int) -> tuple[int, int]:
    # タッチ画面の範囲を判定する
    if not (
        TOUCH_SCREEN_TOP_X <= x < TOUCH_SCREEN_TOP_X + TOUCH_WIDTH
        and TOUCH_SCREEN_TOP_Y <= y < TOUCH_SCREEN_TOP_Y + TOUCH_HEIGHT
    ):
        return -1, -1

    # タッチ画面を原点とする座標へ変換する
    return x - TOUCH_SCREEN_TOP_X, y - TOUCH_SCREEN_TOP_Y
