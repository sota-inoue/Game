# evdevライブラリはLinuxでのみ使用でき、Windowsではインポートできないため、
# ImportErrorが発生した場合でもプログラムが停止しないようにする
try:
    from evdev import InputDevice, list_devices, ecodes
except ImportError:
    InputDevice = None
    list_devices = None
    ecodes = None

from config import DEVICE_NAME


def find_device():
    # evdevが使用できない環境では、入力デバイスを使用しない
    if InputDevice is None or list_devices is None:
        return None

    # 接続されている入力デバイスを順番に調べる
    for path in list_devices():
        # eventXに対応する入力デバイスの情報を取得する
        device = InputDevice(path)

        # 指定したデバイス名と一致した場合、そのデバイスを返す
        if device.name == DEVICE_NAME:
            return device

    # タッチパネルが見つからなかった場合
    raise FileNotFoundError(f"{DEVICE_NAME} が見つかりません")

def device_input(touch):
    # 必ず最初に初期化する
    x, y = -1, -1

    try:
        for event in touch.read():

            if event.type == ecodes.EV_ABS:
                if event.code == ecodes.ABS_X:
                    x = event.value

                elif event.code == ecodes.ABS_Y:
                    y = event.value

            elif (event.type == ecodes.EV_KEY and event.code == ecodes.BTN_TOUCH ):
                if not bool(event.value):
                    x, y = -1, -1

        return x, y

    except BlockingIOError:
        return -1, -1