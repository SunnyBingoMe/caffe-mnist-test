You may see that it's hard to find any document about how to use the trained model of MNIST in caffe project.
If this script helps you, pls give us a star or msg, thanks!

# Installing Caffe
[dmml.nu/caffe-install](http://dmml.nu/caffe-install)

# Example Usage
`python2 mnist_test.py 2.png` (jpg also works)

Result:

![](https://github.com/SunnyBingoMe/caffe-mnist-test/raw/master/2017-12-03-15-50-27.jpg)

# Note
* written in python 2
* you may want to change `Caffe_Root` in mnist_test.py if you installed somewhere else
* the test is running on GPU by default, you can change `caffe.set_mode_gpu()` to `caffe.set_mode_cpu()` if necessary


2017

by 9crk & SunnyBingoMe
