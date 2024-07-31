from matplotlib import pyplot as plt
import argparse
import cv2

# Load image from arguments into program
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--in", required=True,
                help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread("images/in/" + args["in"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure()
plt.axis("off")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB))

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])

plt.figure()
plt.title("Grayscale Histogram (Normalized)")
plt.xlabel("Bins")
plt.ylabel("% of Pixels")
plt.plot(hist / hist.sum())
plt.xlim([0, 256])

plt.show()