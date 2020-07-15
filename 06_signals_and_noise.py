####################################
# --- Day 6: Signals and Noise --- #
####################################

import AOCUtils

####################################

messages = AOCUtils.loadInput(6)
n = len(messages[0])

counts = [dict() for _ in range(n)]
for message in messages:
    for i, c in enumerate(message):
        if c not in counts[i]:
            counts[i][c] = 0
        counts[i][c] += 1

corrected = "".join([max((ct, c) for c, ct in count.items())[1] for count in counts])
print("Part 1: {}".format(corrected))

corrected = "".join([max((-ct, c) for c, ct in count.items())[1] for count in counts])
print("Part 2: {}".format(corrected))

AOCUtils.printTimeTaken()