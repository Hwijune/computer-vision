import numpy as np
import cv2

def drawCube(img, corners, imgpts):
    imgpts = np.int32(imgpts).reshape(-1, 2)
    cv2.drawContours(img, [imgpts[:4]], -1, (255, 0, 0), -3)

    for i, j in zip(range(4), range(4, 8)):
        cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]), (0, 255, 0), 2)

    cv2.drawContours(img, [imgpts[4:]], -1, (0, 255, 0), 2)

    return img

def poseEstimation():
    with np.load('calib.npz') as X:
        ret, mtx, dist, _, _ = [X[i] for i in ('ret', 'mtx', 'dist', 'rvecs', 'tvecs')]

    termination = (cv2.TERM_CRITERIA_EPS + cv2.TermCriteria_MAX_ITER, 30, 0.001)
    objp = np.zeros((7*10, 3), np.float32)
    objp[:, :2] = np.mgrid[0:7, 0:10].T.reshape(-1,2)
    axis = np.float32([[0,0,0],[0,3,0],[3,3,0],[3,0,0],[0,0,-3],[0,3,-3],[3,3,-3],[3,0,-3]])

    objpoints = []
    imgpoints = []

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray,(7,10),None)

        if ret == True:
            cv2.cornerSubPix(gray, corners, (11, 11),(-1, -1), termination)
            _, rvecs, tvecs, inliers = cv2.solvePnPRansac(objp, corners, mtx, dist)
            imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)
            frame = drawCube(frame, corners, imgpts)

        cv2.imshow('frame', frame)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

poseEstimation()

