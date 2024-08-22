from MDP import GridMDP
from Parser import get_param

# mdp = GridMDP(grid=[[-0.04, -0.04, -0.04, 1],
#                     [-0.04, None, -0.04, -1],
#                     [-0.04, -0.04, -0.04, -0.04]],
#               terminals=[(3, 2), (3, 1)])

f = open("mdp_input.txt", "r")
contents = f.read()
params = get_param(contents)
# params = {'terminals': [(2, 4), (3, 4), (1, 3)], <-- the number is (x, y) which correspond to 5 3, 5 4, 4 2
# 'grid':
# [[-0.04, -0.04, -3, 2],
# [-0.04, 1, -0.04, -0.04],
# [-0.04, -0.04, -0.04, -0.04],
# [-0.04, None, None, -0.04],
# [-0.04, -0.04, -0.04, -0.04]],
# 'epsilon': 0.001, 'gamma': 0.85, 'T': (0.8, 0.1, 0.1)}

mdp = GridMDP(grid=params['grid'], terminals=params['terminals'],
              transition=params['T'], gamma=params['gamma'], epsilon=params['epsilon'])

# set show_iteration=False to turn off iteration result, U is the utility function
U = mdp.value_iteration(show_iteration=True)

# best_policy convert utility function to best policy by using eq. 17.4
vi_pi = mdp.best_policy(U)
# [['v', '<', '.', '.'],
#  ['>', '.', '>', '^'],
#  ['>', '^', '>', '^'],
#  ['^', None, None, '^'],
#  ['^', '>', '>', '^']]
# this is the same as the given expected output shown below except the grid definition is different
# E,>  E,>  E,>  E,>  T,.
#
# N,^  -    N,^  N,^  T,.
#
# N,^  -    E,>  T,.  S,v
#
# E,>  E,>  N,^  N,^  W,<
pi_pi = mdp.policy_iteration()

# to_arrows translate policy mapping to human readable arrow grid
print('Value Iteration Result: \n', mdp.to_arrows(vi_pi))
print('Policy Iteration Result: \n', mdp.to_arrows(pi_pi))

