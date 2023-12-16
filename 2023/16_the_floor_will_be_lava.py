##########################################
# --- Day 16: The Floor Will Be Lava --- #
##########################################

import AOCUtils

moves_4 = {
    'U': (-1,  0),
    'D': ( 1,  0),
    'L': ( 0, -1),
    'R': ( 0,  1)
}

mirrors = {
     '.': {'U':  'U', 'R':  'R', 'L':  'L', 'D':  'D'},
     '/': {'U':  'R', 'R':  'U', 'L':  'D', 'D':  'L'},
    '\\': {'U':  'L', 'R':  'D', 'L':  'U', 'D':  'R'},
     '|': {'U':  'U', 'R': 'UD', 'L': 'UD', 'D':  'D'},
     '-': {'U': 'LR', 'R':  'R', 'L':  'L', 'D': 'LR'},
}

def count_energized_tiles(layout, start):
    visited = set()
    energized_tiles = set()

    queue = [start]
    while queue:
        x, y, direction = queue.pop()

        if not (0 <= x < len(layout) and 0 <= y < len(layout[0])):
            continue
        if (x, y, direction) in visited:
            continue

        visited.add((x, y, direction))
        energized_tiles.add((x, y))

        for nxt_direction in mirrors[layout[x][y]][direction]:
            delta = moves_4[nxt_direction]
            queue.append((x+delta[0], y+delta[1], nxt_direction))

    return len(energized_tiles)

##########################################

layout = AOCUtils.load_input(16)
h, w = len(layout), len(layout[0])

AOCUtils.print_answer(1, count_energized_tiles(layout, (0, 0, 'R')))

edge = [(  0,   i, 'D') for i in range(w)] + \
       [(h-1,   i, 'U') for i in range(w)] + \
       [(  i,   0, 'R') for i in range(h)] + \
       [(  i, w-1, 'L') for i in range(h)]

AOCUtils.print_answer(2, max(count_energized_tiles(layout, start) for start in edge))

AOCUtils.print_time_taken()
