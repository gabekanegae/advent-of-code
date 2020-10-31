#########################################
# --- Day 10: Elves Look, Elves Say --- #
#########################################

import AOCUtils

def lookAndSay(s):
    out = []

    last = s[0]
    count = 1
    for c in s[1:]:
        if c == last:
            count += 1
        else:
            out.append(str(count))
            out.append(last)

            count = 1
            last = c

    out.append(str(count))
    out.append(last)

    return out

#########################################

sequence = str(AOCUtils.loadInput(10))

for _ in range(40):
    sequence = lookAndSay(sequence)

print("Part 1: {}".format(len(sequence)))

sequence = str(AOCUtils.loadInput(10))

for _ in range(50):
    sequence = lookAndSay(sequence)

print("Part 2: {}".format(len(sequence)))

AOCUtils.printTimeTaken()