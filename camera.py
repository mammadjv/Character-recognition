#!/usr/bin/pythom
import numpy as np
import cv2

class Camera:
        def __init__(self,id):
		self.cap = cv2.VideoCapture(id)
	def read(self):
		ret, frame = self.cap.read()
		return frame
