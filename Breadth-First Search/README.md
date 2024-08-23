# BreadthFirstSearch
A Breadth-first search algorithm for n-puzzle games.

## Features

- a brute force Breadth-first search algorithm for n-puzzle games (8-puzzle, 15-puzzle etc)
- initial state parameter for parallel computation
- solvable check

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
from PyNPuzzle import NPuzzle

fifteen_puzzle = NPuzzle({})
fifteen_puzzle.engage([1, 0, 2, 4, 5, 7, 3, 8, 9, 6, 11, 12, 13, 10, 14, 15])
```
For Python, you can run the tests with:

`python run.py`
    
For Node.js, run the tests with:

`node run`
