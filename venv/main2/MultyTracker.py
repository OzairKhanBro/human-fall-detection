import cv2
class MultyTracker:
    def __init__(self,TrackerName="kcf"):
        self.trackerName=TrackerName
        self.multiTracker = []
        self.fps=[]
    def setFrame(self,frame,box):
        self.fps.append(FPS())
        tracker = OPENCV_OBJECT_TRACKERS[trackerName]()
        tracker.init(frame,box)
        self.multiTracker.append(tracker)
    def removeTracker(self,index):
        self.multiTracker.pop(index)
        self.fps.pop(index)
    def update(self,frame,index):
        self.fps[index]=Fps().start()
        success,box= self.multiTracker[index].update()
        self.fps[index].stop()
        self.fps[index].update()
        return success,box
    def WriteOnFrame(self,frame):
        for j,singletracker in enumerate(multiTracker):
            (success, box)=self.update(frame,j)
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
                self.removeTracker(j)
        info = [
            ("Tracker", tracker),
            ("Success", successcount if successcount > 0 else "No"),
            ("FPS", "{:.2f}".format(fps.fps()))]
        for (i, (k, v)) in enumerate(info):
            text = "{}: {}".format(k, v)
            cv2.putText(frame, text, (10, H - ((i * 20) + 20))
                        , cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)


OPENCV_OBJECT_TRACKERS = {
    "csrt": cv2.TrackerCSRT_create,
    "kcf": cv2.TrackerKCF_create,
    "boosting": cv2.TrackerBoosting_create,
    "mil": cv2.TrackerMIL_create,  # when object counters many herdals infront of camera
    "tld": cv2.TrackerTLD_create,
    "medianflow": cv2.TrackerMedianFlow_create,  # for small and predictable places i.e face
    "mosse": cv2.TrackerMOSSE_create,
    "goturn": cv2.TrackerGOTURN_create
}