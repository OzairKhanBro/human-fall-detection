import cv2
import time

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# cap = cv2.VideoCapture('../data2/fall-01-cam0.mp4' )
# cap = cv2.VideoCapture('../data1/video (2).avi' )
# cap = cv2.VideoCapture('../data3/1_3.MKV' )
# cap = cv2.VideoCapture('../data2/1_2.mp4' )
cap = cv2.VideoCapture('../data1/video (2).avi' )
# start_frame_number = 50
# cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame_number)
_i=1;
while True:
    r, frame = cap.read()
    # if _i%10!=0:
    #     _i=_i+1;
    #
    #     cv2.imshow("preview", frame)
    #
    # elif r:
    if r:
        start_time = time.time()
        frame = cv2.resize(frame,(400,500) )#(1280, 720))  # Downscale to improve frame rate
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)  # HOG needs a grayscale image

        rects, weights = hog.detectMultiScale(gray_frame)

        # Measure elapsed time for detections
        end_time = time.time()
        print("Elapsed time:", end_time - start_time)
        _i=_i+1

        for i, (x, y, w, h) in enumerate(rects):
            if weights[i] < 0.8:
                continue
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("preview", frame)
#        time.sleep(0.5)

    k = cv2.waitKey(1)
    if k & 0xFF == ord("q"):  # Exit condition
        break