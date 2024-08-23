from NPuzzle import NPuzzle
from HeuristicFunction import ManhattanDistance, MisplacementTiles
from CLInterface import CLInterface
from Utils import memory_usage_psutil
import time

# puzzle = [1,2,3,4,5,10,6,0,9,7,11,8,13,14,15,12]

## Test Cases
puzzle = [5,2,4,8,10,3,11,14,6,0,9,12,13,1,15,7]
# Solution: ['down', 'right', 'right', 'up', 'up', 'left', 'left', 'down', 'right', 'right', 'up', 'up', 'left', 'left', 'down', 'left', 'down', 'right', 'right', 'down', 'left', 'up', 'up', 'left', 'up', 'right', 'right', 'down', 'down', 'right', 'down']
# Iterations:  5
# Number of nodes expanded:  7830
# Time taken:  4.21952223777771  seconds
# Memory used:  92.0 KB

n_puzzle = NPuzzle()

# for A* Search
id_a_star_md = n_puzzle.IdAStar(heuristic=ManhattanDistance())
id_a_star_mt = n_puzzle.IdAStar(heuristic=MisplacementTiles())

# example

print("Example Puzzle: ", puzzle, "\n")
print("%%% Solving puzzle by using Iterative Deepening A* algorithm %%%")
print("### Heuristic Function 1: Mahhattan Distance ###")
start_time = time.time()
start_mem = memory_usage_psutil()
solution = id_a_star_md.solve(puzzle)
print('Solution:', solution['steps'])
print('Iterations: ', solution['iteration'])
print('Number of nodes expanded: ', solution['nodes'])
print('Time taken: ', time.time() - start_time, ' seconds')
print('Memory used: ', memory_usage_psutil()-start_mem, 'KB\n')


print("### Heuristic Function 2: Misplacement Tiles ###")
start_time = time.time()
start_mem = memory_usage_psutil()
solution = id_a_star_mt.solve(puzzle)
print('Solution:', solution['steps'])
print('Number of nodes expanded: ', solution['nodes'])
print('Time taken: ', time.time() - start_time, ' seconds')
print('Memory used: ', memory_usage_psutil()-start_mem, 'KB\n')
command = input("Do you want to play a game (Y/n)? ")

if command != "n":
    CLInterface().play(4)
