# Fall detector Person class
#
from MultyTracker import MultyTracker
import cv2
import imutils
import settings
from statistics import mean,stdev

class Person(object):
	"""Person"""
	amount = 0

	def __init__(self, x, y, w, h, movementMaximum, movementMinimum, movementTime):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.frameSize=25
		self.hog = cv2.HOGDescriptor()
		self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

		self.deltaW=[]
		self.deltaH=[]
		self.frameW=[]
		self.frameH=[]
		self.fallH=[]
		self.fallW=[]
		self.delH=0
		self.delW=0
		self.movementTime = movementTime
		self.movementMaximum = movementMaximum
		self.movementMinimum = movementMinimum
		self.lastmoveTime = 0
		self.alert = 0
		self.alarmReported = 0
		self.lastseenTime = 0
		self.remove = 0
		self.human=0
		Person.amount += 1
		if Person.amount > 1000:
			Person.amount = 0
		self.id = Person.amount

	def samePerson(self, x, y, w, h):
		same = 0
		if x+self.movementMaximum > self.x and x-self.movementMaximum < self.x:
			if y+self.movementMaximum > self.y and y-self.movementMaximum < self.y:
				same = 1
		return same

	def editPerson(self, x, y, w, h,frame):
		self.frame=frame
		if abs(x-self.x) > self.movementMinimum or abs(y-self.y) > self.movementMinimum \
				or abs(w-self.w) > self.movementMinimum or abs(h-self.h) > self.movementMinimum:
			self.lastmoveTime = 0
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		if settings.Settings().humanCheck and self.human==0:
			if self.isHuman():
				self.human=1
				print("Human......")

		self.lastseenTime = 0
		if self.frameH.__len__() !=0:
			self.deltaW.append(self.frameW[self.frameW.__len__() - 1] - w)
			self.deltaH.append(self.frameH[self.frameH.__len__() - 1] - h)
			if (self.frameH[self.frameH.__len__() - 1]>=h and
				self.frameW[self.frameW.__len__() - 1]<=w):
				self.fallW.append(w)
				self.fallH.append(h)
			else:
				self.fallW.clear()
				self.fallH.clear()
		self.frameH.append(h)
		self.frameW.append(w)

		# self.frameH.append(h)
        # if(len(self.deltaW)>self.frameSize):
		# 	pass

		if(len(self.frameH)>self.frameSize):
			if stdev(self.deltaH)>2 and stdev(self.deltaW)>11\
					and mean(self.deltaH)>1.0 and mean(self.deltaW)<-4:
				self.alert=1
			#
			# self.deltaW.append(self.frameW[self.frameW.__len__()-1]-w)
			# self.deltaH.append(self.frameH[self.frameH.__len__()-1]-h)
			#
			#
			self.deltaW.pop(0)
			self.deltaH.pop(0)
			self.frameH.pop(0)
			self.frameW.pop(0)
			# if(self.deltaH.index(max(self.deltaH))<
			# 		self.deltaH.index(min(self.deltaH))):
			# 	self.delH=-(max(self.frameH)-min(self.frameH))
			# else:
			self.delH=(max(self.frameH)-min(self.frameH))
			# if(self.deltaW.index(max(self.deltaW))<
			# 		self.deltaW.index(min(self.deltaW))):
			# 	self.delW=-(max(self.frameW)-min(self.frameW))
			# else:
			self.delW=(max(self.frameW)-min(self.frameW))

			# print("h="+str(self.delH)+" w="+str(self.delW)+" mw="+str(mean(self.deltaW))
            #       +" mh="+str(mean(self.deltaH))+" stdw="+str(stdev(self.deltaW))
            #       +" stdH="+str(stdev(self.deltaH)))
			# print("h={} w={} mW={:4.1f} mH={:4.1f} stdW={:4.1f} stdH={:4.1f}".format(
			# 	self.delH,self.delW,mean(self.deltaW),mean(self.deltaH),stdev(self.deltaW),stdev(self.deltaH)
			# ))


	def getId(self):
		return self.id

	def tick(self):
		self.lastmoveTime += 1
		self.lastseenTime += 1
		# if self.lastmoveTime > self.movementTime:
		# 	self.alert = 1
		# 	print("alarm...")
		if self.lastseenTime > 4: # how many frames ago last seen
			self.remove = 1
			
	def getAlert(self):
		return self.alert

	def getRemove(self):
		return self.remove


	def isHuman(self):
		asdf=self.frame[self.y:self.y+self.h, self.x:self.x+self.w]
		asdf=imutils.resize(asdf,width=150)
		rects, weights=self.hog.detect(asdf)
		# rects, weights = hog.detectMultiScale(frame,scale=1.00)#,winStride=(8,8),
                                            #padding=(16,16), scale=1.05)
		if len(weights)==0:
			return None
		return weights[0]>0.6
class Persons:
	def __init__(self, movementMaximum, movementMinimum, movementTime):
		self.persons = []
		self.movementMaximum = movementMaximum
		self.movementMinimum = movementMinimum
		self.movementTime = movementTime
		Person.amount = 0
		self.frame=[]

	# self.multyTracker=MultyTracker()

	def addPerson(self, x, y, w, h,frame):
		# self.frame=frame
		person = self.familiarPerson(x, y, w, h)
		if person:
			person.editPerson(x, y, w, h,frame)
			return person
		else:
			person = Person(x ,y ,w ,h , self.movementMaximum, self.movementMinimum, self.movementTime)
			self.persons.append(person)
			return person
		
	def familiarPerson(self, x, y, w, h):
		for i,person in enumerate(self.persons):
			if person.samePerson(x, y, w, h):
				return person
		return None

	def tick(self):
		for person in self.persons:
			person.tick()
			if person.getRemove():
				self.persons.remove(person)
	def isHuman(self,frame1):
		if frame1.size==0:
			return None
		cv2.imshow("asdf",frame1)
		frame=imutils.resize(frame1,width=200)
		rects, weights=self.hog.detect(frame)
		# rects, weights = hog.detectMultiScale(frame,scale=1.00)#,winStride=(8,8),
                                            #padding=(16,16), scale=1.05)
		if len(weights)==0:
			return None
		return weights[0]>0.6
