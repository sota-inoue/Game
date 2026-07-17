# evdevライブラリはLinuxでのみ使用でき、Windowsではインポートできないため、
# ImportErrorが発生した場合でもプログラムが停止しないようにする
try:
    from evdev import ecodes
except ImportError:
    InputDevice = None
    list_devices = None
    ecodes = None

from config import DEVICE_NAME

def find_device():
    if InputDevice is None or list_devices is None:
        return None
    # 接続されている入力デバイス(/dev/input/event0～eventX)を順番に調べる
    for path in list_devices():
        # eventXに対応する入力デバイスの情報を取得する
        device = InputDevice(path)
        # デバイス名が「ADS7846 Touchscreen」であれば、
        # このeventXをタッチパネルの入力デバイスとして使用する
        if device.name == DEVICE_NAME:
            return device
    # タッチパネルの入力デバイスが見つからなかった場合のエラー処理
    raise FileNotFoundError(f"{DEVICE_NAME} が見つかりません")

def device_input(touch):
        try:
            # タッチパネルから発生したイベントを取得する
            for event in touch.read():
                # イベントの種類が座標についての場合の処理
                if event.type == ecodes.EV_ABS:
                    # X座標
                    if event.code == ecodes.ABS_X:
                        x = event.value
                    # Y座標
                    elif event.code == ecodes.ABS_Y:
                        y = event.value
                # イベントの種類がタッチのON/OFFについての場合の処理
                elif event.type == ecodes.EV_KEY and event.code == ecodes.BTN_TOUCH:
                    # タッチパネルから指を離していた場合に座標をリセットする
                    if not bool(event.value):
                        x, y = -1 ,-1
            return x,y
        # イベントが無い場合は何もしない
        except BlockingIOError:
            return -1,-1