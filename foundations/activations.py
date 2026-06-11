import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        return np.round(1 / (1 + np.exp(-z)), 5)

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        return np.maximum(0, z)
    
# z is a 1D NumPy array (a flat vector, e.g. np.array([-2.0, 0.0, 3.5])),
# not a scalar or a Python list. NumPy ops are vectorized, so expressions
# like np.exp(-z) and np.maximum(0, z) apply element-wise across the whole
# array at once and return a new array of the same shape — no loops needed.
# Scalar is just the math/programming word for a single value — one number, like 3.5. 