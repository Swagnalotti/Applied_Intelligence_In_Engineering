import numpy as np

# Create an array of student grades
grades = np.array([88, 92, 79, 93, 85])

# Basic statistics
print("Grades:", grades)
print("Average:", np.mean(grades))
print("Highest:", np.max(grades))
print("Lowest:", np.min(grades))

# Add 5 bonus points to every grade
curved = grades + 5
print("Curved Grades:", curved)

# Find students who scored above 90
high_scores = grades[grades > 90]
print("Scores above 90:", high_scores)