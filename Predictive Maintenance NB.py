from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# 1. Load dataset
ai4i_2020_predictive_maintenance_dataset = fetch_ucirepo(id=601)
X = ai4i_2020_predictive_maintenance_dataset.data.features
X['Type'] = X['Type'].map({'L': 0, 'M': 1, 'H': 2})
for target in ['Machine failure', 'TWF', 'HDF', 'PWF', 'OSF', 'RNF']:
    y = ai4i_2020_predictive_maintenance_dataset.data.targets[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = GaussianNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)