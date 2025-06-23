import cv2
import numpy as np
import pyautogui

# Define green HSV range
low_green = np.array([25, 52, 72])
high_green = np.array([102, 255, 255])

# Capture webcam
cap = cv2.VideoCapture(0)

prev_x, prev_y = 0, 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for natural interaction
    frame = cv2.flip(frame, 1)

    # Convert to HSV and create mask for green color
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, low_green, high_green)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            x, y, w, h = cv2.boundingRect(contour)
            center_x = x + w // 2
            center_y = y + h // 2

            # Draw bounding box and center
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(frame, (center_x, center_y), 5, (255, 0, 0), -1)

            # Movement detection
            dx = center_x - prev_x
            dy = center_y - prev_y

            # Apply threshold to avoid noise
            if abs(dx) > 20 or abs(dy) > 20:
                if abs(dx) > abs(dy):
                    if dx > 0:
                        pyautogui.press('right')
                    else:
                        pyautogui.press('left')
                else:
                    if dy < 0:
                        pyautogui.press('space')  # upward
                    else:
                        pyautogui.press('down')

            # Update previous position
            prev_x, prev_y = center_x, center_y

    # Show the frame
    cv2.imshow('frame', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()   
                                                         
              