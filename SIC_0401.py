import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# dataset 1
X1, label1 = make_blobs(n_samples=100, n_features=2, centers=2, cluster_std=5, random_state=123)
plt.scatter(X1[:, 0], X1[:, 1], c=label1, alpha=0.7)
plt.title('Dataset #1 : Original')
plt.show()

# dataset 2
X2, label2 = make_blobs(n_samples=100, n_features=2, centers=3, cluster_std=1, random_state=321)
plt.scatter(X2[:, 0], X2[:, 1], c=label2, alpha=0.7)
plt.title('Dataset #2 : Original')
plt.show()

# dataset 1 and 2 cluster
kmeans = KMeans(n_clusters=2, random_state=123)
kmeans.fit(X1)
myColors = {0: 'red', 1: 'green', 2: 'blue'}
plt.scatter(X1[:, 0], X1[:, 1], c=pd.Series(kmeans.labels_).apply(lambda x: myColors[x]), alpha=0.7)
plt.title('Dataset #1 : K-Means 2 cluster')
plt.show()

# dataset 1 and 3 cluster
kmeans = KMeans(n_clusters=3, random_state=123)
kmeans.fit(X1)
plt.scatter(X1[:, 0], X1[:, 1], c=pd.Series(kmeans.labels_).apply(lambda x: myColors[x]), alpha=0.7)
plt.title('Dataset #1 : K-Means 3 cluster')
plt.show()

# dataset 2 and 2 cluster
kmeans = KMeans(n_clusters=2, random_state=123)
kmeans.fit(X2)
plt.scatter(X2[:, 0], X2[:, 1], c=pd.Series(kmeans.labels_).apply(lambda x: myColors[x]), alpha=0.7)
plt.title('Dataset #2 : K-Means 2 cluster')
plt.show()

# dataset 2 and 3 cluster
kmeans = KMeans(n_clusters=3, random_state=123)
kmeans.fit(X2)
plt.scatter(X2[:, 0], X2[:, 1], c=pd.Series(kmeans.labels_).apply(lambda x: myColors[x]), alpha=0.7)
plt.title('Dataset #2 : K-Means 3 cluster')
plt.show()
