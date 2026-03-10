# **Scikit-Learn Regression Cheat Sheet**

### **1. Linear Models**

---


| **Model**                 | **Import Command**                              |
| ------------------------------- | ----------------------------------------------------- |
| **Linear Regression**     | `from sklearn.linear_model import LinearRegression` |
| **Ridge Regression (L2)** | `from sklearn.linear_model import Ridge`            |
| **Lasso Regression (L1)** | `from sklearn.linear_model import Lasso`            |
| **ElasticNet**            | `from sklearn.linear_model import ElasticNet`       |
| **Bayesian Ridge**        | `from sklearn.linear_model import BayesianRidge`    |
| **SGD Regressor**         | `from sklearn.linear_model import SGDRegressor`     |

### **2. Non-Linear & Tree-Based Models**

---

These models capture complex, non-linear patterns and are generally more robust to outliers.

| **Model**                | **Import Command**                                       |
| ------------------------------ | -------------------------------------------------------------- |
| **Decision Tree**        | `from sklearn.tree import DecisionTreeRegressor`             |
| **Random Forest**        | `from sklearn.ensemble import RandomForestRegressor`         |
| **Extra Trees**          | `from sklearn.ensemble import ExtraTreesRegressor`           |
| **AdaBoost**             | `from sklearn.ensemble import AdaBoostRegressor`             |
| **Gradient Boosting**    | `from sklearn.ensemble import GradientBoostingRegressor`     |
| **HistGradientBoosting** | `from sklearn.ensemble import HistGradientBoostingRegressor` |

### **3. Support Vector & Kernel-Based Models**

---

Effective in high-dimensional spaces or when using specific kernel tricks.

| **Model**                | **Import Command**                                          |
| ------------------------------ | ----------------------------------------------------------------- |
| **SVR (Support Vector)** | `from sklearn.svm import SVR`                                   |
| **NuSVR**                | `from sklearn.svm import NuSVR`                                 |
| **Linear SVR**           | `from sklearn.svm import LinearSVR`                             |
| **Gaussian Process**     | `from sklearn.gaussian_process import GaussianProcessRegressor` |
| **Kernel Ridge**         | `from sklearn.kernel_ridge import KernelRidge`                  |

### **4. Neighbors & Neural Networks**

---

Alternative approaches based on data proximity or simplified biological neurons.

| **Model**                      | **Import Command**                                   |
| ------------------------------------ | ---------------------------------------------------------- |
| **K-Nearest Neighbors**        | `from sklearn.neighbors import KNeighborsRegressor`      |
| **Radius Neighbors**           | `from sklearn.neighbors import RadiusNeighborsRegressor` |
| **MLP Regressor (Neural Net)** | `from sklearn.neural_network import MLPRegressor`        |

---

### **5. Robust & Specialized Regressors**

---

Designed to handle outliers or specific statistical distributions.

| **Model**               | **Import Command**                               |
| ----------------------------- | ------------------------------------------------------ |
| **Huber Regressor**     | `from sklearn.linear_model import HuberRegressor`    |
| **RANSAC Regressor**    | `from sklearn.linear_model import RANSACRegressor`   |
| **Theil-Sen Regressor** | `from sklearn.linear_model import TheilSenRegressor` |
| **Poisson Regressor**   | `from sklearn.linear_model import PoissonRegressor`  |
| **Tweedie Regressor**   | `from sklearn.linear_model import TweedieRegressor`  |

# Scikit-Learn Classification Cheat Sheet

---

### **1. Linear & Baseline Classifiers**

Ideal for high-dimensional text data or as a fast baseline to test your dataset's "linearity."

| **Model**               | **Import Command**                                         |
| ----------------------------- | ---------------------------------------------------------------- |
| **Logistic Regression** | `from sklearn.linear_model import LogisticRegression`          |
| **Ridge Classifier**    | `from sklearn.linear_model import RidgeClassifier`             |
| **SGD Classifier**      | `from sklearn.linear_model import SGDClassifier`               |
| **Passive Aggressive**  | `from sklearn.linear_model import PassiveAggressiveClassifier` |
| **Perceptron**          | `from sklearn.linear_model import Perceptron`                  |

---

### **2. Tree & Ensemble Classifiers**

These are generally the most powerful models for structured/tabular data. They handle non-linear relationships and feature interactions automatically.

| **Model**                | **Import Command**                                        |
| ------------------------------ | --------------------------------------------------------------- |
| **Decision Tree**        | `from sklearn.tree import DecisionTreeClassifier`             |
| **Random Forest**        | `from sklearn.ensemble import RandomForestClassifier`         |
| **Extra Trees**          | `from sklearn.ensemble import ExtraTreesClassifier`           |
| **AdaBoost**             | `from sklearn.ensemble import AdaBoostClassifier`             |
| **Gradient Boosting**    | `from sklearn.ensemble import GradientBoostingClassifier`     |
| **HistGradientBoosting** | `from sklearn.ensemble import HistGradientBoostingClassifier` |

---

### **3. Support Vector & Kernel Models**

Excellent for finding the "optimal margin" between classes, especially when you have more features than samples.

| **Model**                | **Import Command**              |
| ------------------------------ | ------------------------------------- |
| **SVC (Support Vector)** | `from sklearn.svm import SVC`       |
| **Linear SVC**           | `from sklearn.svm import LinearSVC` |
| **Nu-SVC**               | `from sklearn.svm import NuSVC`     |

---

### **4. Distance & Probability Based**

These rely on either the "closeness" of data points or Bayes' Theorem for probabilistic classification.

| **Model**                | **Import Command**                               |
| ------------------------------ | ------------------------------------------------------ |
| **K-Nearest Neighbors**  | `from sklearn.neighbors import KNeighborsClassifier` |
| **Gaussian Naive Bayes** | `from sklearn.naive_bayes import GaussianNB`         |
| **Multinomial NB**       | `from sklearn.naive_bayes import MultinomialNB`      |
| **Bernoulli NB**         | `from sklearn.naive_bayes import BernoulliNB`        |
| **MLP Classifier**       | `from sklearn.neural_network import MLPClassifier`   |

---

### **5. Specialized Classifiers**

Used for specific data types or multi-output problems.

| **Model**                     | **Import Command**                                                    |
| ----------------------------------- | --------------------------------------------------------------------------- |
| **LDA (Linear Discriminant)** | `from sklearn.discriminant_analysis import LinearDiscriminantAnalysis`    |
| **QDA (Quadratic Disc.)**     | `from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis` |
| **One Vs Rest**               | `from sklearn.multiclass import OneVsRestClassifier`                      |
| **Voting Classifier**         | `from sklearn.ensemble import VotingClassifier`                           |

# Scikit-Learn Clustring Cheat Sheet

Clustering is an **unsupervised learning** technique used to group similar data points together when you don't have pre-defined labels. Unlike classification, the model tries to find "natural" structures in the data.

---

## **Scikit-Learn Clustering Cheat Sheet**

### **1. Partitioning & Centroid-Based**

These models divide data into non-overlapping subsets (clusters) by minimizing the distance between points and a central point.

| **Model**                | **Import Command**                            |
| ------------------------------ | --------------------------------------------------- |
| **K-Means**              | `from sklearn.cluster import KMeans`              |
| **Mini-Batch K-Means**   | `from sklearn.cluster import MiniBatchKMeans`     |
| **Affinity Propagation** | `from sklearn.cluster import AffinityPropagation` |
| **Mean Shift**           | `from sklearn.cluster import MeanShift`           |

---

### **2. Density-Based & Spatial**

These are excellent for finding clusters of arbitrary shapes and identifying "noise" or outliers that don't belong to any group.

| **Model**   | **Import Command**                |
| ----------------- | --------------------------------------- |
| **DBSCAN**  | `from sklearn.cluster import DBSCAN`  |
| **HDBSCAN** | `from sklearn.cluster import HDBSCAN` |
| **OPTICS**  | `from sklearn.cluster import OPTICS`  |

---

### **3. Hierarchical & Connectivity-Based**

These build a tree of clusters (dendrogram) by either merging small clusters (agglomerative) or splitting large ones.

| **Model**                 | **Import Command**                                |
| ------------------------------- | ------------------------------------------------------- |
| **Agglomerative**         | `from sklearn.cluster import AgglomerativeClustering` |
| **Feature Agglomeration** | `from sklearn.cluster import FeatureAgglomeration`    |
| **BIRCH**                 | `from sklearn.cluster import Birch`                   |

---

### **4. Probabilistic & Manifold-Based**

These use statistical distributions or graph-based approaches to determine cluster membership.

| **Model**               | **Import Command**                           |
| ----------------------------- | -------------------------------------------------- |
| **Gaussian Mixture**    | `from sklearn.mixture import GaussianMixture`    |
| **Spectral Clustering** | `from sklearn.cluster import SpectralClustering` |
| **Bisecting K-Means**   | `from sklearn.cluster import BisectingKMeans`    |

---
