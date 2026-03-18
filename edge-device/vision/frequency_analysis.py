import time

class FrequencyAnalyzer:
    def __init__(self):
        self.timestamps = []

    def update(self, detected):
        now = time.time()

        if detected:
            self.timestamps.append(now)

        # Keep last 3 seconds
        self.timestamps = [t for t in self.timestamps if now - t <= 3]

    def get_frequency(self):
        if len(self.timestamps) < 2:
            return 0

        duration = self.timestamps[-1] - self.timestamps[0]
        if duration == 0:
            return 0

        return len(self.timestamps) / duration