#######################################
# --- Day 5: Alchemical Reduction --- #
#######################################

import AOCUtils

def diffPolarity(a, b):
    return ord(a) == ord(b)+32 or ord(a)+32 == ord(b)

def react(polymer):
    stack = []
    for p in polymer:
        if len(stack) == 0 or not diffPolarity(p, stack[-1]):
            stack.append(p)
        else:
            stack.pop()

    return len(stack)

#######################################

polymer = AOCUtils.loadInput(5)

print("Part 1: {}".format(react(polymer)))

minSize, minType = None, None
for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    newPolymer = "".join(p for p in polymer if p.upper() != c.upper())
    newSize = react(newPolymer)
    if not minSize or newSize < minSize:
        minSize = newSize
        minType = c

print("Part 2: {}".format(minSize))

AOCUtils.printTimeTaken()