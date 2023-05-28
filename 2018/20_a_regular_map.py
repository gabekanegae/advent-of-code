#################################
# --- Day 20: A Regular Map --- #
#################################

import AOCUtils

#################################

regexp = AOCUtils.load_input(20)[1:-1]
max_bound = len(regexp)

stack = []
pos = (max_bound, max_bound)
room_distances = {pos: 0}

moves = {'N': (0, -1), 'W': (-1, 0), 'S': (0, 1), 'E': (1, 0)}
for c in regexp:
    last_pos = pos

    if c == '(':
        stack.append(pos)
    elif c == ')':
        pos = stack.pop()
    elif c == '|':
        pos = stack[-1]
    else: # NWSE
        delta = moves[c]
        pos = (pos[0]+delta[0], pos[1]+delta[1])
        if pos in room_distances:
            room_distances[pos] = min(room_distances[pos], room_distances[last_pos] + 1)
        else:
            room_distances[pos] = room_distances[last_pos] + 1

AOCUtils.print_answer(1, max(room_distances.values()))

far_rooms = sum(dist >= 1000 for dist in room_distances.values())
AOCUtils.print_answer(2, far_rooms)

AOCUtils.print_time_taken()