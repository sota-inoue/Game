# evdevライブラリはLinuxでのみ使用でき、Windowsではインポートできないため、
# ImportErrorが発生した場合でもプログラムが停止しないようにする
try:
    from evdev import InputDevice, list_devices, ecodes
except ImportError:
    InputDevice = None
    list_devices = None
    ecodes = None

class TouchInput:
    # タッチパネルのデバイス名
    DEVICE_NAME = "ADS7846 Touchscreen"
    # タッチパネルの画面サイズ
    WIDTH = 480
    HEIGHT = 320
    # タッチパネルの最大入力値
    RAW_X_MAX = 4095
    RAW_Y_MAX = 4095

    def __init__(self):
        # タッチパネルデバイスを取得する
        self.touch = self.find_device()
        # タッチ座標
        self.x = 0
        self.y = 0
        # タッチされているかどうか
        self.touch_down = False

    def find_device(self):
        if InputDevice is None or list_devices is None:
            return None
        # 接続されている入力デバイス(/dev/input/event0～eventX)を順番に調べる
        for path in list_devices():
            # eventXに対応する入力デバイスの情報を取得する
            device = InputDevice(path)
            # デバイス名が「ADS7846 Touchscreen」であれば、
            # このeventXをタッチパネルの入力デバイスとして使用する
            if device.name == self.DEVICE_NAME:
                return device
        # タッチパネルの入力デバイスが見つからなかった場合のエラー処理
        raise FileNotFoundError("ADS7846 Touchscreen が見つかりません")

    def update(self):
        try:
            # タッチパネルから発生したイベントを取得する
            for event in self.touch.read():
                # イベントの種類が座標についての場合の処理
                if event.type == ecodes.EV_ABS:
                    # X座標
                    if event.code == ecodes.ABS_X:
                        # 生の座標(0～4095)を画面座標(0～480)へ変換
                        self.x = event.value * self.WIDTH // self.RAW_X_MAX
                    # Y座標
                    elif event.code == ecodes.ABS_Y:
                        # 生の座標(0～4095)を画面座標(0～320)へ変換
                        self.y = event.value * self.HEIGHT // self.RAW_Y_MAX
                # イベントの種類がタッチのON/OFFについての場合の処理
                elif event.type == ecodes.EV_KEY and event.code == ecodes.BTN_TOUCH:
                    # タッチされているかどうかを確認
                    self.touch_down = bool(event.value)
                    # タッチパネルから指を離していた場合に座標をリセットする
                    if not self.touch_down:
                        self.x = 0
                        self.y = 0
        # イベントが無い場合は何もしない
        except BlockingIOError:
            return
        
        