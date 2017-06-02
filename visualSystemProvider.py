#!/usr/bin/pythom

from camera import Camera
from pattern_perceptor import PatternPerceptor
import cv2

class VisualSystemProvider:
	def __init__(self):
		self.camera = Camera(0);
		self.patternPerceptor = PatternPerceptor("./deploy.prototxt","./hand_written.caffemodel");
	def run(self):
		while(True):
			image = self.camera.read()
			image = self.cvCVMATtoCaffeImage(image)
#			cv2.imshow("image",image)
#			cv2.waitKey(2)
			self.patternPerceptor.recognize(image)
	def cvCVMATtoCaffeImage(self,image):
		image = image / 255
	        image = image[:,:,(2,1,0)]
		return image
