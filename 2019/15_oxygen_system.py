#################################
# --- Day 15: Oxygen System --- #
#################################

import AOCUtils
from intcodeVM import VM
from collections import deque

def explore(start, startVM, moves):
    queue = deque([start])
    vms = {start: startVM}
    maze = {start: 1}
    while queue:
        cur = queue.popleft()

        for m in range(len(moves)):
            step = (cur[0]+moves[m][0], cur[1]+moves[m][1])
            if step not in maze:
                vms[step] = vms[cur].copy()
                vms[step].run(m+1)
                maze[step] = vms[step].output[-1]
                if maze[step] != 0:
                    queue.append(step)

    return maze

def find_oxygen(maze, start, moves):
    queue = deque([(start, 0)])
    visited = set()
    while queue:
        cur, dist = queue.popleft()

        if cur in visited: continue
        visited.add(cur)

        if maze[cur] == 2:
            return (cur, dist)

        for move in moves:
            step = (cur[0]+move[0], cur[1]+move[1])
            if maze[step] != 0:
                queue.append((step, dist+1))

def time_to_fill(maze, oxygen, moves):
    max_distance = 0

    queue = deque([(oxygen, 0)])
    visited = set()
    while queue:
        cur, distance = queue.popleft()

        if cur in visited: continue
        visited.add(cur)

        max_distance = max(max_distance, distance)

        for move in moves:
            step = (cur[0]+move[0], cur[1]+move[1])
            if maze[step] != 0:
                queue.append((step, distance+1))

    return max_distance

#################################

raw_program = AOCUtils.load_input(15)
memory = [int(i) for i in raw_program.split(',')]

start = (0, 0)
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
maze = explore(start, VM(memory), moves)

oxygen, distance = find_oxygen(maze, start, moves)
AOCUtils.print_answer(1, distance)

time = time_to_fill(maze, oxygen, moves)
AOCUtils.print_answer(2, time)

AOCUtils.print_time_taken()