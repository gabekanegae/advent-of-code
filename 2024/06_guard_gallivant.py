##################################
# --- Day 6: Guard Gallivant --- #
##################################

import AOCUtils

##################################

get_delta_direction = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
directions = list(get_delta_direction.keys())

def simulate(cur, walls):
    seen = set()
    while True:
        if cur in seen:
            return None

        seen.add(cur)

        x, y, direction = cur

        nxt_x = x + get_delta_direction[direction][0]
        nxt_y = y + get_delta_direction[direction][1]

        if not (0 <= nxt_x < h and 0 <= nxt_y < w):
            return seen

        if (nxt_x, nxt_y) in walls:
            nxt_direction = directions[(directions.index(direction) + 1) % 4]
            cur = (x, y, nxt_direction)
        else:
            cur = (nxt_x, nxt_y, direction)

##################################

lab_map = AOCUtils.load_input(6)

h, w = len(lab_map), len(lab_map[0])

initial_state = None
walls = set()
for i in range(h):
    for j in range(w):
        if lab_map[i][j] == '#':
            walls.add((i, j))
        elif lab_map[i][j] in get_delta_direction:
            initial_state = (i, j, lab_map[i][j])

unique_positions = set((x, y) for x, y, direction in simulate(initial_state, walls))
AOCUtils.print_answer(1, len(unique_positions))

loop_count = sum(simulate(initial_state, walls | set([pos])) is None for pos in unique_positions)
AOCUtils.print_answer(2, loop_count)

AOCUtils.print_time_taken()
