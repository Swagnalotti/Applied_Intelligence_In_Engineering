from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import mean_squared_error, accuracy_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




# 1. Load dataset
predictive_maintenance = pd.read_csv('predictive_maintenance.csv')
X = predictive_maintenance.drop(columns=['UDI', 'Product ID', 'Target', 'Failure Type'])
X["Type"] = X["Type"].map({
    "L": 0,
    "M": 1,
    "H": 2
})

y = predictive_maintenance['Target']

# 2. Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Train model
model = GaussianNB()
model.fit(X_train, y_train)

# 4. Predict
y_pred = model.predict(X_test)

# 5. Evaluate
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


# print("Training Features:\n", X_train)
# print("Testing Labels:\n", y_test)















# # KNN
#
# # K Nearest Neighbor
# # 1. Split into training (60%) and temporary data (40%)
# X_train, X_temp, y_train, y_temp = train_test_split( X, y, test_size=0.4, random_state=42)
#
# # 2. Split temporary data into validation (20%) and testing (20%)
# X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
#
# # 3. Try different K values using validation data
# for k in [1, 3, 5]:
#     model = KNeighborsRegressor(n_neighbors=k)
#     # Store values for calculation
#     model.fit(X_train, y_train)
#     val_prediction = model.predict(X_val)
#     error = mean_squared_error(y_val, val_prediction)
#     print("K =", k, "Validation Error =", error)
#
# final_model = KNeighborsRegressor(n_neighbors=1)
# final_model.fit(X_train, y_train)
# test_prediction = final_model.predict(X_test)
# test_error = mean_squared_error(y_test, test_prediction)
# print("Test Error:", test_error)
#
# # Iris
# # 1. Split into training (60%) and temporary data (40%)
# X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
#
# # 2. Split temporary data into validation (20%) and testing (20%)
# X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
#
# # 3. Try different K values using validation data
# for k in [1, 3, 5]:
#     model = KNeighborsClassifier(n_neighbors=k)
#     # Learn patterns from training data
#     model.fit(X_train, y_train)
#     # Predict validation samples
#     val_prediction = model.predict(X_val)
#     # Measure accuracy
#     accuracy = accuracy_score(y_val, val_prediction)
#     print("K =", k, "Validation Accuracy =", accuracy)
#
# # Wine
# # 1. Split into training (60%) and temporary data (40%)
# X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
#
# # 2. Split temporary data into validation (20%) and testing (20%)
# X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
#
# # 3. Try different K values using validation data
# for k in [1, 2, 3, 4, 5, 6]:
#     model = KNeighborsClassifier(n_neighbors=k)
#     # Learn patterns from training data
#     model.fit(X_train, y_train)
#     # Predict validation samples
#     val_prediction = model.predict(X_val)
#     # Measure accuracy
#     accuracy = accuracy_score(y_val, val_prediction)
#     print("K =", k, "Validation Accuracy =", accuracy)



# Decision Trees






# Iris





# Wine






# Breast Cancer


# NB
# random_state=15



# SVC






# Video
# train_data = pd.read_csv('/content/Train.csv')
# print("Shape of train data:", train_data.shape)
#
# X = train_data.iloc[:, 1:]
# y = train_data.iloc[:, 0]
#
# print("Shape of X after separating features:", X.shape)




