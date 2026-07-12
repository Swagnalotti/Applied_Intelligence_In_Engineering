from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 1. Load dataset
ai4i_2020_predictive_maintenance_dataset = fetch_ucirepo(id=601)
X = ai4i_2020_predictive_maintenance_dataset.data.features
X['Type'] = X['Type'].map({'L': 0, 'M': 1, 'H': 2})
y = ai4i_2020_predictive_maintenance_dataset.data.targets['Machine failure']
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5)
for k in range(1, 41):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    val_prediction = model.predict(X_val)
    accuracy = accuracy_score(y_val, val_prediction)
    print("K =", k, "Validation Accuracy =", accuracy)