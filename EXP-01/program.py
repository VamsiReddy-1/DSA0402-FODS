import numpy as np

student_scores = np.array([
    [85, 78, 90, 88],
    [76, 82, 84, 80],
    [91, 89, 87, 85],
    [88, 90, 92, 91]
])

subjects = ["Math", "Science", "English", "History"]

average_scores = np.mean(student_scores, axis=0)

print("Average Marks of Each Subject")
print()

for i in range(4):
    print(subjects[i], ":", average_scores[i])

highest = np.argmax(average_scores)

print()
print("Subject with Highest Average:", subjects[highest])
