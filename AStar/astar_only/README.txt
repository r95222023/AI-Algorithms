Usage:
Import the AStar class and use solve method. For example,

    from AStar import AStar
    from HeuristicFunction import ManhattanDistance, MisplacementTiles

    puzzle = [1, 3, 6, 4, 9, 5, 2, 7, 0, 10, 11, 12, 13, 14, 8, 15]

    a_star = AStar(ManhattanDistance())
    # AStar(MisplacementTiles()) for Misplacement Tiles

    solution = a_star.solve(puzzle)
    print('Solution:', solution['steps'])
    
Tests can be run with:

    python run.py

For full featured playable program move to 'full' directory and run with:
   
    python run.py