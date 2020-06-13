################################
# --- Day 3: Spiral Memory --- #
################################

import AOCUtils

################################

square = AOCUtils.loadInput(3)

p1, p2 = None, None

x, y = 0, 0
edgeCount = 0
seen = {(0, 0): 1}

while not (p1 and p2):
    loopStart = True

    for _ in range((edgeCount//4 + 1) * 2):
        if edgeCount % 4 == 0:
            if loopStart: # >
                x += 1
                loopStart = False
            else:
                y -= 1 # ^
        elif edgeCount % 4 == 1: # <
            x -= 1
        elif edgeCount % 4 == 2: # v
            y += 1
        elif edgeCount % 4 == 3: # >
            x += 1
        
        seen[(x, y)] = 0 if p2 else sum(seen[(x+dx, y+dy)] for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (x+dx, y+dy) in seen)

        if not p1 and len(seen) == square:
            p1 = abs(x) + abs(y)
        if not p2 and seen[(x, y)] > square:
            p2 = seen[(x, y)]
        if p1 and p2:
            break

    edgeCount += 1

print("Part 1: {}".format(p1))
print("Part 2: {}".format(p2))

AOCUtils.printTimeTaken()