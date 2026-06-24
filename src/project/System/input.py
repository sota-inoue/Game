try:
    from evdev import InputDevice, ecodes
except ImportError:
    InputDevice = None
    ecodes = None

class TouchInput:

    DEVICE = "/dev/input/event11"

    WIDTH = 480
    HEIGHT = 320

    RAW_X_MAX = 4095
    RAW_Y_MAX = 4095

    def __init__(self):
        self.touch = InputDevice(self.DEVICE)

        self.x = 0
        self.y = 0
        self.touch_down = False

    def update(self):
        try:
            for event in self.touch.read():

                if event.type == ecodes.EV_ABS:

                    if event.code == ecodes.ABS_X:
                        self.x = event.value * self.WIDTH // self.RAW_X_MAX

                    elif event.code == ecodes.ABS_Y:
                        self.y = event.value * self.HEIGHT // self.RAW_Y_MAX

                elif event.type == ecodes.EV_KEY:

                    if event.code == ecodes.BTN_TOUCH:
                        self.touch_down = bool(event.value)

                        if not self.touch_down:
                            self.x = 0
                            self.y = 0

        except BlockingIOError:
            return