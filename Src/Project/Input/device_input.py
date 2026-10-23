# evdevライブラリはLinuxでのみ使用でき、Windowsではインポートできないため、
# ImportErrorが発生した場合でもプログラムが停止しないようにする

from collections import deque

try:
    from evdev import InputDevice, list_devices, ecodes
except ImportError:
    InputDevice = None
    list_devices = None
    ecodes = None

from config import DEVICE_NAME


def find_device():
    if InputDevice is None:
        raise RuntimeError("evdevが使用できません")

    for path in list_devices():
        device = InputDevice(path)

        if device.name == DEVICE_NAME:
            return device

        device.close()

    raise FileNotFoundError(f"{DEVICE_NAME} が見つかりません")


class DeviceInput:
    def __init__(self, device):
        self._device = device

        self._x = None
        self._y = None
        self._is_touching = False

        self._pending = False
        self._events = deque()

    def update(self):
        try:
            for event in self._device.read():

                # タッチ座標を取得する
                if event.type == ecodes.EV_ABS:
                    if event.code == ecodes.ABS_X:
                        self._x = event.value
                    elif event.code == ecodes.ABS_Y:
                        self._y = event.value

                # タッチの開始と終了を検出する
                elif event.type == ecodes.EV_KEY:
                    if event.code == ecodes.BTN_TOUCH:
                        if event.value == 1:
                            self._is_touching = True
                            self._pending = True

                        elif event.value == 0:
                            self._is_touching = False

                # イベントを確定する
                elif event.type == ecodes.EV_SYN:
                    if event.code == ecodes.SYN_REPORT:
                        self._commit()

        except BlockingIOError:
            pass

    def _commit(self):
        if self._pending and self._x is not None and self._y is not None:
            self._events.append((self._x, self._y))
            self._pending = False

    def get_input(self):
        if self._events:
            return self._events.popleft()

        return -1, -1

    def has_input(self):
        return bool(self._events)