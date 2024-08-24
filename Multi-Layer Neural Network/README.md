# Multi-Layer Neural Network

This module provides a deep neural network designed for image classification with a customizable number of hidden layers.

- All necessary functions to build and train the deep neural network are contained in `deep_neural_network_utils.py`.
- The package includes implementations for both a two-layer neural network (`two_layer_model`) and a more general L-layer neural network (`L_layer_model`).

## Usage

### Training the Model

To train a 4-layer neural network, you can execute the following code:

```python
layers_dims = [12288, 20, 7, 5, 1]  # 4-layer model

parameters, costs = L_layer_model(train_x, train_y, layers_dims, num_iterations=2500, print_cost=True)
```

### Making Predictions with the Model

To make predictions using the trained model:

```python
pred_test = predict(test_x, test_y, parameters)
```

### Important Notes

- The cost function should decrease with each iteration.
- Training the model for 2500 iterations might take up to 5 minutes.