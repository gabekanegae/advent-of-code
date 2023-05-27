#########################################
# --- Day 16: Permutation Promenade --- #
#########################################

import AOCUtils

def dance(programs, moves):
    programs = list(programs)
    for move in moves:
        if move[0] == "s":
            n = int(move[1:])
            programs = programs[-n:] + programs[:-n]
        elif move[0] == "x":
            a, b = [int(i) for i in move[1:].split("/")]
            programs[a], programs[b] = programs[b], programs[a]
        elif move[0] == "p":
            a, b = move[1], move[3]
            pa, pb = programs.index(a), programs.index(b)
            programs[pa], programs[pb] = programs[pb], programs[pa]

    return "".join(programs)

#########################################

origPrograms = "abcdefghijklmnop"
moves = AOCUtils.loadInput(16).split(",")

programs = origPrograms
print("Part 1: {}".format(dance(programs, moves)))

programs = origPrograms
seenStr = {programs: 0}
seenID = {0: programs}

i = 1
while True:
    programs = dance(programs, moves)
    if programs in seenStr:
        loop = (seenStr[programs], i)
        break

    seenStr[programs] = i
    seenID[i] = programs

    i += 1

loop = (1000000000 - loop[0]) % (loop[1] - loop[0])
print("Part 2: {}".format(seenID[loop]))

AOCUtils.printTimeTaken()