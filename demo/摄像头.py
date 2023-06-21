import cv2

cv2.namedWindow('new',cv2.WINDOW_NORMAL)
cv2.resizeWindow('new', 640, 480)

cap = cv2.VideoCapture(0)

while True:
    res,frame = cap.read()
    try:
        cv2.imshow('new', frame)
    except:
        pass
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()