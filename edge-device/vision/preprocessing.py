import cv2

def apply_roi(frame):
    h, w, _ = frame.shape
    return frame[int(h/2):h, :]

def to_hsv(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)