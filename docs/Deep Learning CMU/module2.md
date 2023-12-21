
# A. Softmax Function and LogSumExp Trick

## Overview

The discussion focused on the softmax function, its implementation using the LogSumExp trick, and how this trick enhances numerical stability. The softmax function is essential in machine learning for converting real-valued vectors into probability distributions. However, direct implementation can lead to numerical issues like overflow and underflow, especially when dealing with large input values.

## Softmax Function

- **Purpose**: Used in classification tasks to convert a vector of real numbers into a probability distribution.
- **Formula**: Softmax of an element $ x_i $ in a vector $ x $ is defined as $\text{softmax}(x_i) = \frac{e^{x_i}}{\sum_{j} e^{x_j}}$
- **Batch Processing**: In practical applications, especially in neural networks, softmax is often applied to batches of data, requiring the function to handle 2D arrays.

## LogSumExp Trick

- **Problem Addressed**: Direct computation of softmax can lead to numerical instability due to exponentiation of large numbers.
- **Solution**: The LogSumExp trick improves numerical stability by subtracting the maximum element in the input vector from each element before exponentiation.
- **Implementation**:
  1. Compute the maximum value $a$ in the input array (or along each row for a 2D array).
  2. Adjust the softmax calculation to $ \text{softmax}(x_i) = \frac{e^{x_i - a}}{\sum_{j} e^{x_j - a}}$
  3. This adjustment ensures no overflow or underflow during computation.

## Softmax with LogSumExp Trick Implementation

- **Input**: A 2D array, typically representing a batch of data points.
- **Process**:
  1. Find the maximum value \( a \) in each row.
  2. Compute `denom` as $ a + \log(\sum_{j} e^{x_j - a}) $ for each row.
  3. Apply softmax by calculating `np.exp(x - denom)`, ensuring each row sums up to 1.

source: Programming Assignment 2.1: Multilayer Perceptron (Assignment 1A) - https://classroom.emeritus.org/courses/6844
```py
def softmax(x):
    """[Given] Calculates the softmax of the input array using the LogSumExp trick for numerical stability.
    Args:
        x (np.array): Input array, shaped (batch_size, d), where d is any integer.
    Returns:
        np.array: Same shape as input, but the values of each row are now scaled to add up to 1.
    """
    # [Given] Use this in CrossEntropyLoss.
    a = np.max(x, axis=1, keepdims=True)
    denom = a + np.log(np.sum(np.exp(x - a), axis=1, keepdims=True))
    return np.exp(x - denom)
```
- **Benefits**: This implementation is numerically stable and suitable for batch processing in machine learning contexts.

## Example and Practical Application

- **Use Case**: Applied in machine learning models, particularly in calculating probabilities for classification tasks and in loss functions like cross-entropy loss.
- **Numerical Stability**: The LogSumExp trick ensures the softmax function works accurately even with high-dimensional data and large values, common in deep learning models.