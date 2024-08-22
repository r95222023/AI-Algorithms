import random, operator
# Possible directions that a state can move. ex. (x_new, y_new) = (x,y)+(1,0) is moving to the right
# (1, 0), (0, 1), (-1, 0), (0, -1) correspond to directional arrows >, ^, <, v
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def turn_right(direction):
    return directions[directions.index(direction) - 1]


def turn_left(direction):
    return directions[(directions.index(direction) + 1) % len(directions)]


def argmin(list, fn):
    """Find an element with lowest fn(seq[i]) score; tie goes to first one.
    """
    best = list[0]; best_score = fn(best)
    for x in list:
        x_score = fn(x)
        if x_score < best_score:
            best, best_score = x, x_score
    return best


def argmax(seq, fn):
    """Find an element with highest fn(seq[i]) score; goes to first one if values are the same.
    """
    return argmin(seq, lambda x: -fn(x))


class GridMDP:
    """
    A Markov Decision Process, defined by an initial state, transition model,
    and reward function, and discount_rate, gamma. Instead of using P(s, a, s')
    being probability number for each state/action/state triplet as shown in
    Fig 17.1 and 17.7, get_transitions(s, a) return a list of (p, s')
    pairs. The gird specify is a list of lists of rewards; use None for an obstacle
    (unreachable state)."""
    def __init__(self, grid, terminals, action_list=directions, init=(0, 0), gamma=.85, epsilon=0.001, transition=(0.8, 0.1, 0.1)):
        grid.reverse() ## because we want row 0 on bottom, not on top

        self.init = init
        # An action is an (x, y) unit vector; e.g. (1, 0) means move to the right.
        self.action_list = action_list
        self.terminals = terminals
        self.gamma = gamma
        self.epsilon = epsilon
        self.states = set()
        self.reward = {}
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.transition = transition
        for x in range(self.cols):
            for y in range(self.rows):
                self.reward[x, y] = grid[y][x]
                if grid[y][x] is not None:
                    self.states.add((x, y))

    def actions(self, state):
        """
        Return a set of actions that can be performed in this state.
        """
        if state in self.terminals:
            return [None]
        else:
            return self.action_list

    def get_transitions(self, state, action):
        if action == None:
            return [(0.0, state)]
        else:
            forward, right, left = self.transition
            return [(forward, self.move(state, action)),
                    (right, self.move(state, turn_right(action))),
                    (left, self.move(state, turn_left(action)))]

    def get_reward(self, state):
        """Get numeric reward for this state."""
        return self.reward[state]

    def move(self, state, direction):
        """Get the state that results from moving in this direction."""
        state1 = tuple(map(operator.add, state, direction))
        # add direction to a state. ex: {1,1}+{1,0}={2,1}
        return state1 if state1 in self.states else state

    def to_grid(self, mapping):
        """Convert a mapping from (x, y) to v into a [[..., v, ...]] grid."""
        return list(reversed([[mapping.get((x, y), None)
                               for x in range(self.cols)]
                              for y in range(self.rows)]))

    def to_arrows(self, policy):
        """Translate policy to human readable arrows that indicate moving direction"""
        chars = {(1, 0):'>', (0, 1):'^', (-1, 0):'<', (0, -1):'v', None: '.'}
        return self.to_grid(dict([(s, chars[a]) for (s, a) in policy.items()]))

    def value_iteration(self, show_iteration):
        return value_iteration(self, show_iteration)

    def best_policy(self, U):
        return best_policy(self, U)

    def policy_iteration(self):
        return policy_iteration(self)


def value_iteration(mdp, show_iteration=False):
    """Perform value iteration to solve an MDP."""
    U1 = dict([(s, 0) for s in mdp.states])
    gamma = mdp.gamma
    epsilon = mdp.epsilon
    iteration = 0
    while True:
        U = U1.copy()
        if show_iteration:
            print('Value iteration ', iteration)
            print(mdp.to_grid(U))
        iteration = iteration+1
        delta = 0
        for s in mdp.states:
            U1[s] = mdp.get_reward(s) + gamma * max([sum([p * U[s1] for (p, s1) in mdp.get_transitions(s, a)])
                                        for a in mdp.actions(s)])
            delta = max(delta, abs(U1[s] - U[s]))
        if delta < epsilon * (1 - gamma) / gamma:
            return U


def best_policy(mdp, U):
    """Given an MDP and a utility function U, determine the best policy,
    as a mapping from state to action. (Equation 17.4)"""
    pi = {}
    for s in mdp.states:
        pi[s] = argmax(mdp.actions(s), lambda a:expected_utility(a, s, U, mdp))
    return pi


def expected_utility(a, s, U, mdp):
    """The expected utility of doing a in state s, according to the MDP and U."""
    return sum([p * U[s1] for (p, s1) in mdp.get_transitions(s, a)])


def policy_iteration(mdp):
    """Perform policy iteration to solve an MDP"""
    U = dict([(s, 0) for s in mdp.states])
    pi = dict([(s, random.choice(mdp.actions(s))) for s in mdp.states])
    while True:
        U = policy_evaluation(pi, U, mdp)
        unchanged = True
        for s in mdp.states:
            a = argmax(mdp.actions(s), lambda a: expected_utility(a,s,U,mdp))
            if a != pi[s]:
                pi[s] = a
                unchanged = False
        if unchanged:
            return pi


def policy_evaluation(pi, U, mdp, k=25):
    """Update utility mapping U in the MDP to its utility by using modified policy iteration."""
    for i in range(k):
        for s in mdp.states:
            U[s] = mdp.get_reward(s) + mdp.gamma * sum([p * U[s] for (p, s1) in mdp.get_transitions(s, pi[s])])
    return U
