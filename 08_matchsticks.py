##############################
# --- Day 8: Matchsticks --- #
##############################

import AOCUtils

def countCode(s):
    # Remove first and last chars (")
    s = s[1:-1]
    n = 2

    i = 0
    while i < len(s):
        if s[i] == "\\":
            n += 1 # Skip \
            i += 1
            if i < len(s) and s[i] == "x":
                n += 2 # Skip xn
                i += 2
        i += 1

    return n

def encode(s):
    encoded = ""

    for c in s:
        if c in '"\\':
            encoded += '\\'
        encoded += c

    return '"' + ''.join(encoded) + '"'

##############################

strings = AOCUtils.loadInput(8)

total = sum(countCode(s) for s in strings)
print("Part 1: {}".format(total))

strings = [encode(s) for s in strings]

total = sum(countCode(s) for s in strings)
print("Part 2: {}".format(total))

AOCUtils.printTimeTaken()