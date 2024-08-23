from IdAStar import IdAStar
from HeuristicFunction import ManhattanDistance, MisplacementTiles
from Bfs import Bfs
from AStar import AStar
from Utils import memory_usage_psutil
from Node import Node
import time

puzzle = [1, 3, 4, 8, 5, 2, 0, 6, 9, 10, 7, 11, 13, 14, 15, 12]
# puzzle = [1, 2, 7, 3, 5, 6, 11, 4, 9, 10, 0, 8, 13, 14, 15, 12]
node = Node(puzzle, heuristic=ManhattanDistance(), g_score=0)
print(node.get_h_score())

# for Bfs Search
bfs = Bfs()
astar = AStar(heuristic=MisplacementTiles())
# example

print("Example Puzzle: ", puzzle, "\n")
start_time = time.time()
start_mem = memory_usage_psutil()
solution = bfs.solve(puzzle)
print('Solution:', solution.get('steps'))

