############################################
# --- Day 8: Two-Factor Authentication --- #
############################################

import AOCUtils

############################################

instructions = AOCUtils.loadInput(8)
w, h = 50, 6

screen = [["." for _ in range(w)] for _ in range(h)]

for inst in instructions:
    if inst.startswith("rect"):
        a, b = map(int, inst.split()[1].split("x"))
        
        for j in range(a):
            for i in range(b):
                screen[i][j] = "#"
    elif inst.startswith("rotate row"):
        inst = inst.split()
        x, d = int(inst[2].split("=")[1]), int(inst[-1])

        screen[x] = screen[x][-d:] + screen[x][:-d]
    elif inst.startswith("rotate column"):
        inst = inst.split()
        y, d = int(inst[2].split("=")[1]), int(inst[-1])

        col = [screen[i][y] for i in range(h)]
        for i in range(h):
            screen[i][y] = col[(i-d)%h]


print("Part 1: {}".format(sum(screen[x].count("#") for x in range(h))))

print("Part 2:")
for i in range(h):
    for j in range(w):
        if screen[i][j] == "#":
            print("##", end="")
        else:
            print("  ", end="")
    print()

AOCUtils.printTimeTaken()