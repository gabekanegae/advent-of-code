###########################################
# --- Day 12: Hill Climbing Algorithm --- #
###########################################

import AOCUtils

from collections import deque

def get_min_dist(grid, start, end):
    n, m = len(grid), len(grid[0])

    queue = deque([(start, 0)])
    visited = set()
    while queue:
        cur, dist = queue.popleft()

        if cur in visited: continue
        visited.add(cur)

        if cur == end:
            return dist

        for delta in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nxt = (cur[0]+delta[0], cur[1]+delta[1])

            if not (0 <= nxt[0] < n and 0 <= nxt[1] < m): continue

            if ord(grid[nxt[0]][nxt[1]]) <= ord(grid[cur[0]][cur[1]]) + 1:
                queue.append((nxt, dist+1))

    return float('inf')

###########################################

raw_grid = AOCUtils.load_input(12)
grid = list(map(list, raw_grid))

start, end = None, None
starts = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            grid[i][j] = 'a'
            start = (i, j)
        elif grid[i][j] == 'E':
            grid[i][j] = 'z'
            end = (i, j)
        elif grid[i][j] == 'a':
            starts.append((i, j))

AOCUtils.print_answer(1, get_min_dist(grid, start, end))

starts = [start] + starts

AOCUtils.print_answer(2, min(get_min_dist(grid, start, end) for start in starts))

AOCUtils.print_time_taken()