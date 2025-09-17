import numpy as np
import matplotlib.pyplot as plt

# Define the data points
data = np.array([[1, 2], [1, 3], [2, 3], [4, 2]])

# Calculate pairwise Manhattan distances
def manhattan_distance(point1, point2):
    return np.abs(point1[0] - point2[0]) + np.abs(point1[1] - point2[1])

distances = np.zeros((len(data), len(data)))
for i in range(len(data)):
    for j in range(len(data)):
        distances[i, j] = manhattan_distance(data[i], data[j])

# Calculate k nearest neighbors for each point
k = 2
nearest_neighbors = np.argsort(distances, axis=1)[:, 1:k+1]

# Calculate average distance for each point
avg_distances = np.mean(distances[:, nearest_neighbors], axis=1)

# Calculate LDOF for each point
ldof = np.zeros(len(data))
for i in range(len(data)):
    ldof[i] = np.sum(np.maximum(avg_distances[nearest_neighbors[i]] - distances[i, nearest_neighbors[i]], 0))

# Identify the top outlier
top_outlier_index = np.argmax(ldof)
top_outlier = data[top_outlier_index]

# Plot the data points
plt.scatter(data[:, 0], data[:, 1], color='blue', label='Data Points')

# Highlight the top outlier
plt.scatter(top_outlier[0], top_outlier[1], color='red', label='Top Outlier')

# Plot lines connecting the top outlier to its neighbors
for neighbor_index in nearest_neighbors[top_outlier_index]:
    neighbor = data[neighbor_index]
    plt.plot([top_outlier[0], neighbor[0]], [top_outlier[1], neighbor[1]], color='green', linestyle='--')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Local Distance-Based Outlier Detection')
plt.legend()
plt.grid(True)
plt.show()

print("Top Outlier:", top_outlier)
print("LDOF Scores:", ldof)
