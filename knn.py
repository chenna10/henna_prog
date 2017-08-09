'''
Created on Jun 1, 2017

@author: che
'''
import numpy as np
import matplotlib.pyplot
from matplotlib.colors import ListedColormap
from sklearn import neighbors

n_neighbors = 13

# import some data to play with
f = open("Test2.txt")
f.readline()  # skip the header
data = np.loadtxt(f)

X = data[:, 1:]  # select columns 1 through end
y = data[:, 2]   # select column 0, the stock price


h = .1  # step size in the mesh

# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

for weights in ['uniform', 'distance']:
    # we create an instance of Neighbours Classifier and fit the data.
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + .009
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    matplotlib.pyplot.figure()
    matplotlib.pyplot.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    matplotlib.pyplot.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
    matplotlib.pyplot.xlim(xx.min(), xx.max())
    matplotlib.pyplot.ylim(yy.min(), yy.max())
    matplotlib.pyplot.title("3-Class classification (k = %i, weights = '%s')"
              % (n_neighbors, weights))

matplotlib.pyplot.show()