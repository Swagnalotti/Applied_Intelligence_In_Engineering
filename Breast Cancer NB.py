from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# 1. Load dataset
breast_cancer = load_breast_cancer()
X = breast_cancer.data      # features
y = breast_cancer.target    # labels

# 2. Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=15
)

# 3. Train model
model = GaussianNB()
model.fit(X_train, y_train)

# 4. Predict
y_pred = model.predict(X_test)

# 5. Evaluate
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)