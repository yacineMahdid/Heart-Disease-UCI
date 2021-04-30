import pandas as pd
import numpy as np
from sklearn.preprocessing import Normalizer

DATA_SOURCE = "/home/yacine/Documents/Kaggle/heart_disease_eda/data/raw/heart_kaggle.csv"
FIGURE_SOURCE = "/home/yacine/Documents/Kaggle/heart_disease_eda/reports/figures/"

df = pd.read_csv(DATA_SOURCE)

y = df['target'].to_numpy()
X = df.drop('target', axis=1)

# Let's normalize everything for now without too much consideration for the categorical variables
X = Normalizer().fit_transform(X)

from sklearn.decomposition import PCA

# 2D vizualization
pca = PCA(n_components = 2)
X2D = pca.fit_transform(X)

# Amount of explained variance kept 2D
exp_variance_2d = pca.explained_variance_ratio_
print(f"2D: Total = {np.sum(exp_variance_2d)} and per components = {exp_variance_2d}")

# 3D vizualization
pca = PCA(n_components = 3)
X3D = pca.fit_transform(X)

# Amount of explained variance kept 3D
exp_variance_3d = pca.explained_variance_ratio_

import matplotlib.pyplot as plt

# Plot of the 2D PCA results
fig, ax = plt.subplots()

X2D_healthy = X2D[y == 0]
X2D_disease = X2D[y == 1]

ax.scatter(X2D_healthy[:,0], X2D_healthy[:,1], color="blue", label="healthy", edgecolors='none')
ax.scatter(X2D_disease[:,0], X2D_disease[:,1], color="red", label="disease", edgecolors='none')

ax.legend()
ax.grid(True)
ax.set_xlabel("C1")
ax.set_ylabel("C2")

fig.suptitle(f"2D PCA on Heart Disease with exp variance = {round(np.sum(exp_variance_2d), 3)}")
fig.savefig(f'{FIGURE_SOURCE}2d_pca.png')

# Plot of the 3D PCA results
fig = plt.figure()
ax3d = fig.add_subplot(projection='3d')

X3D_healthy = X3D[y == 0]
X3D_disease = X3D[y == 1]

ax3d.scatter(X3D_healthy[:,0], X3D_healthy[:,1], X3D_healthy[:,2], color="blue", label="healthy", edgecolors='none')
ax3d.scatter(X3D_disease[:,0], X3D_disease[:,1], X3D_disease[:,2], color="red", label="disease", edgecolors='none')

ax3d.legend()
ax3d.grid(True)

fig.suptitle(f"3D PCA on Heart Disease with exp variance = {round(np.sum(exp_variance_3d), 3)}")

fig.savefig(f'{FIGURE_SOURCE}3d_pca.png')
