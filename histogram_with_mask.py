from matplotlib import pyplot as plt
import numpy as np
import imutils
import argparse
import cv2

# Load image from arguments into program
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--in", required=True,
                help="path to input image")
args = vars(ap.parse_args())

def plot_1D(image, title, mask=None):
    channels = cv2.split(image)
    colors = ("b", "g", "r")

    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("% of Pixels") # plt.ylabel("# of Pixels")

    for (channel, color) in zip(channels, colors):
        hist = cv2.calcHist([channel], [0], mask, [256], [0, 256])
        plt.plot(hist / hist.sum(), color=color)
        plt.xlim([0, 256])

    print(f"1D histogram shape: {hist.shape}, with {hist.flatten().shape[0]} values")

def plot_2D(image, title, mask=None):
    channels = cv2.split(image)
    colors = ("b", "g", "r")

    fig = plt.figure()
    plt.title(title)

    index = 131

    for (i, (channel1, color1)) in enumerate(zip(channels[:-1], 
                                                 colors[:-1])):
        for (channel2, color2) in zip(channels[i+1:], 
                                    colors[i+1:]):
            ax = fig.add_subplot(index)
            hist = cv2.calcHist([channel1, channel2], [0, 1], mask, [32, 32],
                                [0, 256, 0, 256])
            p = ax.imshow(hist / hist.sum(), interpolation="nearest")
            ax.set_title(f"2D Color Histogram for {color1.upper()} and {color2.upper()}")
            plt.colorbar(p)

            index += 1

    print(f"2D histogram shape: {hist.shape}, with {hist.flatten().shape[0]} values")

def plot_histogram(image, title, mask=None, masked=None):
    plot_1D(image, "1D Histogram " + title, mask=mask)
    plot_2D(image, "2D Histogram " + title, mask=mask)
    plt.figure()
    plt.axis("off")
    plt.title(title + " Image")
    plt.imshow(imutils.opencv2matplotlib(image if masked is None else masked))

image = cv2.imread("images/in/" + args["in"])

plot_histogram(image, "Original")

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (60, 290), (210, 390), 255, -1)
cv2.imshow("Mask", mask)
masked = cv2.bitwise_and(image, image, mask=mask)

plot_histogram(image, "Masked", mask=mask, masked=masked)


plt.show()