# 🚦 Vision-Based Emergency Vehicle Detection System

## 📌 Overview
A real-time edge-based traffic signal control system that detects emergency vehicles using computer vision and prioritizes traffic signals.

## 🧠 Features
- Red/Blue flashing light detection (OpenCV)
- Real-time processing on Raspberry Pi
- Frequency-based validation
- Traffic signal control via GPIO
- False positive reduction using:
  - HSV filtering
  - Frame differencing
  - Temporal persistence

## ⚙️ Tech Stack
- Python
- OpenCV
- Raspberry Pi
- (Optional) Spring Boot backend

## 🚀 How to Run
```bash
pip install -r requirements.txt
python main.py
