from matplotlib import pyplot as plt
import argparse
import imutils
import cv2

# Load image from arguments into program
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--in", required=True,
                help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread("images/in/" + args["in"])

channels = cv2.split(image)
colors = ("b", "g", "r")

plt.figure()
plt.title('"Flattened" Color Histogram')
plt.xlabel("Bins")
plt.ylabel("% of Pixels") # plt.ylabel("# of Pixels")

for (channel, color) in zip(channels, colors):
    hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
    plt.plot(hist / hist.sum(), color=color)
    plt.xlim([0, 256])

print(f"1D histogram shape: {hist.shape}, with {hist.flatten().shape[0]} values")

fig = plt.figure()
index = 131

for (i, (channel1, color1)) in enumerate(zip(channels[:-1], 
                                             colors[:-1])):
    for (channel2, color2) in zip(channels[i+1:], 
                                  colors[i+1:]):
        ax = fig.add_subplot(index)
        hist = cv2.calcHist([channel1, channel2], [0, 1], None, [32, 32],
                            [0, 256, 0, 256])
        p = ax.imshow(hist, interpolation="nearest")
        ax.set_title(f"2D Color Histogram for {color1.upper()} and {color2.upper()}")
        plt.colorbar(p)

        index += 1

print(f"2D histogram shape: {hist.shape}, with {hist.flatten().shape[0]} values")

plt.show()