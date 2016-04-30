"""Softmax."""

scores = [1.0, 2.0, 3.0]

import numpy as np
import math

def softmax(x):
    """Compute softmax values for each sets of scores in x."""

    pass  # TODO: Compute and return softmax(x)

    scores_np = np.array(scores)
    return_array = np.zeros(scores_np.shape)

    total_denominator = 0

    for x in scores_np:
        total_denominator = total_denominator+np.exp(x)

    for x in scores_np:
        current_prob = np.exp(x)/total_denominator
        return_array = np.append(return_array, current_prob)

    return np.array(return_array)

print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
