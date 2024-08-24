# U-Net Model for Image Segmentation

This project provides an implementation of a U-Net model using TensorFlow and Keras. U-Net is a convolutional neural network architecture designed for fast and precise segmentation of images. It's widely used in medical image segmentation and other tasks where accurate localization is important.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Functions and Methods](#functions-and-methods)
- [Example](#example)
- [License](#license)

## Overview

The U-Net model implemented here is composed of a contracting path (downsampling) that captures context and an expansive path (upsampling) that enables precise localization. This repository includes functions to preprocess images and masks, build the U-Net model, and create both downsampling and upsampling blocks.

## Installation

To run this code, you'll need Python and TensorFlow installed. You can install the necessary packages using pip:

```bash
pip install tensorflow numpy
```

## Usage

1. **Processing and Preprocessing Data:**
   - The functions `process_path` and `preprocess` are used to load and resize images and their corresponding masks.

2. **Building the Model:**
   - The U-Net model is built using `conv_block` for downsampling and `upsampling_block` for upsampling. The main model-building function is `unet_model`.

### Example Usage

Below is an example of how to build and compile the U-Net model:

```python
import tensorflow as tf
from unet import unet_model

# Define input size, number of filters, and number of classes
input_size = (96, 128, 3)
n_filters = 32
n_classes = 23

# Build the model
model = unet_model(input_size=input_size, n_filters=n_filters, n_classes=n_classes)

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Display the model summary
model.summary()
```

## Example

To train the model, you would typically follow these steps:

1. **Prepare your dataset**: Make sure your images and masks are correctly formatted and paired.
2. **Preprocess the data**: Use the `process_path` and `preprocess` functions to load and preprocess the data.
3. **Build the model**: Use `unet_model` to build the U-Net model.
4. **Compile and train the model**: Compile the model with an optimizer and loss function suitable for your task, then train the model on your dataset.
