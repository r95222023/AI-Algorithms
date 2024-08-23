# GridMDP

This project implements the `GridMDP` as described in Chapter 17 of *AI: A Modern Approach (3rd Edition)*. The `GridMDP` module offers methods for solving Markov Decision Processes (MDPs) using both value iteration and policy iteration algorithms. It is tailored for grid-based MDPs, supports input parsing from files, and presents results in an easily interpretable format.

## Features

- **Value Iteration**: Computes the utility function for each state and derives the best policy.
- **Policy Iteration**: Computes the optimal policy directly.
- **Human-Readable Output**: Converts policy mappings to a grid of arrows for easy interpretation.

## Usage

Modify `run.py` as follows:
### Setup and Solve MDP

```python
from MDP import GridMDP
from Parser import get_param

# Define the MDP grid and terminal states
mdp = GridMDP(grid=[[-0.04, -0.04, -0.04, 1],
                    [-0.04, None, -0.04, -1],
                    [-0.04, -0.04, -0.04, -0.04]],
                terminals=[(3, 2), (3, 1)])

# Perform value iteration and get the utility function
U = mdp.value_iteration(show_iteration=True)

# Derive the best policy from the utility function
vi_pi = mdp.best_policy(U)
pi_pi = mdp.policy_iteration()

# Convert policies to human-readable format and print
print('Value Iteration Result: \n', mdp.to_arrows(vi_pi))
print('Policy Iteration Result: \n', mdp.to_arrows(pi_pi))
```

### Parsing Input from a File

1. **Prepare `mdp_input.txt`**: The file should include grid, terminals, transition probabilities, gamma, epsilon, etc.

2. **Read and Parse File:**

```python
from MDP import GridMDP
from Parser import get_param

# Read the input file
with open("mdp_input.txt", "r") as f:
    contents = f.read()

# Parse parameters from the file
params = get_param(contents)

# Initialize GridMDP with parsed parameters
mdp = GridMDP(grid=params['grid'],
                terminals=params['terminals'],
                transition=params['T'],
                epsilon=params['epsilon'])

# Solve and display results as needed
```

## Running Tests

To run tests, execute the following command:

```bash
python run.py
```

Feel free to adjust any specifics based on your project's details or additional features.