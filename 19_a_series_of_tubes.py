#####################################
# --- Day 19: A Series of Tubes --- #
#####################################

import AOCUtils

#####################################

diagram = AOCUtils.loadInput(19)

h, w = len(diagram), len(diagram[0])

cx, cy = None, None
for y in range(w):
    if diagram[0][y] != " ":
        cx, cy = 0, y
        break

seenLetters = []
steps = 0

px, py = -1, cy
nx, ny = 1, cy
while diagram[cx][cy] != " ":
    if diagram[cx][cy].isalpha():
        seenLetters.append(diagram[cx][cy])

    if diagram[cx][cy] != "+":
        nx, ny = cx+cx-px, cy+cy-py
    else:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx+dx, cy+dy
            
            if not (0 <= nx < h and 0 <= ny < w): continue
            if (nx, ny) == (px, py): continue
            if diagram[nx][ny] == " ": continue
            
            break

    px, py = cx, cy
    cx, cy = nx, ny
    steps += 1

print("Part 1: {}".format("".join(seenLetters)))
print("Part 2: {}".format(steps))

AOCUtils.printTimeTaken()