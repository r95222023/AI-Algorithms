# Transformer Model Implementation

This repository contains a TensorFlow-based implementation of the Transformer model, as described in the paper ["Attention is All You Need"](https://arxiv.org/abs/1706.03762) by Vaswani et al. The code includes components for both the Encoder and Decoder, along with utilities for positional encoding, masking, and multi-head attention.

## Components

1. **Positional Encoding**
   - **`get_angles`**: Computes the angles for positional encoding.
   - **`positional_encoding`**: Generates the positional encoding matrix.

2. **Masks**
   - **`create_padding_mask`**: Creates a mask to ignore padding tokens.
   - **`create_look_ahead_mask`**: Creates a look-ahead mask for preventing the decoder from attending to future tokens.

3. **Encoder Layer**
   - **`EncoderLayer`**: Implements a single layer of the Transformer encoder, including multi-head self-attention and a feed-forward network.

4. **Decoder Layer**
   - **`DecoderLayer`**: Implements a single layer of the Transformer decoder, including multi-head self-attention, encoder-decoder attention, and a feed-forward network.

5. **Encoder**
   - **`Encoder`**: Stacks multiple `EncoderLayer`s to form the complete encoder.

6. **Decoder**
   - **`Decoder`**: Stacks multiple `DecoderLayer`s to form the complete decoder.

7. **Transformer Model**
   - **`Transformer`**: Combines the encoder and decoder, including a final dense layer for output predictions.

## Usage

### Dependencies

- TensorFlow
- NumPy
- Hugging Face Transformers

### Installation

You can install the necessary packages using pip:

```bash
pip install tensorflow numpy transformers
```

### Example Usage

To use the Transformer model, you can initialize and call it as follows:

```python
import tensorflow as tf
from transformer import Transformer

# Initialize Transformer model
transformer = Transformer(
    num_layers=4,
    embedding_dim=128,
    num_heads=8,
    fully_connected_dim=512,
    input_vocab_size=10000,
    target_vocab_size=10000,
    max_positional_encoding_input=1000,
    max_positional_encoding_target=1000
)

# Example input tensors
input_sentence = tf.random.uniform((batch_size, input_seq_len), maxval=input_vocab_size, dtype=tf.int32)
output_sentence = tf.random.uniform((batch_size, target_seq_len), maxval=target_vocab_size, dtype=tf.int32)
enc_padding_mask = tf.random.uniform((batch_size, 1, input_seq_len), dtype=tf.float32)
look_ahead_mask = tf.random.uniform((batch_size, target_seq_len, target_seq_len), dtype=tf.float32)
dec_padding_mask = tf.random.uniform((batch_size, 1, input_seq_len), dtype=tf.float32)

# Forward pass
final_output, attention_weights = transformer(input_sentence, output_sentence, training=True, 
                                              enc_padding_mask=enc_padding_mask, 
                                              look_ahead_mask=look_ahead_mask, 
                                              dec_padding_mask=dec_padding_mask)
```
