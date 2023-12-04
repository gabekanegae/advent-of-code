############################################
# --- Day 8: Two-Factor Authentication --- #
############################################

import AOCUtils

############################################

instructions = AOCUtils.load_input(8)
w, h = 50, 6

screen = [['.' for _ in range(w)] for _ in range(h)]

for inst in instructions:
    if inst.startswith('rect'):
        a, b = map(int, inst.split()[1].split('x'))
        
        for j in range(a):
            for i in range(b):
                screen[i][j] = '#'
    elif inst.startswith('rotate row'):
        inst = inst.split()
        x, d = int(inst[2].split('=')[1]), int(inst[-1])

        screen[x] = screen[x][-d:] + screen[x][:-d]
    elif inst.startswith('rotate column'):
        inst = inst.split()
        y, d = int(inst[2].split('=')[1]), int(inst[-1])

        col = [screen[i][y] for i in range(h)]
        for i in range(h):
            screen[i][y] = col[(i-d)%h]

AOCUtils.print_answer(1, sum(screen[x].count('#') for x in range(h)))

screen_lines = []
for i in range(h):
    # line = [screen[i][j] == '#' for j in range(w)]ä
    line = []
    for j in range(w):
        line.append(screen[i][j] == '#')
    screen_lines.append(line)

AOCUtils.print_answer(2, screen_lines)

AOCUtils.print_time_taken()