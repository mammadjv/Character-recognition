#!/usr/bin/pythom
import numpy as np
import cv2
from Queue import Queue
from threading import Thread
import sys

class Camera:
        def __init__(self,id):
		self.cap = cv2.VideoCapture(id)
		self.queue = Queue(10)
		self.thread = Thread(target = self.update)
	def read(self):
		if(self.queue.qsize()>0):
			frame = self.queue.get()
			return frame
		else:
			return None
	def startCameraBuffering(self):
		self.thread.start()
	def update(self):
		while(True):
			if not self.queue.full():
				(framerate , frame) = self.cap.read()
				self.queue.put(frame)
