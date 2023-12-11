#############################
# --- Day 10: Pipe Maze --- #
#############################

import AOCUtils
from collections import deque

pipe_neighbors = {'|': sorted('NS'),
                  '-': sorted('EW'),
                  'L': sorted('NE'),
                  'J': sorted('NW'),
                  '7': sorted('SW'),
                  'F': sorted('SE')}

moves = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}

inv_dir = {'N': 'S', 'S': 'N', 'W': 'E', 'E': 'W'}

#############################

raw_maze = AOCUtils.load_input(10)
maze = list(map(list, raw_maze))

height, width = len(maze), len(maze[0])

start = None
for x in range(height):
    if start: break
    for y in range(width):
        if maze[x][y] == 'S':
            start = (x, y)
            break

start_moves = []
for move, delta in moves.items():
    neighbor = (start[0] + delta[0], start[1] + delta[1])
    if inv_dir[move] in pipe_neighbors[maze[neighbor[0]][neighbor[1]]]:
        start_moves.append(move)

start_pipe = next(k for k, v in pipe_neighbors.items() if sorted(start_moves) == v)
maze[start[0]][start[1]] = start_pipe

max_dist = 0
queue = deque([(start, 0)])
loop = set()
while queue:
    cur, dist = queue.popleft()
    loop.add(cur)

    max_dist = max(max_dist, dist)

    for neighbor in pipe_neighbors[maze[cur[0]][cur[1]]]:
        delta = moves[neighbor]
        nxt = (cur[0] + delta[0], cur[1] + delta[1])
        if nxt not in loop:
            queue.append((nxt, dist+1))

AOCUtils.print_answer(1, max_dist)

# Scanline approach, keeping track of whenever we go from
# outside -> inside -> outside the shape (| or FJ or L7)
inside = set()
for x in range(height):
    is_inside = False
    last_edge = ''
    for y in range(width):
        if (x, y) in loop:
            edge = maze[x][y]
            if edge == '|' or (last_edge + edge in ['FJ', 'L7']):
                is_inside = ~is_inside
            if edge in 'FJL7|':
                last_edge = edge
        elif is_inside:
            inside.add((x, y))

AOCUtils.print_answer(2, len(inside))

AOCUtils.print_time_taken()
