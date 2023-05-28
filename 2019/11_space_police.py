################################
# --- Day 11: Space Police --- #
################################

import AOCUtils
from intcodeVM import VM

def painting_robot(memory, start):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    pos = (0, 0)
    facing = 0
    painted = {(0, 0): start}

    vm = VM(memory)
    while not vm.halted:
        vm.run(pos in painted and painted[pos] == 1)
        color, rotation = vm.output[-2:]
        
        painted[pos] = color

        if rotation == 0: # Left
            facing += 1
        elif rotation == 1: # Right
            facing -= 1
        facing %= len(directions)

        step = directions[facing]
        pos = (pos[0]+step[0], pos[1]+step[1])

    return painted

################################

raw_program = AOCUtils.load_input(11)
memory = [int(i) for i in raw_program.split(',')]

painted = painting_robot(memory, 0)
AOCUtils.print_answer(1, len(painted))

painted = painting_robot(memory, 1)
white_panels = [k for k, v in painted.items() if v == 1]

min_point = list(white_panels[0])
max_point = list(white_panels[0])
for p in white_panels[1:]:
    if p[0] < min_point[0]: min_point[0] = p[0]
    elif p[0] > max_point[0]: max_point[0] = p[0]
    if p[1] < min_point[0]: min_point[1] = p[1]
    elif p[1] > max_point[1]: max_point[1] = p[1]

white_panels_image = []
for x in range(min_point[0], max_point[0]+1):
    l = [(x, y) in white_panels for y in range(min_point[1], max_point[1]+1)]
    white_panels_image.append(l)

AOCUtils.print_answer(2, white_panels_image)

AOCUtils.print_time_taken()