#!/usr/bin/env python3
import cv2


aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
# cv2.imwrite('aruco_4_0.png', cv2.aruco.drawMarker(aruco_dict, 0, 6))
parameters = cv2.aruco.DetectorParameters_create()


capture = cv2.VideoCapture(0)
width = 600
height = int(width / capture.get(cv2.CAP_PROP_FRAME_WIDTH) *
             capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
cv2.namedWindow("img")


while True:
    ret, img = capture.read()
    img = cv2.resize(img, (width, height))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(
        gray, aruco_dict, parameters=parameters)
    img = cv2.aruco.drawDetectedMarkers(img, corners, ids)
    cv2.imshow("img", img)

    # Press any key to quit
    if cv2.waitKey(1) >= 0:
        break
