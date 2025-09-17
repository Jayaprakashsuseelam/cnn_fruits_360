import numpy as np
import matplotlib.pyplot as plt

# Define the data points
points = {'a': np.array([1, 2]), 'b': np.array([1, 3]), 'c': np.array([2, 3]), 'd': np.array([4, 2])}

# Function to calculate Manhattan distance
def manhattan_distance(p1, p2):
    return np.sum(np.abs(p1 - p2))

# Function to calculate LDOF for a point
def calculate_ldof(point, k, points):
    distances = []
    for neighbor, neighbor_point in points.items():
        if neighbor != point:
            distances.append(manhattan_distance(points[point], neighbor_point))
    distances.sort()
    knn_distance = distances[k - 1]  # Distance to the k-th nearest neighbor
    violation_degree = manhattan_distance(points[point], np.mean(list(points.values()), axis=0)) / knn_distance
    return violation_degree

# Calculate LDOF for each point
k = 2
ldof_scores = {}
for point in points:
    ldof_scores[point] = calculate_ldof(point, k, points)

# Identify the outlier
outlier = max(ldof_scores, key=ldof_scores.get)

# Plot the points and highlight the outlier
plt.figure()
for point, coordinates in points.items():
    plt.scatter(coordinates[0], coordinates[1], label=point)
plt.scatter(points[outlier][0], points[outlier][1], color='red', label='Outlier')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Data Points with Outlier Detection')
plt.legend()
plt.grid(True)
plt.show()

print("LDOF Scores:")
for point, score in ldof_scores.items():
    print(f"{point}: {score}")

print(f"\nThe top outlier is: {outlier} with LDOF score of {ldof_scores[outlier]}")
