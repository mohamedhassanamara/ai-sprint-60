import numpy as np

# Simulate our dataset: 10,000 matches, 15 features (stats) per match
X = np.random.rand(10000, 15)

# Simulate our neural network's weights: 15 inputs matching to 64 neurons
W = np.random.rand(15, 64)

# --- THE MATRIX MULTIPLICATION ---
# TODO: Multiply matrix X and matrix W to get the final predictions
layer_output = X @ W

# This should print (10000, 64) if done correctly
print(f"Output matrix shape: {layer_output.shape}")