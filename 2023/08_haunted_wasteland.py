####################################
# --- Day 8: Haunted Wasteland --- #
####################################

import AOCUtils
from math import lcm

def get_distance(nodes, instructions, start, is_end):
    distance = 0
    cur = start

    while not is_end(cur):
        cur = nodes[cur][instructions[distance % len(instructions)]]
        distance += 1

    return distance

####################################

maps = AOCUtils.load_input(8)

instructions = maps[0]

nodes = dict()
for raw_node in maps[2:]:
    raw_node = raw_node.split(' = ')

    node = raw_node[0]
    out_nodes = dict(zip('LR', raw_node[1][1:-1].split(', ')))

    nodes[node] = out_nodes

AOCUtils.print_answer(1, get_distance(nodes, instructions, 'AAA', lambda x: x == 'ZZZ'))

p2 = 1
for node in nodes:
    if not node.endswith('A'): continue

    factor = get_distance(nodes, instructions, node, lambda x: x.endswith('Z'))
    p2 = lcm(p2, factor)

AOCUtils.print_answer(2, p2)

AOCUtils.print_time_taken()
