###################################
# --- Day 16: Dragon Checksum --- #
###################################

import AOCUtils

def getChecksum(data, diskLen):
    inv = {"0": "1", "1": "0"}
    data = list(data)

    while len(data) < diskLen:
        b = [inv[c] for c in data[:][::-1]]
        data += ["0"]
        data += b

    data = data[:diskLen]

    while len(data) % 2 == 0:
        newData = []
        for i in range(0, len(data), 2):
            c = "1" if data[i] == data[i+1] else "0"
            newData.append(c)
        data = newData

    return "".join(data)

###################################

data = str(AOCUtils.loadInput(16))

print("Part 1: {}".format(getChecksum(data, 272)))

print("Part 2: {}".format(getChecksum(data, 35651584)))

AOCUtils.printTimeTaken()