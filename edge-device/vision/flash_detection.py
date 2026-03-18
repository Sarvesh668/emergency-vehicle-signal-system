import cv2

def frame_diff(prev, current):
    if prev is None:
        return None
    return cv2.absdiff(prev, current)