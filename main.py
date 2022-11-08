import os
import cv2

#from cvzone.HandTrackingModule import HandDetector
#from cvzone.HandTrackingModule import HandDetector import cv2
#import cv2 from cvzone.HandTrackingModule import HandDetector
from cvzone.HandTrackingModule import HandDetector

width, height = 1280, 720
folderPath = "presentation"

cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

pathImages = sorted(os.listdir(folderPath), key=len)
print(pathImages)

imgNumber = 0
hs, ws = int(120 * 2.5), int(213 * 2.5)

detector = HandDetector(detectionCon=0.8, maxHands=1)

# Hand Detector


while True:
    success, img = cap.read()
    pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

    hands, img = detector.findHands()

    imgSmall = cv2.resize(img, (ws, hs))
    h, w, _ = imgCurrent.shape
    imgCurrent[0:hs, w - ws:w] = imgSmall

    cv2.imshow("Image", img)
    cv2.imshow("Slides", imgCurrent)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
