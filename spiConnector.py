import time
import sys
import spidev
import sys


class SPI : 
	def __init__(self , bus ,device):
		self.spi = spidev.SpiDev()
		self.spi.open(bus,device)
	def writeData(self,data):
		self.spi.writebytes(data)
