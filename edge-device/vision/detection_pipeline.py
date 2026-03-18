import cv2
import numpy as np
from vision.frame_capture import FrameCapture
from vision.preprocessing import apply_roi, to_hsv
from vision.color_detection import detect_colors
from vision.flash_detection import frame_diff
from vision.frequency_analysis import FrequencyAnalyzer
from config.settings import MIN_AREA, PERSISTENCE_FRAMES

class DetectionPipeline:
    def __init__(self):
        self.capture = FrameCapture()
        self.prev_frame = None
        self.freq = FrequencyAnalyzer()
        self.persistence = 0
        self.last_confirmed = False

    def process_frame(self):
        frame = self.capture.get_frame()
        if frame is None:
            return {"detected": False}

        roi = apply_roi(frame)
        hsv = to_hsv(roi)
        mask = detect_colors(hsv)

        h, s, v = cv2.split(hsv)
        bright_mask = cv2.inRange(v, 150, 255)
        mask = cv2.bitwise_and(mask, bright_mask)

        diff = frame_diff(self.prev_frame, roi)
        self.prev_frame = roi.copy()

        if diff is None:
            return {"detected": False}

        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)

        combined = cv2.bitwise_and(mask, thresh)

        contours, _ = cv2.findContours(combined, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        detected = False

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > MIN_AREA and area<5000:
                detected = True
                #print("Detected:", detected, "Freq:", frequency)
                break

        self.freq.update(detected)
        frequency = self.freq.get_frequency()
        #print("Detected:", detected, "Freq:", round(frequency, 2))

        if detected:
            self.persistence += 1
        else:
            self.persistence = max(0, self.persistence - 0.5)
        self.persistence= max(0, self.persistence) 

        confirmed = self.persistence > PERSISTENCE_FRAMES 

        if confirmed and not self.last_confirmed:
             print("🚑 Emergency detected | Freq:", round(frequency, 2))

        self.last_confirmed= confirmed

        cv2.imshow("ROI", roi)
        cv2.imshow("Mask", mask)
        cv2.imshow("Flash", combined)

        cv2.putText(roi, f"Pers: {int(self.persistence)}", (10,20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)

        cv2.putText(roi, f"Freq: {round(frequency,2)}", (10,40),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)

        cv2.putText(roi, f"Detected: {confirmed}", (10,60),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)

        return {
         "detected": confirmed,
         "frequency": round(frequency, 2),
         "confidence": min(1.0, frequency / 5),
         "type": "Emergency Vehicle",
         "frame": roi
        }