
# IterativeDeepeningDepthFirstSearch

An Iterative Deepening Depth-First Search (IDDFS) algorithm for n-puzzle games.

## Features

- An iterative deepening depth-first search algorithm for n-puzzle games (8-puzzle, 15-puzzle, etc.)
- Uses iterative deepening to combine the benefits of depth-first search and breadth-first search
- Adjustable maximum depth for iterative deepening
- Initial state parameter for parallel computation
- Solvable check

## Description

The Iterative Deepening Depth-First Search (IDDFS) algorithm is a hybrid search strategy that combines the space efficiency of depth-first search with the completeness of breadth-first search. It performs depth-limited searches with increasing depth limits until it finds the goal state. The pseudo-code for this algorithm can be found in `iterative deepening.png`.

### Key Components:

- **Depth-Limited Search:** IDDFS performs a series of depth-limited searches, starting from a depth of zero and increasing incrementally. Each search explores the state space up to the current depth limit.

- **Adjustable Depth:** The maximum depth of the iterative search can be adjusted, allowing for fine-tuning of the search strategy.

- **Solvable Check:** Includes functionality to check if a given n-puzzle instance is solvable before performing the search.

- **Initial State Parameter:** Supports parallel computation by allowing an initial state parameter, enabling concurrent searches across different states.

## N-Puzzle Problem
The n-puzzle is a classic puzzle consisting of a grid with `n` numbered tiles and one empty space. The objective is to rearrange the tiles by sliding them into the empty space to reach a specific goal configuration, typically with the tiles ordered numerically. As the grid size increases, the puzzle's complexity also increases, making it an excellent test case for algorithms like A*.

For example, the 15-puzzle (a 4x4 grid with 15 tiles) aims to achieve the following goal configuration:

\[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0\]

Here, `0` represents the empty space. In a 2D grid format, this looks like:

<table>
  <tr>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
  </tr>
  <tr>
    <td>5</td>
    <td>6</td>
    <td>7</td>
    <td>8</td>
  </tr>
  <tr>
    <td>9</td>
    <td>10</td>
    <td>11</td>
    <td>12</td>
  </tr>
  <tr>
    <td>13</td>
    <td>14</td>
    <td>15</td>
    <td>0</td>
  </tr>
</table>

## Usage
To use this in Python, simply import the NPuzzle class from the file, initialize it with a history or an empty dictionary, and then call the engage method to compute the solution:
```python
from Dataset import DataSet
from DTL import DecisionTreeLearner

# attr_names is a string including space-delimited attribute names
# target is the target we want to show as the final result
# file_name is the file name of the csv file(ex: file_name='restaurant' for  restaurant.csv)

dataset = DataSet(file_name='restaurant', target='Wait',
attr_names='Alternate Bar Fri/Sat Hungry Patrons Price Raining Reservation Type WaitEstimate Wait')


dtl= DecisionTreeLearner(dataset)
dtl.show(indent=0)
```
For Python, you can run the tests with:

`python run.py`
    
For Node.js, run the tests with:

`node run`
