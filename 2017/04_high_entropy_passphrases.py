###########################################
# --- Day 4: High-Entropy Passphrases --- #
###########################################

import AOCUtils

###########################################

passphrases = [s.split() for s in AOCUtils.loadInput(4)]
print("Part 1: {}".format(sum(len(p) == len(set(p)) for p in passphrases)))

passphrases = [["".join(sorted(word)) for word in p] for p in passphrases]
print("Part 2: {}".format(sum(len(p) == len(set(p)) for p in passphrases)))

AOCUtils.printTimeTaken()