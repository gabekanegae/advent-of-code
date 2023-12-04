####################################################
# --- Day 13: A Maze of Twisty Little Cubicles --- #
####################################################

import AOCUtils
from collections import deque

def get_tile(fav, p):
    x, y = p

    n = x*x + 3*x + 2*x*y + y + y*y
    n += fav

    set_bits = 0
    while n:
        set_bits += n % 2
        n //= 2

    return '#' if set_bits % 2 == 1 else '.'

####################################################

favorite_number = AOCUtils.load_input(13)
goal = (31, 39)

visited = set()
queue = deque([((1, 1), 0)])
while queue:
    cur, cur_dist = queue.popleft()

    if cur in visited: continue
    visited.add(cur)

    if cur == goal:
        break

    for delta in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nxt = (cur[0] + delta[0], cur[1] + delta[1])

        if nxt[0] >= 0 and nxt[1] >= 0 and get_tile(favorite_number, nxt) == '.':
            queue.append((nxt, cur_dist+1))

AOCUtils.print_answer(1, cur_dist)

visited = set()
queue = deque([((1, 1), 0)])
while queue:
    cur, cur_dist = queue.popleft()

    if cur in visited: continue
    visited.add(cur)

    if cur_dist == 50:
        continue

    for delta in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nxt = (cur[0] + delta[0], cur[1] + delta[1])

        if nxt[0] >= 0 and nxt[1] >= 0 and get_tile(favorite_number, nxt) == '.':
            queue.append((nxt, cur_dist+1))

AOCUtils.print_answer(2, len(visited))

AOCUtils.print_time_taken()