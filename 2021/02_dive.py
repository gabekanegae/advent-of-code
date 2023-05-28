########################
# --- Day 2: Dive! --- #
########################

import AOCUtils

########################

course = AOCUtils.load_input(2)

pos, depth = 0, 0
for step in course:
    direction, delta = step.split()
    delta = int(delta)
    
    if direction == 'forward':
        pos += delta
    elif direction == 'down':
        depth += delta
    elif direction == 'up':
        depth -= delta

AOCUtils.print_answer(1, pos * depth)

pos, depth, aim = 0, 0, 0
for step in course:
    direction, delta = step.split()
    delta = int(delta)

    if direction == 'forward':
        pos += delta
        depth += aim * delta
    elif direction == 'down':
        aim += delta
    elif direction == 'up':
        aim -= delta

AOCUtils.print_answer(2, pos * depth)

AOCUtils.print_time_taken()