import cv2
import numpy as np
import time
import winsound

camera_index = 0
camera = cv2.VideoCapture(camera_index)

min_area = 5000
threshold_value = 30
alarm_duration = 500
alarm_frequency = 1000
wait_time = 5
background_update_interval = 5

ret, frame = camera.read()
if not ret:
    print("Camera could not be opened!")
    exit()

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (21, 21), 0)
background = gray

last_alarm = 0
last_background_update = time.time()

print("Program started... Press 'q' to quit.")

while True:
    ret, frame = camera.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    difference = cv2.absdiff(background, gray)
    _, thresh = cv2.threshold(difference, threshold_value, 255, cv2.THRESH_BINARY)
    thresh = cv2.dilate(thresh, None, iterations=2)

    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected = False
    for contour in contours:
        if cv2.contourArea(contour) < min_area:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        motion_detected = True

    if motion_detected and (time.time() - last_alarm > wait_time):
        winsound.Beep(alarm_frequency, alarm_duration)
        print("Motion detected! Alarm triggered 🚨")
        last_alarm = time.time()

    if time.time() - last_background_update > background_update_interval:
        background = gray
        last_background_update = time.time()

    status_text = "Motion: YES" if motion_detected else "Motion: NO"
    cv2.putText(frame, status_text, (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    cv2.imshow("Camera", frame)
    cv2.imshow("Difference", difference)
    cv2.imshow("Threshold", thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
