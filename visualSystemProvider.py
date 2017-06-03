#!/usr/bin/pythom

from camera import Camera
from pattern_perceptor import PatternPerceptor
import cv2
import time
import cv

class VisualSystemProvider:
	def __init__(self):
		self.camera = Camera(1);
		self.patternPerceptor = PatternPerceptor("./deploy.prototxt","./hand_written.caffemodel");
	def run(self):
		self.camera.startCameraBuffering()
		while(True):
			start = time.time()		
			image = self.camera.read()
			if image == None :
				continue
			print('read' , time.time() - start)
			cv2.imshow('image',image)
			cv2.waitKey(2)
			self.patternPerceptor.recognize(image)
			print('full ' , time.time()-start)
	def cvCVMATtoCaffeImage(self,image):
		cvImg = cv2.cv.fromarray(image)
#		image = image / 255.
#	        image = image[:,:,(2,1,0)]
		return cvImg
