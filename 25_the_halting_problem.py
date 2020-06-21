#######################################
# --- Day 25: The Halting Problem --- #
#######################################

import AOCUtils

#######################################

rawInput = [s.strip()[:-1] if s else "" for s in AOCUtils.loadInput(25)]

startState = rawInput[0][-1]
steps = int(rawInput[1].split()[-2])

rawStates = [s.split()[-1] for s in rawInput[2:] if s]

states = dict()
for i in range(0, len(rawStates), 9):
    cur = rawStates[i]

    state = dict()
    for j in range(i, i+2*4, 4):
        value = int(rawStates[j+1])
        write = int(rawStates[j+2])
        move = 1 if rawStates[j+3] == "right" else -1
        nxt = rawStates[j+4]

        state[value] = {"write": write, "move": move, "nxt": nxt}

    states[cur] = state

curState = startState
curPos = 0

tape = dict()
for step in range(steps):
    if curPos not in tape:
        tape[curPos] = 0

    action = states[curState][tape[curPos]]

    tape[curPos] = action["write"]
    curPos += action["move"]
    curState = action["nxt"]

checksum = sum(tape.values())
print("Part 1: {}".format(checksum))

AOCUtils.printTimeTaken()