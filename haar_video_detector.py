from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2

# Load image from arguments into program
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", type=str,
                default="dog_face.xml")
args = vars(ap.parse_args())

print("[INFO] loading dog detector...")
detector = cv2.CascadeClassifier("cascades/" + args["cascade"])

print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)


while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=500)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector.detectMultiScale(gray, scaleFactor=1.15,
                                    minNeighbors=8, minSize=(30, 30),
                                    flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y),
                    (x + w, y + h),
                    (0, 255, 0), 2)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        break

cv2.destroyAllWindows()
vs.stop()