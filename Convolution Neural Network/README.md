# Convolution Neural Network

This module provides a convolution network with convolutional (CONV) and pooling (POOL) layers implemented in numpy, including both forward propagation and backward propagation.
This repository contains a Python implementation of a basic Convolutional Neural Network (CNN) from scratch, without using any high-level deep learning libraries like TensorFlow or PyTorch. The implementation covers the essential components of a CNN, including convolution layers, pooling layers, forward propagation, and backpropagation.

## Overview

This CNN implementation provides a step-by-step guide to building a multi-layer convolutional neural network using basic NumPy operations. It is a great resource for learning how convolutional layers, pooling layers, and fully connected layers work under the hood.

## Features

- **Zero Padding**: Adds padding around the input image to control the spatial size of the output.
- **Convolution Operation**: Implements the forward and backward pass of convolution, which includes calculating the gradients for backpropagation.
- **Pooling Operation**: Implements max pooling and average pooling layers with forward and backward propagation.
- **Multiple Layers**: Supports building CNNs with multiple convolutional and pooling layers.
- **Customizable Parameters**: Allows setting custom hyperparameters like filter size, number of filters, stride, and padding.


## Usage

To train a multiple-layer Convolutional Neural Network (CNN) model using the functions provided in your code snippet, we need to define a full training loop. Here's an example of how you could set up a simple CNN training routine in Python, using the provided convolution and pooling functions.

### Step-by-Step Example: Training a Simple CNN

1. **Define the Neural Network Architecture**: This involves setting up the layers (convolutional and pooling layers).
2. **Initialize Parameters**: Initialize weights and biases for each layer.
3. **Forward Propagation**: Compute the output for a batch of input images by passing them through the layers of the network.
4. **Compute Loss**: Measure the difference between the predicted output and the true output (e.g., using cross-entropy loss for classification).
5. **Backward Propagation**: Compute gradients with respect to parameters to adjust them in a way that reduces the loss.
6. **Update Parameters**: Update the weights and biases using gradient descent.
7. **Training Loop**: Repeat the process for multiple epochs.

Here's how you could implement this:

```python
import numpy as np

# Assuming the ConvLayer and other necessary functions (conv_forward, conv_backward, pool_forward, etc.) are already defined as provided.

class SimpleCNN:
    def __init__(self):
        self.conv1 = ConvLayer(filter_size=3, num_filters=8, stride=1, pad=1)
        self.conv2 = ConvLayer(filter_size=3, num_filters=16, stride=1, pad=1)
        self.pool = {"stride": 2, "f": 2}
        
    def forward(self, X):
        Z1 = self.conv1.forward(X)
        A1, _ = pool_forward(Z1, self.pool, mode="max")
        Z2 = self.conv2.forward(A1)
        A2, _ = pool_forward(Z2, self.pool, mode="max")
        return A2
    
    def backward(self, dA2):
        dZ2 = dA2  # dA2 could be from a loss function gradient
        dA1, dW2, db2 = self.conv2.backward(dZ2)
        dZ1 = dA1  # After pooling layer, this should be adjusted
        dA0, dW1, db1 = self.conv1.backward(dZ1)
        return dW1, db1, dW2, db2
    
    def update_parameters(self, dW1, db1, dW2, db2, learning_rate):
        self.conv1.update_parameters(dW1, db1, learning_rate)
        self.conv2.update_parameters(dW2, db2, learning_rate)

# Initialize the network
cnn = SimpleCNN()

# Dummy data
X_train = np.random.randn(10, 64, 64, 3)  # 10 images of 64x64x3
Y_train = np.random.randint(0, 2, (10, 1))  # Binary classification labels for example

# Training parameters
epochs = 10
learning_rate = 0.01

# Training loop
for epoch in range(epochs):
    # Forward propagation
    A2 = cnn.forward(X_train)
    
    # Compute loss (example with binary cross-entropy)
    # Loss would typically be computed using a softmax activation and cross-entropy loss
    # But here we will assume a direct output for simplicity
    
    # Backward propagation
    # For this example, let's assume dA2 is computed by some loss function with respect to Y_train
    dA2 = np.random.randn(*A2.shape)  # Placeholder for the gradient of the loss with respect to A2
    
    dW1, db1, dW2, db2 = cnn.backward(dA2)
    
    # Update parameters
    cnn.update_parameters(dW1, db1, dW2, db2, learning_rate)
    
    # Print loss every epoch
    print(f"Epoch {epoch + 1}/{epochs} complete")

print("Training finished.")
```

### Explanation:

- **Initialization**: A `SimpleCNN` class is created that contains two convolutional layers (`conv1` and `conv2`) and pooling layers.
- **Forward Pass**: Images are passed through the two convolutional layers and pooling layers.
- **Backward Pass**: Gradients are computed with respect to the output, and backpropagation is performed to adjust weights.
- **Parameter Update**: Parameters are updated using the computed gradients and a learning rate.

### Note:

- This code assumes a basic understanding of how gradients (`dA2`, `dZ2`, etc.) are computed through a loss function. For a complete working example, you need to define a proper loss function (e.g., cross-entropy for classification) and compute the gradient of the loss with respect to the network's output.
- The current example uses placeholder gradients (`dA2`) for simplicity. In practice, you'd compute these based on the network's output and the true labels (`Y_train`).