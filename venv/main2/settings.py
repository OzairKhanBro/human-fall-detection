# Fall detector settings class
#

class Settings(object):
	
	def __init__(self):
		self.debug = 0 # boolean
		# self.source = '../data2/fall-09-cam0.mp4' # camera source
		# self.source = '../data2/1_2.mp4'  # camera source
		# if (len(self.frameH) > self.frameSize):
		# if stdev(self.deltaH) > 4 and stdev(self.deltaW) > 11 \
		# 			and mean(self.deltaH) > 2 and mean(self.deltaW) < -4:
		# 		self.alert = 1
		# self.source = '../data4/video (14).avi'  # working
		# self.source = '../data4/video (17).avi'  # working
		self.source = '../data4/video (9).avi'  # working
		# self.source = '../data4/video (8).avi'  # working
		# self.source = '../data4/video (6).avi'  #not working false positive
		# self.source = '../data4/video (5).avi'  #working
		# self.source = '../data4/video (4).avi'  #working
		# self.source = '../data4/video (2).avi'  #working
		# self.source = '../data4/video (1).avi'  #working

		#######
		# if (len(self.frameH) > self.frameSize):
		# 	if stdev(self.deltaH) > 4 and stdev(self.deltaW) > 11 \
		# 			and mean(self.deltaH) > 2 and mean(self.deltaW) < -9:
		# 		self.alert = 1
		#######
		# self.source = '../data5/chute01/cam7.avi'  # working
		# self.source = '../data5/chute02/cam7.avi'  # working
		# self.source = '../data5/chute03/cam7.avi'  # working
		# self.source = '../data5/chute04/cam7.avi'  # working
		# self.source = '../data5/chute05/cam7.avi'  # not workig
		# self.source = '../data5/chute06/cam7.avi'  # working
		# self.source = '../data5/chute07/cam7.avi'  # working
		# self.source = '../data5/chute08/cam7.avi'  # working
		# self.source = '../data5/chute09/cam7.avi'  #not working
		# self.source = '../data5/chute10/cam7.avi'  #not working
		# self.source = '../data5/chute12/cam7.avi'  # working
		# self.source = '../data5/chute13/cam7.avi'  # working
		# self.source = '../data5/chute14/cam7.avi'  # working
		# self.source = '../data5/chute15/cam7.avi'  #not working
		# self.source = '../data5/chute16/cam7.avi'  # working
		# self.source = '../data5/chute17/cam7.avi'  # working
		# self.source = '../data5/chute18/cam7.avi'  #not working
		# self.source = '../data5/chute19/cam7.avi'  #not working
		# self.source = '../data5/chute21/cam7.avi'  #working  good
		# self.source = '../data5/chute22/cam7.avi'  #not working fall after sit down
		# self.source = '../data5/chute24/cam7.avi'  #not working  false positive

		# self.source = '../data3/17_3.MKV'  # camera source
		# self.source = '../data3/1_1.avi'  # camera source

		#true negative

		# self.source = '../data4/video (19).avi'  # working
		# self.source = '../data5/chute23/cam7.avi'  #working
		# self.source = '../data1/video (18).avi'  # working
		# self.source = '../data1/video (26).avi'  # working
		# self.source = '../data1/video (17).avi'  # working
		# self.source = '../data1/video (7).avi'  # working
		# self.source = '../data1/video (5).avi'  # working

		# self.source = '../data4/video (20).avi'  # working
		# self.source = '../data4/video (21).avi'  # working
		# self.source = '../data4/video (22).avi'  # working
		# self.source = '../data4/video (23).avi'  #not working false positive
		# self.source = '../data4/video (25).avi'  # working
		# self.source = '../data4/video (26).avi'  # working
		# self.source = '../data4/video (27).avi'  # working
		# self.source = '../data4/video (27).avi'  # working
		# self.source = '../data4/video (28).avi'  # working
		# self.source = '../data4/video (29).avi'  # working
		# self.source = '../data4/video (30).avi'  # working
		# self.source = '../data4/video (31).avi'  # working
		# self.source = '../data4/video (32).avi'  # working
		# self.source = '../data4/video (33).avi'  # working


		self.bsMethod = 0  #listed in bs.py
		self.MOG2learningRate = 0
		self.MOG2shadow = 0
		self.humanCheck=1
		self.MOG2history = 100
		self.MOG2thresh = 20
		self.minArea = 150*150 # minimum area to be considered as a person
		self.thresholdLimit = 50
		self.dilationPixels = 30
		self.useGaussian = 0 # boolean
		self.gaussianPixels = 31
		self.useBw = 1 # boolean
		self.useResize = 1 # boolean
		self.movementMaximum = 100 # amount to move to still be the same person
		self.movementMinimum = 3 # minimum amount to move to not trigger alarm
		self.movementTime = 80 # number of frames after the alarm is triggered
		self.location = 'Viikintie 1'
		self.phone = '01010101010'