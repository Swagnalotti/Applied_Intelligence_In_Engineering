from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_wine

# Load Wine dataset
wine = load_wine()

# Features: [alcohol, hue, proline, ... etc]
X = wine.data

# Target: 0 = class0, 1 = class1, 2 = class2
y = wine.target

# 1. Split into training (60%) and temporary data (40%)
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)

# 2. Split temporary data into validation (20%) and testing (20%)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# 3. Try different K values using validation data
for k in [1, 2, 3, 4, 5, 6]:
    model = KNeighborsClassifier(n_neighbors=k)
    # Learn patterns from training data
    model.fit(X_train, y_train)
    # Predict validation samples
    val_prediction = model.predict(X_val)
    # Measure accuracy
    accuracy = accuracy_score(y_val, val_prediction)
    print("K =", k, "Validation Accuracy =", accuracy)