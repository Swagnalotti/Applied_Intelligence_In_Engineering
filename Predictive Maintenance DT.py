from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np

# 1. Load dataset
ai4i_2020_predictive_maintenance_dataset = fetch_ucirepo(id=601)
X = ai4i_2020_predictive_maintenance_dataset.data.features
X['Type'] = X['Type'].map({'L': 0, 'M': 1, 'H': 2})
y = ai4i_2020_predictive_maintenance_dataset.data.targets['Machine failure']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Plot the tree
plot_tree(model, feature_names=X.columns, class_names=['No failure', 'Failure'], filled=True)
#plot_tree(model, feature_names=X.columns, class_names=y.columns, filled=True)
plt.savefig("Decision Tree.png", dpi=600, bbox_inches='tight')
plt.show()

# Plot feature importance
n_features = ai4i_2020_predictive_maintenance_dataset.data.features.shape[1]
plt.barh(range(n_features), model.feature_importances_, align='center')
plt.yticks(np.arange(n_features), X.columns)
plt.xlabel("Feature importance")
plt.ylabel("Feature")
plt.tight_layout()
plt.savefig("Feature Importance.png", dpi=600, bbox_inches='tight')
plt.show()