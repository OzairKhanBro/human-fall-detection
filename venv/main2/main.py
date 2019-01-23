# Fall detector main

import video
import time
import sys
import numpy as np
import cv2
import time
import threading
from form import SettingForm
class cameraManager(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.video = video.Video()
        # time.sleep(1.0) # let camera autofocus + autosaturation settle
        # self.video.camera.set(cv2.CAP_PROP_POS_FRAMES,120)
        self.video.nextFrame()
        self.video.testBackgroundFrame()
        # video.camera.set(cv2.CAP_PROP_FPS,60)
        # self.video.camera.set(cv2.CAP_PROP_FPS,20)

    # print(self.video.camera.get(CAP_PROP_POS_MEC))
    # print(self.video.camera.get(cv2.CAP_PROP_FRAME_COUNT ))
    # print(self.video.camera.get(CAP_PROP_POS_FRAMES))


    def run(self):
        print(self.video.camera.get(cv2.CAP_PROP_FRAME_COUNT))
        print(str(self.video.camera.get(cv2.CAP_PROP_FPS)))
        while 1:
            #
            #        +" "+str(self.video.camera.get(cv2.CAP_PROP_POS_MSEC)))
            # if(cv2.CAP_PROP_POS_AVI_RATIO==1):
            #     print(self.video.camera.get(cv2.CAP_PROP_POS_FRAMES))
            self.video.nextFrame()
            self.video.testBackgroundFrame()
            self.video.updateBackground()
            self.video.compare()
            self.video.showFrame()
            self.video.testSettings()
            if self.video.testDestroy():
                sys.exit()

if "__main__" == __name__:
	camera=cameraManager()
	camera.start()
	# print("fjauwefhnasmdnf lkajweflnkjasdf")
	# ET = SettingForm(camera.video.settings)
	# ET.top.mainloop()
