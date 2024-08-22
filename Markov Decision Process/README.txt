# Markov Decision Process

Usage:
Import the GridMDP class and use policy_iteration or value_iteration methods to solve the problem. For example, the
setup in Fig. 17.1 from AIMA:

    from MDP import GridMDP
    from Parser import get_param

    mdp = GridMDP(grid=[[-0.04, -0.04, -0.04, 1],
                        [-0.04, None, -0.04, -1],
                        [-0.04, -0.04, -0.04, -0.04]],
                  terminals=[(3, 2), (3, 1)])

    # set show_iteration=False to turn off iteration result, U is the utility function
    U = mdp.value_iteration(show_iteration=True)

    # best_policy convert utility function to best policy by using eq. 17.4
    vi_pi = mdp.best_policy(U)
    pi_pi = mdp.policy_iteration()

    # to_arrows translate policy mapping to human readable arrow grid
    print('Value Iteration Result: \n', mdp.to_arrows(vi_pi))
    print('Policy Iteration Result: \n', mdp.to_arrows(pi_pi))

To parse input from a file, you can import the get_param from Parser. For example,
the following code parse mdp_input.txt file to get grid, terminals, T, gamma, epsilon etc..
And we can initiate a GridMDP class by using those inputs

    from MDP import GridMDP
    from Parser import get_param

    f = open("mdp_input.txt", "r")
    contents = f.read()
    params = get_param(contents)
    mdp = GridMDP(grid=params['grid'], terminals=params['terminals'], transition=params['T'], epsilon=params['epsilon'])

    ...

Tests can be run with:

    python run.py