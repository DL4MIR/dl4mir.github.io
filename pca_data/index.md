| [Homepage](https://dl4mir.github.io) | [Course content](https://dl4mir.github.io/#course-content) |

# Datasets and dimensionality reduction

## Audio datasets

* MIR and Deep Learning are "data-driven".

* This means that we "do as the data says", and as a result we need large amounts of "datapoints" (in the order of thousands) to find "the real meaning that the data is trying to convey".

* The definition of a datapoint depends on the goal or research question:
    * it could be as short as a milliseconds-long recording of a vowel (if the goal is, for example, to identify or generate vowels), or 
    * as long as the entire duration of a piece of music (if the goal is, for example, generation of entire songs that closely follow the style of an artist).

* Fortunately, large amounts of data have already been curated by researchers and are easily accesible. 

* [mirdata](https://mirdata.readthedocs.io), [soundata](https://soundata.readthedocs.io), and [micarraylib](https://github.com/micarraylib/micarraylib) are examples of open-source projects that make large amounts of data readily available for data-driven research with audio.

## Dimensionality reduction with principal components analysis (PCA)

* We have discussed how feature extraction can serve as a technique to achieve dimensionality reduction. 

* The audio features we have studied so far are "hand-picked", which can result in a flawed research methodology (why?)

* The [principal components analysis](https://en.wikipedia.org/wiki/Principal_component_analysis) is an unsupervised learning method to avoid "hand-picking". 

* It is unsupervised because it can identify structure in data without introducing human bias.

* PCA can reduce the dimensionality of high-dimensional datapoints in a dataset by projecting the data (via dot product) onto a few vectors that are orthogonal to each other, and each vector minimizes the mean squared error from the points.

* The steps needed to carry out PCA (assuming all datapoints are stacked as rows in a matrix `X`) can be summarized as:
    1. Standardized the dataset by zero-centering the features and making their variance equal to 1. 
        * In the specific case of audio, sometimes we "standardize" the data differently. How and why?
    2. Calculate the covariance matrix of the standardized data.
    3. Find the eigenvalues and eigenvectors of the resulting covariance matrix and sort them by size of the corresponding eigenvalue.
    4. Define a matrix whose columns are the N eigenvectors that correspond to the principal components that we want to calculate (usually the first 2, 3, 4, etc.).
    5. Project the standardized dataset onto the matrix (via matrix dot product).

* The relative magnitude of the covariance matrix's eigenvalues represent the proportion of variance that each eigenvalue-eigenvector pair can capture in the data.

* There are python libraries to carry out PCA without having to do all these steps by hand. The most popular implementation is [sklearn's PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html).

* Besides PCA, there are other similar methods to reduce data dimensionality. Examples include [t-SNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html) or [UMAP](https://umap-learn.readthedocs.io/en/latest/basic_usage.html).

# [mirdata and PCA](https://colab.research.google.com/github/dl4mir/assignments/blob/main/pca.ipynb)

___

&copy; [Iran R. Roman](https://iranroman.github.io) & [Camille Noufi](http://camillenoufi.com) 2022
