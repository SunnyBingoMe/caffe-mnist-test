#!/usr/bin/env python2

# usage: python2 mnist_test.py 2.png

# author:  9crk
# updated: SunnyBingoMe
# time:    2017-03-22
# update:  2017-12-03

Caffe_Root = '/root/caffe'

import sys
sys.path.append(Caffe_Root + '/python')

import caffe
import numpy as np
import cv2
#import sys
#import Image
#import matplotlib.pyplot as plt

model = Caffe_Root + '/examples/mnist/lenet.prototxt';
weights = Caffe_Root + '/examples/mnist/lenet_iter_10000.caffemodel';
net = caffe.Net(model,weights,caffe.TEST);
caffe.set_mode_gpu()
#img = caffe.io.load_image(sys.argv[1], color=False)
img = cv2.imread(sys.argv[1],0)
if img.shape != [28,28]:
    img2 = cv2.resize(img,(28,28))
    img = img2.reshape(28,28,-1);
else:
    img = img.reshape(28,28,-1);
#revert the image,and normalize it to 0-1 range
img = 1.0 - img/255.0
possibility_listing = net.forward_all(data=np.asarray([img.transpose(2,0,1)]))

print "==== Possibilities of 0~9: "
print possibility_listing['prob'][0]

print "==== The digit is: "
print possibility_listing['prob'][0].argmax()
