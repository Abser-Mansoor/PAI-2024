import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Part 1: K-means Clustering on Iris Dataset

# Load the Iris dataset
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target

inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(iris.data)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.show()

kmeans = KMeans(n_clusters=3, random_state=42)
iris_df['kmeans_cluster'] = kmeans.fit_predict(iris.data)

plt.figure(figsize=(8, 6))
plt.scatter(iris.data[:, 0], iris.data[:, 1], c=iris_df['kmeans_cluster'], cmap='viridis')
plt.title('K-means Clustering on Iris Dataset')
plt.xlabel('Sepal length (cm)')
plt.ylabel('Sepal width (cm)')
plt.colorbar()
plt.show()

# Part 2: PCA on Handwritten Digits Using Breast Cancer Dataset

# Load the breast cancer dataset
cancer = datasets.load_breast_cancer()

cancer_df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
cancer_df['label'] = cancer.target

scaler = StandardScaler()
cancer_scaled = scaler.fit_transform(cancer_df.drop('label', axis=1))

pca = PCA(n_components=2)
pca_result = pca.fit_transform(cancer_scaled)

print(f"Variance explained by the first 2 principal components: {np.sum(pca.explained_variance_ratio_):.2f}")

# Create a scatter plot of the PCA results
plt.figure(figsize=(8, 6))
sns.scatterplot(x=pca_result[:, 0], y=pca_result[:, 1], hue=cancer_df['label'], palette='Set1', s=100, edgecolor='k')
plt.title('PCA of Breast Cancer Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(title='Label', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
