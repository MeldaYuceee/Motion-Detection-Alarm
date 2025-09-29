🛡️ Motion Detection Alarm

A fun and practical Python project that detects motion through your webcam and triggers a simple alarm.
Perfect for students, hobbyists, or anyone interested in real-time computer vision!

✨ Features

🎥 Real-time motion detection using your webcam

🔔 Audible alarm triggers when significant movement is detected

👋 Ignores small movements like hands or lighting changes

🖼️ Visual feedback: Original, Difference, and Threshold windows

⚡ Minimal setup – just run the script and it works


🔧 How It Works

1.Captures video from the webcam

2.Converts frames to grayscale and applies Gaussian blur to reduce noise

3.Computes difference with the background frame

4.Applies a threshold to detect significant changes

5.Finds contours and ignores small movements using min_area

6.Triggers a beep if motion is detected and enough time has passed since the last alarm

7.Updates the background periodically to ignore temporary changes


   Simple, fast, and visually clear – see motion in real-time!

🖥️ Usage
1.Clone or download this repository
2.Install requirements:
        
***pip install opencv-python numpy


3.Run the script:

    cd path/to/MotionAlarm
    .venv\Scripts\activate  # if using virtual environment
    python motion_alarm.py


Watch the windows:

Camera feed 🎥

Difference frame 🔄

Threshold frame ⚪

When motion is detected:

Console prints: Motion detected! Alarm triggered!

Beep sounds 🔔

Press 'q' to exit

📦 Requirements

Python 3.x

OpenCV (pip install opencv-python)

NumPy (pip install numpy)


🌟 Why This Project is Awesome

✅ Simple but impressive – easy to understand, instant visual feedback

👨‍💻 Student-friendly – easy to read, modify, and extend

🔥 Practical – works immediately on any webcam

🧠 Learn by doing – real-time computer vision without AI or heavy models

💡 Tips & Ideas to Extend

Fine-tune min_area or threshold_value for sensitivity

Replace the beep with email or push notifications

Integrate with Raspberry Pi or other IoT devices for home automation

Add a GUI overlay for even more visual appeal