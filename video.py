import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
print(type(frame), dir(frame))
width, height = frame.shape[:2]
print(width, height)
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #print(frame[255,255])
    #frame[255,255] = (0,0,255)
    lower_black = np.array([0, 0, 150], dtype="uint16")
    upper_black = np.array([80, 80, 255], dtype="uint16")
    black_mask = cv2.inRange(frame, lower_black, upper_black)
    print(black_mask[width//2, height//2])
    black_mask[width//2, height//2] = 255
    #cv2.imshow('mask0', black_mask)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

