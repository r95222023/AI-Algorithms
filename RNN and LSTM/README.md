# Recurrent Neural Network (RNN) and Long Short-Term Memory (LSTM) Implementation

This repository contains Python implementations for basic Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) cells. These implementations cover both the forward and backward propagation through the networks, demonstrating how hidden states and gradients are computed for sequence prediction tasks.

## Table of Contents

- [Overview](#overview)
- [Functions](#functions)
  - [RNN Functions](#rnn-functions)
  - [LSTM Functions](#lstm-functions)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Overview

Recurrent Neural Networks (RNNs) are a class of neural networks designed for sequential data. They maintain a 'memory' of previous inputs by using hidden states that are passed from one time step to the next. This repository includes implementations for:

- **Basic RNN Cells**: Handles sequences using simple neural network cells with a single hidden state.
- **LSTM Cells**: An advanced RNN variant that mitigates the vanishing gradient problem, which is common in traditional RNNs, by using a more complex cell structure with gates that control information flow.

## Functions

### RNN Functions

1. **`rnn_cell_forward`**
   - Implements a single forward step of an RNN cell.
   - **Inputs**: Current input (`xt`), previous hidden state (`a_prev`), and cell parameters (`parameters`).
   - **Outputs**: Next hidden state (`a_next`), prediction (`yt_pred`), and cache for backpropagation.

2. **`rnn_forward`**
   - Implements the forward pass for a sequence of inputs over an RNN.
   - **Inputs**: Input data for all time steps (`x`), initial hidden state (`a0`), and RNN parameters (`parameters`).
   - **Outputs**: Hidden states for all time steps (`a`), predictions for all time steps (`y_pred`), and cache for backpropagation.

3. **`rnn_cell_backward`**
   - Computes gradients for a single time step of the RNN cell.
   - **Inputs**: Gradient of the loss with respect to the next hidden state (`da_next`), cache from the forward pass.
   - **Outputs**: Gradients with respect to input data, previous hidden state, and weights.

4. **`rnn_backward`**
   - Computes gradients for the entire sequence over the RNN.
   - **Inputs**: Gradients of all hidden states (`da`), cache from the forward pass.
   - **Outputs**: Gradients with respect to input data, initial hidden state, and weights.

### LSTM Functions

1. **`lstm_cell_forward`**
   - Implements a single forward step of an LSTM cell.
   - **Inputs**: Current input (`xt`), previous hidden state (`a_prev`), previous memory state (`c_prev`), and LSTM parameters (`parameters`).
   - **Outputs**: Next hidden state (`a_next`), next memory state (`c_next`), prediction (`yt_pred`), and cache for backpropagation.

2. **`lstm_forward`**
   - Implements the forward pass for a sequence of inputs over an LSTM.
   - **Inputs**: Input data for all time steps (`x`), initial hidden state (`a0`), and LSTM parameters (`parameters`).
   - **Outputs**: Hidden states for all time steps (`a`), memory states for all time steps (`c`), predictions for all time steps (`y`), and cache for backpropagation.

3. **`lstm_cell_backward`**
   - Computes gradients for a single time step of the LSTM cell.
   - **Inputs**: Gradients of the next hidden state (`da_next`), gradients of the next cell state (`dc_next`), cache from the forward pass.
   - **Outputs**: Gradients with respect to input data, previous hidden state, previous cell state, and weights.

## Usage

1. Import the required modules and functions:
   ```python
   import numpy as np
   from recurrent_neural_network import *
   ```

2. Define the necessary parameters and inputs:
   ```python
   x = np.random.randn(n_x, m, T_x)  # Input data
   a0 = np.random.randn(n_a, m)  # Initial hidden state
   parameters = initialize_parameters()  # Initialize RNN/LSTM parameters
   ```

3. Call the RNN or LSTM forward functions:
   ```python
   a, y_pred, caches = rnn_forward(x, a0, parameters)
   ```

4. For training, compute the gradients using the backward functions:
   ```python
   gradients = rnn_backward(da, caches)
   ```

## Dependencies

- `numpy`: Used for numerical computations.
- `rnn_utils.py`: Contains utility functions like activation functions (e.g., `sigmoid`, `softmax`, `update_parameters_with_adam`).
