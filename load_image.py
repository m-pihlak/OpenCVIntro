import argparse
import cv2

# Load image from arguments into program
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
ap.add_argument("-o", "--out", required=True,
                help="path to output image")
args = vars(ap.parse_args())

image = cv2.imread("images/in/" + args["image"])
(h, w, c) = image.shape[:3]

print("width: {}px".format(w))
print("height: {}px".format(h))
print("channels: {}".format(c))


cv2.imshow(args["image"], image)
cv2.waitKey(0)

cv2.imwrite("images/out/" + args["out"], image)