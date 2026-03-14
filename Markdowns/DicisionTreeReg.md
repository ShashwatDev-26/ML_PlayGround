
# Decision Tree Regressor with Scikit-Learn

---

This guide provides a structured Markdown breakdown of the **Decision Tree Regressor** using `scikit-learn`. Unlike Linear Regression, Decision Trees handle non-linear relationships by splitting data into smaller and smaller subsets.

A Decision Tree Regressor breaks down a dataset into smaller subsets while at the same time an associated decision tree is incrementally developed. The final result is a tree with **decision nodes** and  **leaf nodes** .

## 1. How it Works

Instead of fitting a line, the regressor predicts the value of a target variable by learning simple decision rules inferred from the data features. For regression, the prediction for a leaf node is usually the **mean** of the target values in that node.

---

## 2. Scikit-Learn Implementation

In `sklearn`, this is found in the `tree` module.

### Core Syntax

**Python**

```
from sklearn.tree import DecisionTreeRegressor

# 1. Initialize the model
# Using a max_depth to prevent overfitting
regressor = DecisionTreeRegressor(max_depth=5, random_state=42)

# 2. Train the model
regressor.fit(X_train, y_train)

# 3. Predict
predictions = regressor.predict(X_test)
```

---

## 3. Key Parameters

Decision Trees are prone to **overfitting** (memorizing the training data). These parameters help control the complexity of the tree.

| **Parameter**             | **Default**   | **Description**                                                                                                        |
| ------------------------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **`criterion`**         | `"squared_error"` | The function to measure the quality of a split. Options include `"absolute_error"`,`"friedman_mse"`, and `"poisson"`.  |
| **`max_depth`**         | `None`            | The maximum depth of the tree. If `None`, nodes expand until leaves are pure.**Crucial for preventing overfitting.** |
| **`min_samples_split`** | `2`               | The minimum number of samples required to split an internal node.                                                            |
| **`min_samples_leaf`**  | `1`               | The minimum number of samples required to be at a leaf node. Higher values smooth the model.                                 |
| **`max_features`**      | `None`            | The number of features to consider when looking for the best split.                                                          |
| **`random_state`**      | `None`            | Ensures the splits are reproducible.                                                                                         |

---

## 4. Strengths & Weaknesses

### Pros

* **Interpretability:** You can visualize the tree and see exactly why a prediction was made.
* **No Scaling Required:** Unlike Linear Regression, trees are invariant to the scale of features.
* **Handles Non-linearity:** Excellent at capturing complex, non-linear patterns.

### Cons

* **Overfitting:** High tendency to create over-complex trees that do not generalize well.
* **Instability:** Small changes in the data can lead to a completely different tree structure.
* **Not Continuous:** Predictions are piecewise constant; it cannot predict values outside the range seen in training data.

---

## 5. Visualizing the Tree

One of the coolest features of `sklearn` is the ability to export the tree as an image or text.

**Python**

```
from sklearn.tree import export_text

# Print the logic of the tree
tree_rules = export_text(regressor, feature_names=list(X.columns))
print(tree_rules)
```

---

## 6. Pro-Tip: Pruning

To keep your tree from getting "out of control," you can use  **Cost Complexity Pruning** . The parameter `ccp_alpha` allows you to penalize the complexity of the tree; a larger alpha increases the amount of pruning.
