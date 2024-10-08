from HeuristicFunction import ManhattanDistance, MisplacementTiles
from AStar import AStar
from Utils import memory_usage_psutil

import time

puzzle = [1, 3, 6, 4, 9, 5, 2, 7, 0, 10, 11, 12, 13, 14, 8, 15]

# for A* Search
a_star_md = AStar(ManhattanDistance())
a_star_mt = AStar(MisplacementTiles())

# example
print("Example Puzzle: ", puzzle, "\n")
print("### Heuristic Function: Mahhattan Distance ###")
start_time = time.time()
start_mem = memory_usage_psutil()
solution = a_star_md.solve(puzzle)
print('Solution:', solution['steps'])
print('Number of nodes expanded: ', solution['nodes'])
print('Time taken: ', time.time() - start_time, ' seconds')
print('Memory used: ', memory_usage_psutil()-start_mem, 'KB\n')


print("### Heuristic Function: Misplacement Tiles ###")
start_time = time.time()
start_mem = memory_usage_psutil()
solution = a_star_mt.solve(puzzle)
print('Solution:', solution['steps'])
print('Number of nodes expanded: ', solution['nodes'])
print('Time taken: ', time.time() - start_time, ' seconds')
print('Memory used: ', memory_usage_psutil()-start_mem, 'KB\n')

