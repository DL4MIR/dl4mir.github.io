| [Homepage](https://dl4mir.github.io) | [Course content](https://dl4mir.github.io/#course-content) |

# Convolutional Neural Networks (CNNs)

## Representing data as tensors

* So far, the data we put in a neural network has looked like a matrix `NxD`, where `N` is the number of datapoints we are using to do a gradient descent step, and `D` is the number of features in each datapoint. 

* Instead of matrices, we can use tensors to represent data with more dimensions. For example, a tensor can be used to represent datapoints that are magnitude spectrograms with dimensions `NxTxF`, where `T` is the number of time bins in each datapoint, and `F` the number of frequency bins.

* We can also use a tensor to represent datapoints as complex spectrograms if we separate the real and imaginary parts and stack them to obtain a tensor of shape `NxTxFxC`, where `C=2` and each `C` is a "channel", with channel 1 being the real part and channel 2 being the imaginary part of the complex spectrogram. 

## Generic CNN operations

* To understand how CNNs work, we must understand their origins in image recognition.

* Before CNNs, for a neural network to be able to process images, one needed to flatten all the pixels in a tensor with image datapoints (shape `NxWxHxC`) into a matrix (shape `Nx(W*H*C)`).

* 2D CNN operations were developed by [Yann LeCunn](https://en.wikipedia.org/wiki/Yann_LeCun) in the late 80s, and work as follows:
    * Do NOT flatten the image tensor and leave it in the form `NxTxFxC`
    * Use `M` filters with shape `KxLxC` to convolve with each datapoint ([visualize convolution here](https://towardsdatascience.com/intuitively-understanding-convolutions-for-deep-learning-1f6f42faee1) and [here](https://setosa.io/ev/image-kernels/))
        * `K<=T`, `L<=F`
    * Add `M` biases, one for each of the `M` filters
    * Apply a non-linearity to the output.
    * What's the shape of the output?

* A convolutional operation is very often followed by a pooling operation ([visualize the pooling operation here](https://www.geeksforgeeks.org/cnn-introduction-to-pooling-layer/)). A pooling layer further reduces redundancy in the output of a convolutional layer as follows:
    * Pass a window of size `QxR` (`Q<=T` and `R<=F`) over the convolutional output
    * In each window, keep only the largest value (max-pooling) or the mean (mean-pooling)

## CNN operations on audio signals

* When working with time-frequency representations of audio signals, the same principle proposed by Yann LeCunn can be used. 

* However, we can also use 1D convolutions on audio data with shape `NxT`.
    * What would be the shape of the convolutional filter(s) in this case?
    * How would the pooling operators look like?

## From CNN features to a neural network output

* After a series of convolution+pooling operations, the CNN hidden layer tensors must be reshaped into a matrix form (via a flattening operator) to use the usual dense layers in a neural network and produce and output. 

* As a result, a CNN can have a final output that is either a classifier (using softmax and cross entropy), a regressor (using a linear layer and MSE) or any other output+cost-function pair you like.

* Armed with all of this information, let's understand together the first CNN ever: the [LeNet](https://www.datasciencecentral.com/lenet-5-a-classic-cnn-architecture/)

## CNN filter initialization

## CNN regulatization with dropout and batchnorm

## The Adam optimization algorithm

# [Convolutional neural network](https://colab.research.google.com/github/dl4mir/assignments/blob/main/cnn.ipynb)

___

&copy; [Iran R. Roman](https://iranroman.github.io) 2022

