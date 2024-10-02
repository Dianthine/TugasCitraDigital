import cv2

cap = cv2.VideoCapture("video1.mp4")
while True:
    ret, frame = cap.read()

    cv2.imshow("Video Fathan",frame)

    key = cv2.waitKey(3)
    if key == 27 or key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()