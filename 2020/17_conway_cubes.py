################################
# --- Day 17: Conway Cubes --- #
################################

import AOCUtils
from itertools import combinations

# Assume dimensions >= 2
def conway_cubes(raw_grid, dimensions, cycles=6):
    all_moves = set(list(combinations([-1, 0, 1]*dimensions, dimensions)))
    null_move = set([tuple([0]*dimensions)])
    moves = list(all_moves - null_move)

    active = set()
    for x in range(len(raw_grid)):
        for y in range(len(raw_grid[0])):
            if raw_grid[x][y] == '#':
                pos = tuple([x, y] + [0]*(dimensions - 2))
                active.add(pos)

    for cycle in range(cycles):
        to_be_updated = set(active)
        for pos in active:
            for delta in moves:
                neighbor = tuple(k+d for k, d in zip(pos, delta))
                to_be_updated.add(neighbor)

        new_active = set(active)
        for pos in to_be_updated:
            neighbors = 0
            for delta in moves:
                neighbor = tuple(k+d for k, d in zip(pos, delta))
                neighbors += int(neighbor in active)

            if pos in active and neighbors not in [2, 3]:
                new_active.remove(pos)
            elif pos not in active and neighbors == 3:
                new_active.add(pos)

        active = new_active

    return len(active)

################################

raw_grid = AOCUtils.load_input(17)

AOCUtils.print_answer(1, conway_cubes(raw_grid, 3))

AOCUtils.print_answer(2, conway_cubes(raw_grid, 4))

AOCUtils.print_time_taken()