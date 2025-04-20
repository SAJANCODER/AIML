#implementation of k-mean cluster
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

#1.)load the dataset
df=pd.read_csv("your.csv")

x=df[['figure1'],['figure2']]
x=x.dropna() #removes the (nan) from your data
#2.)preprocessing
scaler = StandardScaler()
x_scaler = scaler.fit_transform(x)

saj=[]
k=range(1,11)
for k in k:
    kmeans = KMeans(n_clusters=k,init='k-means++',random_state=42)
    kmeans.fit(x_scaler)
    saj.append(kmeans.inertia_)
plt.figure(figsize(8,11))
plt.plot(k,saj,'bo-')
plt.title("clustering")
plt.xlabel("figure1")
plt.ylabel("figure2")
plt.grid(True)
plt.show()

kmeans = KMeans(n_clusters=3,init="k-means++",random_state=42)
cluster = kmeans.fit_predict(x_scaler)
df['cluster'] = cluster
plt.figure(figsize(8,11))
plt.scatter(x_scaler[:,0],x_scaler[:,1],c=cluster)
plt.show()


