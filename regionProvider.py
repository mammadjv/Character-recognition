#!/usr/bin/pythom
import numpy as np
import cv2
from Queue import Queue
from threading import Thread
import sys

class RegionProvider:
        def __init__(self):
		print 'Region provider module created'
	def findContours(self,image):
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(gray, (3, 3), 0)
		ret,thresh = cv2.threshold(gray,80,255,cv2.THRESH_BINARY)
		edged = cv2.Canny(thresh, 100, 50 ,1)
		contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		best_x , best_y , best_w , best_h = 0 , 0 , 0 , 0		
		for cnt in contours :
			x,y,w,h = cv2.boundingRect(cnt)
			if(w*h > best_w*best_h):
				best_x , best_y , best_w , best_h = x , y , w , h
			#cv2.rectangle(draw_image,(x,y),(x+w,y+h),(255,255,0),2)
 
		crop_img = image

		if(best_w > 0):
			crop_img = image[best_y:best_y + best_h, best_x:best_x + best_w]
		return image , crop_img
