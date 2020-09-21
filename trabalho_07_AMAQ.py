import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv('observacoes.csv',sep=',',header=None)
data=np.array(data,dtype=np.float32)
n = 4

#kmeans = KMeans(n_clusters = n, init='k-means++')
kmeans = KMeans(n_clusters = n, init='random')
kmeans.fit(data)
center = kmeans.cluster_centers_
distance = kmeans.fit_transform(data)
labels = kmeans.labels_
print('Numero de iterações:',kmeans.n_iter_)
print('Centro:')
print(center)

for i in range(n):
    plt.scatter(center[i][0],center[i][1], color='black', marker='*')

for i in range(len(data)):
    if(labels[i]==0):
        plt.scatter(data[i][0],data[i][1], color='green', marker='.')
    if(labels[i]==1):
        plt.scatter(data[i][0],data[i][1], color='orange', marker='.')
    if(labels[i]==2):
        plt.scatter(data[i][0],data[i][1], color='blue', marker='.')
    if(labels[i]==3):
        plt.scatter(data[i][0],data[i][1], color='red', marker='.')

plt.show()

green= []
orange = []
blue = []
red = []

for i in range(len(distance)):
    erro = distance[i][labels[i]]**2
    if(labels[i]==0):
        green.append(erro)
    if(labels[i]==1):
        orange.append(erro)
    if(labels[i]==2):
        blue.append(erro)
    if(labels[i]==3):
        red.append(erro)

green.sort(reverse=True)
orange.sort(reverse=True)
blue.sort(reverse=True)
red.sort(reverse=True)

plt.plot(green,color='green')
plt.plot(orange,color='orange')
plt.plot(blue,color='blue')
plt.plot(red,color='red')

plt.show()