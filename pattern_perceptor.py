#!/usr/bin/pythom
import numpy as np
import cv2
import time
import caffe


class PatternPerceptor:
        def __init__(self,trainedfile,model):
		print "pattern perceptor module added"
		self.net = caffe.Net(trainedfile,model,caffe.TEST)
		self.trainedfile = trainedfile
		
	def recognize(self,source):
		transformer = caffe.io.Transformer({'data': self.net.blobs['data'].data.shape})
		transformer.set_transpose('data', (2,0,1))  # move image channels to outermost dimension
		transformer.set_mean('data', np.asarray([104,117,123]))         # subtract the dataset-mean value in each channel
		transformer.set_raw_scale('data', 255)      # rescale from [0, 1] to [0, 255]
		transformer.set_channel_swap('data', (2,1,0))  # swap channels from RGB to BGR
		image = source
		transformed_image = transformer.preprocess('data', image)
		# copy the image data into the memory allocated for the net
		self.net.blobs['data'].data[...] = transformed_image
		### perform classification
		start = time.time()
		output = self.net.forward()
		print('time ' + str(time.time() - start))
		output_prob = output['prob'][0]  # the output probability vector for the first image in the batch
		print(output['prob'])
		print(output_prob.shape)
		print ('predicted class is:', output_prob.argmax())
		return output_prob.argmax(), output_prob[output_prob.argmax()]
