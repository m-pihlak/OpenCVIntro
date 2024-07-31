import argparse
import imutils
import cv2

# Load image from arguments into program
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", type=str,
                default="dog_face.xml")
ap.add_argument("-i", "--in", required=True,
                help="path to input image")
ap.add_argument("-o", "--out", required=True,
                help="path to output image")
args = vars(ap.parse_args())

print("[INFO] loading dog detector...")
detector = cv2.CascadeClassifier("cascades/" + args["cascade"])

image = cv2.imread("images/in/" + args["in"])
image = imutils.resize(image, width=500)
(h, w, c) = image.shape[:3]

print("width: {}px".format(w))
print("height: {}px".format(h))
print("channels: {}".format(c))

print("[INFO] performing dog detection...")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rects = detector.detectMultiScale(gray, scaleFactor=1.06,
                                  minNeighbors=5, minSize=(30, 30),
                                  flags=cv2.CASCADE_SCALE_IMAGE)
print(f"[INFO] {len(rects)} faces detected...")

for (x, y, w, h) in rects:
    cv2.rectangle(image, (x, y),
                  (x + w, y + h),
                  (0, 255, 0), 2)

cv2.imshow(args["out"], image)
cv2.waitKey(0)

cv2.imwrite("images/out/" + args["out"], image)