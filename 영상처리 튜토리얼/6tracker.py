import cv2
import sys

def tracker(name,aa):

    tracker = cv2.Tracker_create(aa)

    # Read video
    video = cv2.VideoCapture(name)

    # Exit if video not opened.
    if not video.isOpened():
        print("Could not open video")
        sys.exit()

    # Read first frame.
    ok, frame = video.read()


    video
    if not ok:
        print('Cannot read video file')
        sys.exit()

    # Define an initial bounding box
    bbox = (287, 23, 86, 320)

    # Uncomment the line below to select a different bounding box
    bbox = cv2.selectROI(frame, False)

    # Initialize tracker with first frame and bounding box
    ok = tracker.init(frame, bbox)

    while True:
        # Read a new frame
        ok, frame = video.read()
        if not ok:
            break

        # Update tracker
        ok, bbox = tracker.update(frame)

        # Draw bounding box
        if ok:
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (0, 0, 255))

        # Display result
        cv2.imshow(aa, frame)

        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27: break

tracker('videos/조명off.mp4',"GOTURN")

# Set up tracker.
# Instead of MIL, you can also use
# BOOSTING, KCF, TLD, MEDIANFLOW or GOTURN
# BOOSTING > MIL > KCF 성능은 MIL KCF3.1 GOTURN3.2
# TLD 겹치기
# MEDIANFLOW 작은변화
# GOTURN CNN알고리즘