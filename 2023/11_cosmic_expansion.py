####################################
# --- Day 11: Cosmic Expansion --- #
####################################

import AOCUtils
from itertools import combinations

def get_distance_sum(image, expansion_factor):
    galaxies = set()
    for x in range(len(image)):
        for y in range(len(image[0])):
            if image[x][y] == '#':
                galaxies.add((x, y))

    empty_rows = [i for i, row in enumerate(image) if row.count('#') == 0]
    empty_cols = [i for i, col in enumerate(zip(*image)) if col.count('#') == 0]

    distances = []
    for (a_x, a_y), (b_x, b_y) in combinations(galaxies, 2):
        delta_x = abs(a_x - b_x)
        delta_y = abs(a_y - b_y)

        expansion_range_x = sorted([a_x, b_x])
        delta_expansion_x = sum(expansion_range_x[0] < row < expansion_range_x[1] for row in empty_rows)

        expansion_range_y = sorted([a_y, b_y])
        delta_expansion_y = sum(expansion_range_y[0] < col < expansion_range_y[1] for col in empty_cols)

        distance = (delta_x + delta_y) + ((delta_expansion_x + delta_expansion_y) * (expansion_factor - 1))
        distances.append(distance)

    return sum(distances)

####################################

image = AOCUtils.load_input(11)

AOCUtils.print_answer(1, get_distance_sum(image, 2))

AOCUtils.print_answer(2, get_distance_sum(image, 1000000))

AOCUtils.print_time_taken()
