from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np

# 1. Load dataset
breast_cancer = load_breast_cancer()
X = breast_cancer.data      # features
y = breast_cancer.target    # labels

# 2. Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(
 X, y, test_size=0.2, random_state=42
)

# 3. Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 4. Predict
y_pred = model.predict(X_test)

# 5. Evaluate
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Plot the tree
plt.figure(figsize=(12, 8))
plot_tree(
    model,
    feature_names=breast_cancer.feature_names,
    class_names=breast_cancer.target_names,
    filled=True
)
plt.show()

# Plot feature importance
n_features = breast_cancer.data.shape[1]
plt.barh(range(n_features), model.feature_importances_, align='center')
plt.yticks(np.arange(n_features), breast_cancer.feature_names)
plt.xlabel("Feature importance")
plt.ylabel("Feature")
plt.show()