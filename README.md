# Motion Detection Alarm – Real-Time Webcam Monitoring

> **Domain:** Computer Vision / Real-Time Detection  
> **Level:** Beginner (Student R&D)  
> **Purpose:** Demonstrate basic motion detection and alarm triggering using Python and OpenCV

---

## 1. Background & Concept
Motion detection is a common entry point into computer vision, enabling real-time anomaly awareness through simple frame differencing and thresholding.  
This prototype detects significant movement through a webcam and raises an alarm while ignoring small, irrelevant changes such as minor lighting variation or hand movement.

---

## 2. Features
- Real-time motion detection via webcam  
- Ignore small movements using area filtering  
- Audible alarm trigger  
- Three display windows (camera, difference, threshold)  
- Minimal setup and beginner-friendly code  

---

## 3. How It Works
1. Capture video frames
2. Convert to grayscale and apply Gaussian blur
3. Compute difference with background frame
4. Threshold major changes
5. Extract contours and filter small ones
6. Trigger audible alert if change is significant
7. Update background periodically to ignore temporary shifts

The result is a simple yet effective motion alarm you can observe in real-time.

---

## 4. Installation
```bash
pip install opencv-python numpy
