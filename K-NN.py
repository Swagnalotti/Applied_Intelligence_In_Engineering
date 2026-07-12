from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

# Student features: [sleep hours, study hours] (small data for the sake of examples)
X = [ [8,2], [6,5], [7,6], [5,8], [4,10], [9,1], [6,7], [3,12], [8,4], [5,9] ]

# Exam grades
y = [70, 75, 82, 85, 90, 65, 88, 95, 78, 92]

# 1. Split into training (60%) and temporary data (40%)
X_train, X_temp, y_train, y_temp = train_test_split( X, y, test_size=0.4, random_state=42)

# 2. Split temporary data into validation (20%) and testing (20%)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# 3. Try different K values using validation data
for k in [1, 3, 5]:
    model = KNeighborsRegressor(n_neighbors=k)
    # Store values for calculation
    model.fit(X_train, y_train)
    val_prediction = model.predict(X_val)
    error = mean_squared_error(y_val, val_prediction)
    print("K =", k, "Validation Error =", error)

final_model = KNeighborsRegressor(n_neighbors=1)
final_model.fit(X_train, y_train)
test_prediction = final_model.predict(X_test)
test_error = mean_squared_error(y_test, test_prediction)
print("Test Error:", test_error)