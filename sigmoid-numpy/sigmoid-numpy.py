import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    x = np.exp(-x)
    y = 1/(1+x)
    return y