from skimage.exposure import rescale_intensity
import numpy as np
import argparse
import cv2

def convolve(image, kernel):
    (iH, iW) = image.shape[:2]
    (kH, kW) = kernel.shape[:2]

    pad_size = (kW - 1) // 2
    image = cv2.copyMakeBorder(image, pad_size, pad_size, pad_size, pad_size,
                               cv2.BORDER_REPLICATE)
    output = np.zeros((iH, iW), dtype="float32")
    
    for y in np.arange(pad_size, iH + pad_size):
        for x in np.arange(pad_size, iW + pad_size):
            roi = image[y - pad_size:y + pad_size + 1,
                        x - pad_size:x + pad_size + 1]
            
            k = (roi * kernel).sum()

            output[y - pad_size, x - pad_size] = k
    
    output = rescale_intensity(output, in_range=(0, 255))
    output = (output * 255).astype("uint8")

    return output


# Load image from arguments into program
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--in", required=True,
                help="path to input image")
ap.add_argument("-o", "--out", required=True,
                help="path to output image")
ap.add_argument("-k", "--kernel", required=True,
                help="kernel type name")
args = vars(ap.parse_args())

image = cv2.imread("images/in/" + args["in"])

def blur(blurAmount: int):
    return np.ones((blurAmount, blurAmount), dtype="float") * (1.0 / (blurAmount * blurAmount))

sharpen = np.array((
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]), dtype="int")

laplacian = np.array((
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]), dtype="int")

sobelX = np.array((
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]), dtype="int")

sobelY = np.array((
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]), dtype="int")

kernels = dict()
kernels["smallBlur"] = blur(7)
kernels["largeBlur"] = blur(21)
kernels["sharpen"] = sharpen
kernels["laplacian"] = laplacian
kernels["sobelX"] = sobelX
kernels["sobelY"] = sobelY

def applyConvolution(image, kernel_name, kernels):
    kernel = kernels[kernel_name]
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    output = convolve(gray_scale, kernel)
    # output = cv2.filter2D(gray_scale, -1, kernel)
    return output

output = applyConvolution(image, args["kernel"], kernels)

(h, w, c) = image.shape[:3]

print("width: {}px".format(w))
print("height: {}px".format(h))
print("channels: {}".format(c))

cv2.imshow(args["in"], image)
#cv2.waitKey(0)

(h, w) = output.shape[:2]

print("width: {}px".format(w))
print("height: {}px".format(h))
print("channels: {}".format(c))

cv2.imshow(args["out"], output)
cv2.waitKey(0)

cv2.imwrite("images/out/" + args["out"], output)