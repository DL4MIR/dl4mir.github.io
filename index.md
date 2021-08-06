<p align="txt-align: center;">
  <img src="https://scontent-lga3-2.xx.fbcdn.net/v/t1.6435-9/99423691_3132529343476526_8281982353090281472_n.jpg?_nc_cat=107&ccb=1-3&_nc_sid=6e5ad9&_nc_ohc=D12Zb03fiMMAX86knWj&_nc_ht=scontent-lga3-2.xx&oh=ab2dd4b9a4a2e0542e087d91115e6d18&oe=612C7164" style="max-width: 100%; height: auto;" />
</p>
<center> <h1> Deep Learning for Music Information Retrieval (part 1) </h1> </center>

## 2021 CCRMA workshop (Aug 2nd - Aug 6th)

This workshop covers the industry-standard methods to develop deep neural network architectures for digital audio. Throughout five intensive days of study, we will cover technical, mathematical, and practical principles that deep learning researchers use everyday in the real world.

The learning material has been designed for people who want to gain serious exposure to deep neural networks applied to digital audio problems. It is assumed that participants have previous knowledge of linear algebra, differential calculus, and programming experience with python.

---

## Day 1
    
- [MIR review and software tools](https://colab.research.google.com/github/elenatheodora/CCRMA-MIR-2021/blob/main/NB1_MIR_Review_%26_Tools.ipynb)
- [Loading datasets and working with them](https://colab.research.google.com/github/DL4MIR/dl4mir.github.io/blob/main/some_audio_datasets.ipynb)
- Things to do before day 2
    - Review/learn [matrix multiplication](https://www.mathsisfun.com/algebra/matrix-multiplying.html)
    - Read about the [binary cross entropy](https://towardsdatascience.com/understanding-binary-cross-entropy-log-loss-a-visual-explanation-a3ac6025181a)

## Day 2

- Cross validation
    - [Read here for an overview](https://machinelearningmastery.com/k-fold-cross-validation/)
- [Arco vs pizzicato classification](https://colab.research.google.com/github/DL4MIR/dl4mir.github.io/blob/main/arco_vs_pizzicato_classification.ipynb) (logistic regression)
- Things to do before day 3
    - Read about the [softmax function](https://deepai.org/machine-learning-glossary-and-terms/softmax-layer)

## Day 3

- [Logistic regression with Tensorflow 2](https://colab.research.google.com/github/DL4MIR/dl4mir.github.io/blob/main/arco_vs_pizzicato_class_tf2.ipynb)
- [Hit song prediction](https://colab.research.google.com/github/elenatheodora/CCRMA-MIR-2021/blob/main/CCRMA_MIR_Hit_Prediction.ipynb)
    - supplemental reading: [NYT Songs of the Summer](https://www.nytimes.com/interactive/2018/08/09/opinion/do-songs-of-the-summer-sound-the-same.html?smid=pl-share)
- Things to do before day 4
    - Read this tutorial on [Neural Networks and their building blocks](https://victorzhou.com/blog/intro-to-neural-networks/)

## Day 4

- [Softmax in keras](https://colab.research.google.com/github/DL4MIR/dl4mir.github.io/blob/main/softmax_in_keras.ipynb)
- Things to read before day 5
    - [convolutional neural networks and their building blocks](https://cs231n.github.io/convolutional-networks/)
    - [Wavenet convolution](https://deepmind.com/blog/article/wavenet-generative-model-raw-audio)
    - [MusicVAE](https://magenta.tensorflow.org/music-vae)

## Day 5

- [MedleyDB](https://colab.research.google.com/github/elenatheodora/CCRMA-MIR-2021/blob/main/MedleyDB/CCRMA_MIR_MedleyDB.ipynb)
    - [github repo](https://github.com/elenatheodora/CCRMA-MIR-2021/tree/main/MedleyDB)
- [Wavenet audio generation](https://colab.research.google.com/github/vincentherrmann/pytorch-wavenet/blob/master/WaveNet_demo.ipynb) (it's broken, but can we fix it?)


---

## Logistics

- Class meets: 
    - in the morning from 9:30AM to 11AM (PDT)
    - in the afternoon from 1:30PM to 3PM (PDT)
- Class will be recorded for people to watch asynchronously
- Create a Google account. We will use Google Colaboratory
    - If you live in a place without access to google colab, try using a VPN, or create a github account and talk to the instructors for working alternatives
- How to set up your python environment in your personal computer:
    - [Install pyenv in your Mac](https://www.liquidweb.com/kb/how-to-install-pyenv-on-ubuntu-18-04/)
    - [Install pyenv in Ubuntu (linux)](https://www.liquidweb.com/kb/how-to-install-pyenv-on-ubuntu-18-04/)
    - [Install WSL if you use Windows](https://docs.microsoft.com/en-us/learn/modules/get-started-with-windows-subsystem-for-linux/2-enable-and-install) and follow the steps for Ubuntu (linux) above.
    - Packages to install with pip (make sure you install the latest version for python 3.6 or greater):
        - librosa
        - tensorflow
        - numpy
        - matplotlib
        - scipy
        - sklearn
        - jupyter
        - IPython 

## How to get the small version of the GTZAN dataset that we are using in this workshop:
1. install [`gdown` using pip](https://pypi.org/project/gdown/)
2. run this command in your terminal `gdown --id 1wAjDwxWMSjrWz4-tbQyWIyqGLMVetWed`
3. and unzip the file `unzip gtzan.zip`


---

## Instructors

Elena Georgieva

email: egeorgie [at] ccrma.stanford.edu

Iran R. Roman

email: iran [at] ccrma.stanford.edu

