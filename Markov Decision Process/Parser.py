import re


def get_size(text):
    size_str = re.search("size : .*", text).group().split(' : ')[1].split(' ')
    row = int(size_str[0])
    col = int(size_str[1])
    return row, col


def get_wall(text):
    walls_str = re.search("walls : .*", text).group().split(' : ')[1].split(', ')
    walls = []
    for wall_str in walls_str:
        coord = wall_str.split(' ')
        row = int(coord[0])
        col = int(coord[1])
        walls.append([row, col])
    return walls


def get_terminal(text):
    terminals_str = re.search("terminal_states : .*", text).group().split(' : ')[1].split(', ')
    terminals = []
    for terminal_str in terminals_str:
        values = terminal_str.split(' ')
        row = int(values[0])
        col = int(values[1])
        reward = int(values[2])
        terminals.append([row, col, reward])
    return terminals


def get_reward(text):
    reward_str = re.search("reward : .*", text).group().split(' : ')[1]
    return float(reward_str)


def get_gamma(text):
    gamma_str = re.search("discount_rate : .*", text).group().split(' : ')[1]
    return float(gamma_str)


def get_epsilon(text):
    epsilon_str = re.search("epsilon : .*", text).group().split(' : ')[1]
    return float(epsilon_str)


def get_T(text):
    t_str = re.search("transition_probabilities : .*", text).group().split(' : ')[1].split(' ')
    return float(t_str[0]), float(t_str[1]), float(t_str[2])


def build_grid(size, walls, terminals, reward):
    row, col = size
    grid = []

    for i in range(0, row):
        grid_row = []
        for j in range(0, col):
            grid_row.append(reward)
        grid.append(grid_row)

    for terminal in terminals:
        grid[terminal[0]-1][terminal[1]-1] = terminal[2]

    for wall in walls:
        grid[wall[0]-1][wall[1]-1] = None
    grid.reverse()
    return grid


def get_grid(text):
    size = get_size(text)
    walls = get_wall(text)
    terminals = get_terminal(text)
    reward = get_reward(text)
    return build_grid(size, walls, terminals,reward)


def get_param(text):
    params = {'terminals': []}
    terminals = get_terminal(text)
    for terminal in terminals:
        params['terminals'].append((terminal[1]-1, terminal[0]-1))
    params['grid'] = get_grid(text)
    params['epsilon'] = get_epsilon(text)
    params['gamma'] = get_gamma(text)
    params['T'] = get_T(text)
    return params
