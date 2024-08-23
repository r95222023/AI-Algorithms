class ManhattanDistance:
    """
    Implementation of Manhattan distance heuristic
    """
    def __init__(self):
        return

    def compute(self, node):
        """
        Computes Manhattan distance of the given Node
        """

        score = 0
        size = node.get_size()
        state = node._state
        for i in range(0, len(state)):
            value = int(state[i])
            if value == 0:
                continue
            row = i // size
            col = i % size
            goal_row = (value - 1) // size
            goal_col = (value - 1) % size

            cur_distance = abs(goal_row - row) + abs(goal_col - col)
            score += cur_distance
        return score


class MisplacementTiles:
    """
    Implementation of Number of Misplacement tiles heuristic
    """

    def __init__(self):
        return

    def compute(self, node):
        """
        Computes Number of Misplacement tiles of the given Node
        """

        state = node._state
        score = 0
        for i in range(1, len(state)):
            if i != int(state[i - 1]):
                score += 1
        return score
