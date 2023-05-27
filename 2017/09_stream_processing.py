####################################
# --- Day 9: Stream Processing --- #
####################################

import AOCUtils

def getComma(stream, p):
    if p < len(stream):
        while stream[p] == ",":
            p += 1 # ,

    return p

def getCancel(stream, p):
    if p < len(stream):
        while stream[p] == "!":
            p += 2 # ! and next

    return p

def getGarbage(stream, p):
    removed = 0

    if p < len(stream):
        while stream[p] == "<":
            p += 1 # <

            while stream[p] != ">":
                p = getCancel(stream, p)

                if stream[p] != ">":
                    p += 1 # garbage
                    removed += 1

            p += 1 # >

            p = getComma(stream, p)

    return p, removed

def getGroup(stream, p=0, level=1):
    score = 0
    removed = 0

    p, nremoved = getGarbage(stream, p)
    removed += nremoved

    while p < len(stream) and stream[p] == "{":
        p += 1 # {
        p, nscore, nremoved = getGroup(stream, p, level+1)
        score += nscore
        removed += nremoved

        p, nremoved = getGarbage(stream, p)
        removed += nremoved

        if stream[p] == "}":
            p += 1 # }
            score += level

        p = getComma(stream, p)

    return (p, score, removed)

####################################

stream = AOCUtils.loadInput(9)

_, score, removed = getGroup(stream)

print("Part 1: {}".format(score))

print("Part 2: {}".format(removed))

AOCUtils.printTimeTaken()