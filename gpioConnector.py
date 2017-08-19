import RPi.GPIO as GPIO
import time

class GPIOConnector:
	def __init__(self , id1 , id2, id3):
		self.pinid1 = id1
		self.pinid2 = id2
		self.pinidRead = id3		

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.pinid1 , GPIO.OUT)
		GPIO.setup(self.pinid2 , GPIO.OUT)
		GPIO.setup(self.pinidRead , GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
		self.reset()
	def writeData(self,pin1value , pin2value):
		GPIO.output(self.pinid1,pin1value)
		time.sleep(0.002)
		GPIO.output(self.pinid2,pin2value)
		time.sleep(0.002)	
	def readData(self):
		return GPIO.input(self.pinidRead) 		
	def reset(self):
		GPIO.output(self.pinid1,GPIO.LOW)
		GPIO.output(self.pinid2,GPIO.LOW)
