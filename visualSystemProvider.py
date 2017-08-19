from camera import Camera
from pattern_perceptor import PatternPerceptor
from regionProvider import RegionProvider
import cv2
import time
import cv
from gpioConnector import GPIOConnector

FrameSizeX, FrameSizeY = 260,260

PIN1 , PIN2 , PIN_Read = 23 , 24 , 21

class VisualSystemProvider:
	def __init__(self):
		self.camera = Camera(0)
		self.patternPerceptor = PatternPerceptor("./deploy.prototxt","./hand_written1.caffemodel")
		self.regionProvider = RegionProvider()
		self.gpioConnector = GPIOConnector(PIN1,PIN2,PIN_Read)
		self.listOfContours = []
		self.mychar = 5
	def run(self):
#		self.camera.startCameraBuffering()
		counter = 0
	    	while(True):
			start = time.time()
			image = self.camera.read()
	        	if (image == None):
				self.gpioConnector.reset()
                        	continue
                	image = cv2.resize(image,(FrameSizeX,FrameSizeY))
#			cv2.imshow('image',image)
#			cv2.waitKey(1)
#			print counter
			counter += 1
			if (self.gpioConnector.readData() == 0):
				self.gpioConnector.reset()
				self.mychar = 5
			if (self.gpioConnector.readData() == 1):
				image,draw_image ,croped_image , contour_found , edged , thresh= self.regionProvider.findContours(image)
				#cv2.imshow('thresh' , thresh)
				#cv2.waitKey(1)
				if(contour_found == False):
#					print 'no contour found in image!'
					self.gpioConnector.reset()
					if self.mychar != 5:
						pin1Value , pin2Value = self.generateByteFromPatternData(self.mychar)
						self.gpioConnector.writeData(pin1Value , pin2Value)
					continue
#				cv2.imshow('contour',croped_image)
#				cv2.imshow('thresh_seen',thresh)
#				cv2.imshow('image',image)		
#				cv2.imshow('draw_image' , draw_image)
#				cv2.waitKey(1)
				predicted_class=self.patternPerceptor.recognize(croped_image)
				pin1Value , pin2Value = self.generateByteFromPatternData(predicted_class)
				self.gpioConnector.writeData(pin1Value , pin2Value)
				#print self.gpioConnector.readData()
				#print self.mychar
				print('full ' , time.time()-start)
	def cvCVMATtoCaffeImage(self,image):
		cvImg = cv2.cv.fromarray(image)
#		image = image / 255.
#	        image = image[:,:,(2,1,0)]
		return cvImg
	def generateByteFromPatternData(self,predicted_class):
		if(predicted_class == 0):
			#print 'predicted class = H'
			self.mychar = 0
			return False , True
		elif (predicted_class == 1):
			#print 'predicted class = S'
			self.mychar = 1
			return True , False
		elif (predicted_class == 2):
			#print 'predicted class = U'
			self.mychar = 2
			return True , True	
		

