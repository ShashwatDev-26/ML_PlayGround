# Linear Regression with Scikit-Learn

---

This Markdown guide provides a comprehensive overview of Linear Regression using the `scikit-learn` library. It covers the mathematical foundation, core parameters, and practical implementation.

Linear Regression is a fundamental supervised learning algorithm used to model the relationship between a dependent variable (target) and one or more independent variables (features).

## 1. The Mathematical Foundation

The goal is to find the "line of best fit" by minimizing the **Residual Sum of Squares (RSS)** between the observed targets and the predictions.

The general equation is:

$$
y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \dots + \beta_nx_n + \epsilon
$$

* **$y$** : Predicted value (Target).
* **$\beta_0$** : Intercept (where the line crosses the y-axis).
* **$\beta_n$** : Coefficients (weights assigned to each feature).
* **$x_n$** : Input features.
* **$\epsilon$** : Error term (residuals).

---

## 2. Scikit-Learn Implementation

In `sklearn`, Linear Regression is handled by the `LinearRegression` class within the `linear_model` module.

### Core Syntax

**Python**

```
from sklearn.linear_model import LinearRegression

# 1. Initialize the model
model = LinearRegression(fit_intercept=True)

# 2. Train the model
model.fit(X_train, y_train)

# 3. Make predictions
predictions = model.predict(X_test)
```

---

## 3. Parameters & Attributes

Understanding the knobs you can turn and the values the model stores after training.

### Initialization Parameters

| **Parameter**         | **Type** | **Default** | **Description**                                                                                                 |
| --------------------------- | -------------- | ----------------- | --------------------------------------------------------------------------------------------------------------------- |
| **`fit_intercept`** | bool           | `True`          | Whether to calculate the intercept (**$\beta_0$**). Set to `False`if your data is already centered at zero. |
| **`copy_X`**        | bool           | `True`          | If `True`,**$X$**will be copied; otherwise, it may be overwritten during preprocessing.                           |
| **`n_jobs`**        | int            | `None`          | The number of CPU cores to use for computation.`-1`uses all available processors.                                   |
| **`positive`**      | bool           | `False`         | When set to `True`, forces the coefficients to be positive. (Useful for specific domain constraints).               |

### Post-Training Attributes

Once `model.fit()` is called, these attributes become available:

* **`model.coef_`** : The estimated coefficients (slopes) for each feature.
* **`model.intercept_`** : The independent term (intercept) in the linear model.
* **`model.n_features_in_`** : The number of features seen during the fit.

---

## 4. Model Evaluation

To see how well your line fits the data, we use the `.score()` method or specific metrics from `sklearn.metrics`.

* **$R^2$ Score (Coefficient of Determination):**
  Measured via `model.score(X, y)`. It ranges from 0 to 1; 1.0 indicates a perfect fit.
* **Mean Squared Error (MSE):**
  The average of the squares of the errors. Lower is better.

**Python**

```
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
```

---

## 5. Practical Guidance

* **Feature Scaling:** While `LinearRegression` is generally robust, it is often good practice to scale features (e.g., `StandardScaler`) if you plan to move toward regularized models like Ridge or Lasso.
* **Assumptions:** Remember that this model assumes a **linear** relationship. If your data looks like a curve, you might need Polynomial Regression.
* **Outliers:** Standard OLS (Ordinary Least Squares) is sensitive to outliers. Always visualize your data first!
