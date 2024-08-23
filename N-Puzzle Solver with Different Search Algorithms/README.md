# N-Puzzle Solver
The N-Puzzle Solver is a command-line interface that allows you to solve n-puzzle games (such as the 8-puzzle or 15-puzzle) using different search algorithms.

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

- **Source code:** https://github.com/r95222023/n_puzzle_solver

It provides:

- Breadth-first search
- Iterative deepening depth-first search
- A* search with Manhattan Distance and Misplacement Tiles heuristic functions 
- Command line interface that allows user to play the n puzzle game and solve the 
  puzzle with different search algorithm


Usage:
Import the NPuzzle class and use solve method. For example, 

    from NPuzzle import NPuzzle
    from HeuristicFunction import ManhattanDistance, MisplacementTiles

    puzzle = [1, 0, 2, 4, 5, 7, 3, 8, 9, 6, 11, 12, 13, 10, 14, 15]
    n_puzzle = NPuzzle()
    
    # for IDA Search
    idastar = n_puzzle.AStar(heuristic=ManhattanDistance())
    idastar.solve(puzzle)
    
    # for A* Search
    astar = n_puzzle.AStar(heuristic=ManhattanDistance())
    astar.solve(puzzle)
    
    # for Iterative Deepening Depth-First Search
    iddfs = n_puzzle.Iddfs()
    iddfs.solve(puzzle)
    
    # for Breadth-First Search
    bfs = n_puzzle.Bfs()
    bfs.solve(puzzle)
    
Tests can be run with:

    python run.py
    
To play the n-puzzle game, simply run

    python play.py