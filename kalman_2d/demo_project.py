import numpy as np
import cv2 as cv
from filter import Kalman_2D

kf_x = Kalman_2D(Q=0.1, R=2, dt=0.01)
kf_y = Kalman_2D(Q=0.1, R=2, dt=0.01)
video = cv.VideoCapture("red_ball.mp4")

while True:
    ret, frame = video.read()
    #resize = cv.resize(frame, (480, 685))
    if not ret:
      break

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    #hsv = cv.cvtColor(resize, cv.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([179, 255, 255])

    # Mask red color
    mask1 = cv.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 | mask2
    # Find contours in the mask
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Proceed only if at least one contour is found
    if contours:
      largest_contour = max(contours, key=cv.contourArea)
      (x, y, w, h) = cv.boundingRect(largest_contour)
      cx = x + w // 2
      cy = y + h // 2
      kf_x.predict()
      kf_y.predict()
      kf_x.update(cx)
      kf_y.update(cy)
      pred_x = int(kf_x.x[0][0])
      pred_y = int(kf_y.x[0][0])

      # Show detection
      cv.circle(frame, (cx, cy), 5, (0, 255, 0), -1)
      cv.circle(frame, (int(pred_x), int(pred_y)), 5, (0, 0, 255), -1)         # KF predicted (red)
      #cv.circle(resize, (cx, cy), 5, (0, 255, 0), -1)
      #cv.circle(resize, (int(pred_x), int(pred_y)), 5, (0, 0, 255), -1)         # KF predicted (red)

    cv.imshow("Tracking", frame)
    #cv.imshow("Tracking", resize)
    if cv.waitKey(30) & 0xFF == ord('q'):
        break
video.release()
cv.destroyAllWindows()
