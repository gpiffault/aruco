#!/usr/bin/env python3
import argparse
import cv2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw ArUco marker.')
    parser.add_argument('id', type=int)
    parser.add_argument('--dict', default='DICT_4X4_50')
    args = parser.parse_args()

    size = int(args.dict[5])

    aruco_dict = cv2.aruco.getPredefinedDictionary(
        getattr(cv2.aruco, args.dict))
    cv2.imwrite('aruco_{}_{}.png'.format(size, args.id),
                cv2.aruco.drawMarker(aruco_dict, args.id, size + 2))
