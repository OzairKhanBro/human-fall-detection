# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import imutils
import time
import cv2

#
# # construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-v", "--video", type=str,
# 	help="path to input video file")
# ap.add_argument("-t", "--tracker", type=str, default="kcf",
# 	help="OpenCV object tracker type")
# args = vars(ap.parse_args())

# extract the OpenCV version info
(major, minor) = cv2.__version__.split(".")[:2]

# if we are using OpenCV 3.2 OR BEFORE, we can use a special factory
# function to create our object tracker
# if int(major) == 3 and int(minor) < 3:
# 	tracker = cv2.Tracker_create("KCF")#args["tracker"].upper())
#
# # otherwise, for OpenCV 3.3 OR NEWER, we need to explicity call the
# # approrpiate object tracker constructor:
# else:
# initialize a dictionary that maps strings to their corresponding
# OpenCV object tracker implementations
trackerName="kcf"
# videopath="../data2/fall-02-cam0.mp4"
# videopath="../data2/1_2.mp4"
# videopath="../data1/asdf.avi"
videopath="../data4/video (25).avi"
OPENCV_OBJECT_TRACKERS = {
   "csrt": cv2.TrackerCSRT_create,
    "kcf": cv2.TrackerKCF_create,
   "boosting": cv2.TrackerBoosting_create,
   "mil": cv2.TrackerMIL_create,#when object counters many herdals infront of camera
   "tld": cv2.TrackerTLD_create,
   "medianflow": cv2.TrackerMedianFlow_create,#for small and predictable places i.e face
   "mosse": cv2.TrackerMOSSE_create,
    "goturn":cv2.TrackerGOTURN_create
}

# grab the appropriate object tracker using our dictionary of
# OpenCV object tracker objects
tracker = OPENCV_OBJECT_TRACKERS[trackerName]()#args["tracker"]]()

# initialize the bounding box coordinates of the object we are going
# to track
initBB = None
# if a video path was not supplied, grab the reference to the web cam
# if not args.get("video", False):
# 	print("[INFO] starting video stream...")
# 	vs = VideoStream(src=0).start()
# 	time.sleep(1.0)
#
# # otherwise, grab a reference to the video file
# else:
vs = cv2.VideoCapture(videopath)#args["video"])

# initialize the FPS throughput estimator
fps = None
multiTracker=[]

# loop over frames from the video stream

# loop over frames from the video stream
while True:
    # grab the current frame, then handle if we are using a
    # VideoStream or VideoCapture object
    frame = vs.read()
    frame = frame[1] #if args.get("video", False) else frame

    # check to see if we have reached the end of the stream
    if frame is None:
        break

    # resize the frame (so we can process it faster) and grab the
    # frame dimensions
    frame = imutils.resize(frame, width=500)
    (H, W) = frame.shape[:2]
    successcount=0
    # check to see if we are currently tracking an object
    if len(multiTracker)>0:
        # grab the new bounding box coordinates of the object
        for singletracker in (multiTracker):
            # print(len(multiTracker))
            # fps = FPS().start()
            (success, box) = singletracker.update(frame)
            # check to see if the tracking was a success
            if success:
                successcount+=1
                (x, y, w, h) = [int(v) for v in box]
                if x<=10 or y<=10 or x+w>=W-10 or y+h>=H-10:
                    tracker.clear()
                    multiTracker.remove(singletracker)
                else:
                    cv2.rectangle(frame, (x, y), (x + w, y + h),
                                  (0, 255, 0), 2)
            else:
                tracker.clear()
                multiTracker.remove(singletracker)



        # update the FPS counter
        fps.update()
        fps.stop()

        # initialize the set of information we'll be displaying on
        # the frame
        info = [
            ("Tracker", tracker),
            ("Success", successcount if successcount>0 else "No"),
            ("FPS", "{:.2f}".format(fps.fps())),
        ]

        # loop over the info tuples and draw them on our frame
        for (i, (k, v)) in enumerate(info):
            text = "{}: {}".format(k, v)
            cv2.putText(frame, text, (10, H - ((i * 20) + 20))
                        ,cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2,cv2.LINE_8)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    # if the 's' key is selected, we are going to "select" a bounding
    #box to track
    if key == ord("s"):
        # select the bounding box of the object we want to track (make
        # sure you press ENTER or SPACE after selecting the ROI)
        initBB = cv2.selectROI("Frame", frame, fromCenter=False,showCrosshair=True)
        # bboxes.append(initBB)
        # start OpenCV object tracker using the supplied bounding box
        # coordinates, then start the FPS throughput estimator as well
        tracker = OPENCV_OBJECT_TRACKERS[trackerName]()
        tracker.init(frame, initBB)
        multiTracker.append(tracker)
        fps = FPS().start()
    elif key == ord("q"):
        break
    # else:
    #     initBB = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)

# if we are using a webcam, release the pointer
# if not args.get("video", False):
#     vs.stop()

# otherwise, release the file pointer
# else:
vs.release()

# close all windows
cv2.destroyAllWindows()




