from config import TOUCH_WIDTH

def change_command(x,y):
    """入力座標からコマンドを決定する"""

    if 0 <= x < TOUCH_WIDTH // 3:
        return 1
    elif TOUCH_WIDTH // 3 <= x < TOUCH_WIDTH*2 // 3:
        return 2
    elif TOUCH_WIDTH*2 // 3 <= x <= TOUCH_WIDTH:
        return 3
    
    return 0