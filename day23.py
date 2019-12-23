########################################################
# --- Day 23: Experimental Emergency Teleportation --- #
########################################################

import AOCUtils
from heapq import heappush, heappop

class Bot:
    def __init__(self, pos, r):
        self.pos = pos
        self.r = r

    def distanceTo(self, other):
        return sum([abs(a-b) for a, b in zip(self.pos, other.pos)])

class Box:
    def __init__(self, low, high):
        self.low, self.high = low, high

    def isInRangeOfBot(self, bot):
        dist = 0
        for boxLow, b, boxHigh in zip(self.low, bot.pos, self.high):
            boxHigh -= 1
            dist += abs(b - boxLow) + abs(b - boxHigh) - (boxHigh - boxLow)

        return dist//2 <= bot.r

    def botsInRange(self, bots): return sum([self.isInRangeOfBot(b) for b in bots])
    def originDistance(self): return sum([abs(c) for c in self.low])

    def __lt__(self, other): return (self.low, self.high) < (other.low, other.high)

########################################################

rawInput = [s[5:].split(">, r=") for s in AOCUtils.loadInput(23)]
positions = [tuple([int(i) for i in s[0].split(",")]) for s in rawInput]
radii = [int(i[1]) for i in rawInput]

bots = [Bot(p, r) for p, r in zip(positions, radii)]

# Sort by largest radius, take first
bots.sort(key=lambda x: x.r, reverse=True)
strongestBot = bots[0]

botsInRange = sum([strongestBot.distanceTo(bot) < strongestBot.r for bot in bots])
print("Part 1: {}".format(botsInRange))

# Create a bounding box big enough for all bots and its ranges
maxCoord = max([max([abs(i)+b.r for i in b.pos]) for b in bots])
boundingBox = Box((-maxCoord, -maxCoord, -maxCoord), (maxCoord, maxCoord, maxCoord))
boundingBoxSize = 2*maxCoord

# Create heap ordered by: most bots in range, biggest size, least distance to origin
heap = [(-len(bots), -boundingBoxSize, boundingBox.originDistance(), boundingBox)]
while len(heap) > 0:
    _, size, originDistance, box = heappop(heap)

    if abs(size) == 1: # Box is 1x1x1 = single point
        print("Part 2: {}".format(originDistance))
        break

    # Break in 8 octants
    octSize = abs(size//2)
    for octant in [(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)]:
        octLow = ([boxLow + octSize*octCoord for boxLow, octCoord in zip(box.low, octant)])
        octHigh = (octLow[0]+octSize, octLow[1]+octSize, octLow[2]+octSize)
        boxOct = Box(octLow, octHigh)

        # Calculate bots in octant range and add to heap
        botsInRange = boxOct.botsInRange(bots)
        heappush(heap, (-botsInRange, -octSize, boxOct.originDistance(), boxOct))

AOCUtils.printTimeTaken()