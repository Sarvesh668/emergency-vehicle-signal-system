from vision.detection_pipeline import DetectionPipeline
from signal_control.signal_logic import SignalLogic
from config.settings import DEBUG
import cv2

def main():
    pipeline = DetectionPipeline()
    signal = SignalLogic()

    while True:
        # FIRST get result + frame
        result = pipeline.process_frame()
        frame = result.get("frame", None)

        # THEN display
        if DEBUG and frame is not None:
            cv2.imshow("Camera Feed", frame)

        # Detection logic
        if result["detected"]:
            if signal.should_trigger():
                signal.trigger()

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()