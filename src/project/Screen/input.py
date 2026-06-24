from evdev import InputDevice, ecodes

class TouchInput:
    
    DEVICE = "/dev/input/event11"

    def __init__(self):
        self.touch = InputDevice(self.DEVICE)

        self.x = 0
        self.y = 0
        self.touch_down = False

    def update(self):
        self.touch_down = False

        try:
            events = self.touch.read()

        except BlockingIOError:
            return

        for event in events:

            if event.type == ecodes.EV_ABS:

                if event.code == ecodes.ABS_X:
                    self.x = event.value

                elif event.code == ecodes.ABS_Y:
                    self.y = event.value

            elif event.type == ecodes.EV_KEY:

                if event.code == ecodes.BTN_TOUCH:
                    self.touch_down = bool(event.value)