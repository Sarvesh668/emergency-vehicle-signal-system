import time
from signal_control.gpio_controller import set_green, reset_signal

class SignalLogic:
    def __init__(self):
        self.last_trigger = 0
        self.cooldown = 10

    def should_trigger(self):
        return time.time() - self.last_trigger > self.cooldown

    def trigger(self):
        print("Emergency detected → Switching signal")
        set_green()
        time.sleep(5)
        reset_signal()
        self.last_trigger = time.time()