from pupil_apriltags import Detector
import argparse
import imutils
import cv2

# Load image from arguments into program
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--in", required=True,
                help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread("images/in/" + args["in"])
image = imutils.resize(image, width=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


detector = Detector(families="tag36h11")
results = detector.detect(gray)
print(f"[INFO] {len(results)} total AprilTags detected")


for r in results:
    (ptA, ptB, ptC, ptD) = r.corners

    corners = []
    for corner in r.corners:
        corners.append((int(corner[0]), 
                        int(corner[1])))

    corners += [corners[0]]

    for i, corner1 in enumerate(corners[:-1]):
        corner2 = corners[i + 1]
        cv2.line(image, corner1, corner2,
             (0, 255, 0), 2)
    
    (cX, cY) = (int(r.center[0]), int(r.center[1]))
    cv2.circle(image, (cX, cY), 5, (0, 0, 255), -1)

    tagFamily = r.tag_family.decode("utf-8")
    cv2.putText(image, tagFamily, (corners[0][0], corners[0][1] - 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                (0, 255, 0), 2)
    print(f"[INFO] tag family: {tagFamily}")

cv2.imshow(args["in"], image)
cv2.waitKey(0)