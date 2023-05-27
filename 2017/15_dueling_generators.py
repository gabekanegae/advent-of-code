######################################
# --- Day 15: Dueling Generators --- #
######################################

import AOCUtils

class Generator:
    def __init__(self, factor, seed):
        self.factor = factor
        self.seed = seed

    def next(self):
        self.seed = (self.seed * self.factor) % 2147483647
        return self.seed

######################################

rawInput = AOCUtils.loadInput(15)

seedA, seedB = int(rawInput[0].split()[-1]), int(rawInput[1].split()[-1])
genA = Generator(16807, seedA)
genB = Generator(48271, seedB)

mask = 0xFFFF

judgeCount = 0
for i in range(40000000):
    genA.next()
    genB.next()
    
    if genA.seed & mask == genB.seed & mask:
        judgeCount += 1

print("Part 1: {}".format(judgeCount))

judgeCount = 0
for i in range(5000000):
    while genA.next() % 4 != 0:
        pass
    while genB.next() % 8 != 0:
        pass

    if genA.seed & mask == genB.seed & mask:
        judgeCount += 1

print("Part 2: {}".format(judgeCount))

AOCUtils.printTimeTaken()