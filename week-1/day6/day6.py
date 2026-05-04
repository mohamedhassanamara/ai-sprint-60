import numpy as np


def perceptron_forward_pass(inputs, weights, bias):
    """
    Simulates a single artificial neuron.
    """
    # Convert lists to NumPy arrays for easy math
    x = np.array(inputs)
    w = np.array(weights)

    # TODO 1: Calculate the dot product of x and w (sum of inputs * weights)
    # Hint: You can use np.dot(x, w)
    dot_product =  np.dot(x, w)

    # TODO 2: Add the bias to the dot product to get Z
    Z =  dot_product + bias

    # TODO 3: Apply the Step Function
    # If Z is greater than 0, return 1. Otherwise, return 0.
    return 1 if Z > 0 else 0


# --- Testing our Neuron ---
# Input: [Distance, Defenders, Balance]
test_inputs = [0.8, 0.2, 0.9]
# Weights: [Distance Weight, Defender Weight, Balance Weight]
test_weights = [2.0, -3.0, 1.5]
test_bias = -1.0

decision = perceptron_forward_pass(test_inputs, test_weights, test_bias)
print(f"The Neuron Output: {decision}")