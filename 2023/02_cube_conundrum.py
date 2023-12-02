#################################
# --- Day 2: Cube Conundrum --- #
#################################

from collections import defaultdict
import AOCUtils

#################################

def is_game_possible(game):
    bag = {'red': 12, 'green': 13, 'blue': 14}

    return all(cube_set[cube] <= bag[cube] for cube in bag.keys() for cube_set in game)

def get_game_power(game):
    bag = {'red': 0, 'green': 0, 'blue': 0}

    for cube in bag.keys():
        bag[cube] = max(cube_set[cube] for cube_set in game)

    return bag['red'] * bag['green'] * bag['blue']

#################################

raw_games = AOCUtils.load_input(2)

games = dict()
for raw_game in raw_games:
    raw_index, raw_cube_sets = raw_game.split(':')
    index = int(raw_index.split()[1])
    raw_cube_sets = raw_cube_sets.split(';')
    cube_sets = []
    for raw_cube_set in raw_cube_sets:
        raw_cubes = raw_cube_set.split(',')
        cube_set = defaultdict(int)
        for raw_cube in raw_cubes:
            amount, cube = raw_cube.strip().split()
            cube_set[cube] = int(amount)
        cube_sets.append(cube_set)
    games[index] = cube_sets

AOCUtils.print_answer(1, sum(k for k, v in games.items() if is_game_possible(games[k])))

AOCUtils.print_answer(2, sum(map(get_game_power, games.values())))

AOCUtils.print_time_taken()
