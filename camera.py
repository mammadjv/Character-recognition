#!/usr/bin/pythom
import numpy as np
import cv2
from Queue import Queue
from threading import Thread
import sys


class Camera:
        def __init__(self,id):
		self.cap = cv2.VideoCapture(id)
		self.queue = []
		self.cap.set(3,640)
		self.cap.set(4,480)
#		self.thread = Thread(target = self.update)
#		self.thread.daemon = True
	def read(self):
		(framerate , frame) = self.cap.read()
		frame = cv2.flip(cv2.transpose(frame) , flipCode = 0)
		return frame
#		if( len(self.queue) > 1):
#			frame = self.queue.pop()
#			frame = cv2.flip(cv2.transpose(frame) , flipCode = 0)
#			return frame
#		else:
#			return None
	def startCameraBuffering(self):
		self.thread.start()
	def update(self):
		while(True):
			if ( len(self.queue) ==   10):
				self.queue.pop(0)
				
			(framerate , frame) = self.cap.read()
			self.queue.append(frame)
