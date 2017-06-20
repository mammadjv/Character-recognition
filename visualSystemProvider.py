#!/usr/bin/pythom

from camera import Camera
from pattern_perceptor import PatternPerceptor
from regionProvider import RegionProvider
import cv2
import time
import cv

class VisualSystemProvider:
	def __init__(self):
		self.camera = Camera(0)
		self.patternPerceptor = PatternPerceptor("./deploy.prototxt","./hand_written1.caffemodel")
		self.regionProvider = RegionProvider()
	def run(self):
		self.camera.startCameraBuffering()
		while(True):
			start = time.time()		
			image = self.camera.read()
			if image == None :
				continue
			print('read' , time.time() - start)
			image, croped_image = self.regionProvider.findContours(image)
			cv2.imshow('image',croped_image)
			cv2.waitKey(2)
#			self.patternPerceptor.recognize(image)
			print('full ' , time.time()-start)
	def cvCVMATtoCaffeImage(self,image):
		cvImg = cv2.cv.fromarray(image)
#		image = image / 255.
#	        image = image[:,:,(2,1,0)]
		return cvImg

