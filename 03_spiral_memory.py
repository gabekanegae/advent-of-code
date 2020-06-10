################################
# --- Day 3: Spiral Memory --- #
################################

import AOCUtils

################################

square = AOCUtils.loadInput(3)

x, y = 0, 0
edgeCount = 0
step = 1
done = False

while not done:
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
        
        step += 1
        if step == square:
            distance = abs(x) + abs(y)
            done = True
            break

    edgeCount += 1

print("Part 1: {}".format(distance))

x, y = 0, 0
edgeCount = 0
seen = {(0, 0): 1}
done = False

while not done:
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
        
        seen[(x, y)] = sum(seen[(x+dx, y+dy)] for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (x+dx, y+dy) in seen)
        if seen[(x, y)] > square:
            done = True
            break

    edgeCount += 1

print("Part 2: {}".format(seen[(x, y)]))

AOCUtils.printTimeTaken()