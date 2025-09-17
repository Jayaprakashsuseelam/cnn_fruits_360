import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# Load the dataset
# https://archive.ics.uci.edu/ml/machine-learning-databases/ionosphere/ionosphere.data
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/ionosphere/ionosphere.data"
df = pd.read_csv(url, header=None)

# Extract the first 2 features (columns 1 and 2)
X = df.iloc[:, 0:2].values

# Normalize the data
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)

# Compute LDOF
k = 3
nn = NearestNeighbors(n_neighbors=k)
nn.fit(X_normalized)
distances, indices = nn.kneighbors(X_normalized)

# Compute LDOF for each point
LDOF = np.mean(distances[:, 1:], axis=1)

# Determine the ranking of outliers
outlier_indices = np.argsort(-LDOF)  # Sort in descending order

# Identify the top 5 outliers
top_outliers = df.iloc[outlier_indices[:5]]

print("Top 5 Outliers:")
print(top_outliers)

# Plot the data points and highlight outliers
plt.figure(figsize=(10, 6))
plt.scatter(X_normalized[:, 0], X_normalized[:, 1], c='b', label='Data Points')
plt.scatter(X_normalized[outlier_indices[:5], 0], X_normalized[outlier_indices[:5], 1], c='r', label='Top 5 Outliers')
plt.title('Ionosphere Dataset with Top 5 Outliers')
plt.xlabel('Feature 1 (Normalized)')
plt.ylabel('Feature 2 (Normalized)')
plt.legend()
plt.grid(True)
plt.show()
