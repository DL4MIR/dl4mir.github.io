| [Homepage](https://dl4mir.github.io) | [Course content](https://dl4mir.github.io/#course-content) |

# Feedforward neural networks

## Recapituation of supervised learning systems studied thus far

* We have studied how linear regression can help us predict continuous values via a linear relationship with a set of features.

* We have also studied how we can use logistic regression and softmax to classify datapoints into different discrete categories.

* The equations for these systems are:
    * Linear regression <img src="https://render.githubusercontent.com/render/math?math=\hat{y}_i = x_iW %2B b \in \mathbb{R}^{1x1}">
    * Logistic regression <img src="https://render.githubusercontent.com/render/math?math=\hat{y}_i = \sigma(x_iW %2B b) = \frac{1}{1 %2B e^{-(x_iW %2B b)}} \in \mathbb{R}^{1x1}">
    * Softmax <img src="https://render.githubusercontent.com/render/math?math=\hat{y}_i=softmax(x_iW %2B b) = \frac{e^{x_iW %2B b}}{\sum_je^{x_iW %2B b}} \in \mathbb{R}^{1xC}">
 
* If you notice, we have 
    * used <img src="https://render.githubusercontent.com/render/math?math=W"> and <img src="https://render.githubusercontent.com/render/math?math=b"> to transform the input data <img src="https://render.githubusercontent.com/render/math?math=x_i">.
    * the result of this transformation gets further processed by a function to get the output <img src="https://render.githubusercontent.com/render/math?math=\hat{y}_i">.

* However, we can apply more transformations to the input data before reaching the final output. 

## Neural network with one hidden layer

* Instead of computing <img src="https://render.githubusercontent.com/render/math?math=\hat{y}_i"> directly, we can use input data <img src="https://render.githubusercontent.com/render/math?math=x_i"> to compute a "hidden state" <img src="https://render.githubusercontent.com/render/math?math=h = f(x_iW %2B b) \mathbb{R}^{1xH}">. 

* The function <img src="https://render.githubusercontent.com/render/math?math=f()"> that gives the hidden state is non-linear and arbitrary (although some non-linearities are more commonly used).

* If we used this hidden state with the systems we have studied so far in this class, their equations would be:
    * Linear regression neural network <img src="https://render.githubusercontent.com/render/math?math=\hat{y}_i = h_iW %2B b \in \mathbb{R}^{1x1}">
    * Logistic regression neural network <img src="https://render.githubusercontent.com/render/math?math=\hat{y}_i = \sigma(h_iW %2B b) = \frac{1}{1 %2B e^{-(h_iW %2B b)}} \in \mathbb{R}^{1x1}">
    * Softmax neural network <img src="https://render.githubusercontent.com/render/math?math=\hat{y}_i=softmax(h_iW %2B b) = \frac{e^{h_iW %2B b}}{\sum_je^{h_iW %2B b}} \in \mathbb{R}^{1xC}">

* These equations represent three different neural networks, each of which could be used for different tasks and applications.

## The choice of non-linearity

* Today, the most commonly used non-linearity is ReLU (Rectified Linear Unit) or [some of its variants](https://en.wikipedia.org/wiki/Rectifier_(neural_networks)).

* Other useful non-linearities include sigmoid and the hyperbolic tangent (tanh).

* Advantages of ReLU over other non-linearities include:
    * the fact that it does not "saturate"
    * its computation does not involve an exponentiation and instead is a "thresholding" operator
    * it results in the network learning a sparse representation

## Feedforward neural networks

* In the previous sections we talked about a neural network with one hidden layer.

* However, we can have more hidden layers. In fact, you can have as many as necessary (how do you know how many are necessary?).

* The resulting compuational architecture is known as a feedforward neural network. 


# [Feedforward neural network](https://colab.research.google.com/github/dl4mir/assignments/blob/main/nn.ipynb)

___

&copy; [Iran R. Roman](https://iranroman.github.io) & [Camille Noufi](http://camillenoufi.com) 2022

