from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2

# Load image from arguments into program
ap = argparse.ArgumentParser()
#ap.add_argument("-p", "--shape-predictor", required=True, help="path to facial landmark predictor")

ap.add_argument("-i", "--in", required=True,
                help="path to input image")
ap.add_argument("-o", "--out", required=True,
                help="path to output image")
args = vars(ap.parse_args())

detector = dlib.cnn_face_detection_model_v1('shape_predictors/dogHeadDetector.dat') #dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictors/landmarkDetector.dat') #dlib.shape_predictor(args["shape_predictor"])

image = cv2.imread(f"images/in/" + args["in"])
image = imutils.resize(image, width=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

dets = detector(gray, 1)

for (i, d) in enumerate(dets):
    rect = d.rect # rect = d
    shape = predictor(gray, rect)
    shape = face_utils.shape_to_np(shape)

    (x, y, w, h) = face_utils.rect_to_bb(rect)
    cv2.rectangle(image, (x, y),
                  (x + w, y + h),
                  (0, 255, 0), 2)
    
    cv2.putText(image, f"Face #{i + 1}",
                (x - 10, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                (0, 255, 0), 2)
    
    for (x, y) in shape:
        cv2.circle(image, (x, y), 
                   1, (0, 0, 255), -1)

cv2.imwrite("images/out/" + args["out"], image)