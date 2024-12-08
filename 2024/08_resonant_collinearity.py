########################################
# --- Day 8: Resonant Collinearity --- #
########################################

import AOCUtils
from itertools import permutations

########################################

def get_antinodes_1(nodes):
    antinodes = set()
    for (a_x, a_y), (b_x, b_y) in permutations(nodes, 2):
        antinode_x = a_x + (a_x - b_x)
        antinode_y = a_y + (a_y - b_y)
        if 0 <= antinode_x < h and 0 <= antinode_y < w:
            antinodes.add((antinode_x, antinode_y))

    return antinodes

def get_antinodes_2(nodes):
    antinodes = set()
    for (a_x, a_y), (b_x, b_y) in permutations(nodes, 2):
        antinode_x, antinode_y = a_x, a_y
        while 0 <= antinode_x < h and 0 <= antinode_y < w:
            antinodes.add((antinode_x, antinode_y))
            antinode_x += (a_x - b_x)
            antinode_y += (a_y - b_y)

    return antinodes

########################################

antenna_map = AOCUtils.load_input(8)

h, w = len(antenna_map), len(antenna_map[0])

node_groups = dict()
for i in range(h):
   for j in range(w):
        x = antenna_map[i][j]
        if x != '.':
            if x not in node_groups:
                node_groups[x] = set()
            node_groups[x].add((i, j))

antinodes_1 = set()
for node_group in node_groups.values():
    antinodes_1 |= get_antinodes_1(node_group)

AOCUtils.print_answer(1, len(antinodes_1))

antinodes_2 = set()
for node_group in node_groups.values():
    antinodes_2 |= get_antinodes_2(node_group)

AOCUtils.print_answer(2, len(antinodes_2))

AOCUtils.print_time_taken()
