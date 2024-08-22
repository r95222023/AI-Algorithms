Usage:
Import the AStar class and use solve method. For example,

    from IdAStar import IdAStar
    from HeuristicFunction import ManhattanDistance, MisplacementTiles

    puzzle = [1, 3, 6, 4, 9, 5, 2, 7, 0, 10, 11, 12, 13, 14, 8, 15]

    ida = IdAStar(heuristic=ManhattanDistance())
    # IdAStar(heuristic=MisplacementTiles()) for Misplacement Tiles

    solution = ida.solve(puzzle)
    print('Solution:', solution['steps'])
    
Tests can be run with:

    python run.py