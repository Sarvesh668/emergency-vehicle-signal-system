import cv2
import numpy as np
from config.settings import *

def detect_colors(hsv):
    mask_red1 = cv2.inRange(hsv, RED_LOW_1, RED_HIGH_1)
    mask_red2 = cv2.inRange(hsv, RED_LOW_2, RED_HIGH_2)
    mask_blue = cv2.inRange(hsv, BLUE_LOW, BLUE_HIGH)

    red_mask = cv2.bitwise_or(mask_red1, mask_red2)
    combined = cv2.bitwise_or(red_mask, mask_blue)

    return combined