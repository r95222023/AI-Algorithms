Here’s a description for an Iterative Deepening A* (IDA*) algorithm implementation:

---

# IDA* Algorithm Implementation

This folder includes an implementation of the Iterative Deepening A* (IDA*) algorithm for solving the n-puzzle problem. IDA* is an advanced pathfinding and graph traversal technique that combines the benefits of both depth-first search and A* to find the shortest path between two points.

## Features

- **IDA* Algorithm**: Efficiently searches for the shortest path from a start state to a goal state using a combination of depth-first search and heuristic-based evaluation.
- **Heuristic Functions**: Supports various heuristic functions, such as Manhattan Distance and Misplacement Tiles, to guide the search process.
- **Bounded Search**: Iteratively deepens the search with increasing bounds based on the heuristic value, optimizing memory usage and search efficiency.
- **Customizable**: Easily extendable to include additional heuristics or modify search parameters for enhanced performance.

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

## Getting Started

### Prerequisites

- Python 3.x

### Usage
```python
Import the AStar class and use solve method. For example,

from IdAStar import IdAStar
from HeuristicFunction import ManhattanDistance, MisplacementTiles

puzzle = [1, 3, 6, 4, 9, 5, 2, 7, 0, 10, 11, 12, 13, 14, 8, 15]

ida = IdAStar(heuristic=ManhattanDistance())
# IdAStar(heuristic=MisplacementTiles()) for Misplacement Tiles

solution = ida.solve(puzzle)
print('Solution:', solution['steps'])
    
```
    
To execute the program, use the following command:

`python run.py`
