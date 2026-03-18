import cv2
from config.settings import FRAME_WIDTH, FRAME_HEIGHT

class FrameCapture:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))
        return frame