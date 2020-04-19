##################################
# --- Day 11: Chronal Charge --- #
##################################

import AOCUtils

def getMaxSum(m, sqSize):
    maxSum, maxCoords = None, None
    for x in range(sqSize-1, 300):
        for y in range(sqSize-1, 300):
            # 2D Partial Sum
            curSum = partials[x][y]
            if x-sqSize >= 0: curSum -= partials[x-sqSize][y]
            if y-sqSize >= 0: curSum -= partials[x][y-sqSize]
            if x-sqSize >= 0 and y-sqSize >= 0: curSum += partials[x-sqSize][y-sqSize]

            if not maxSum or curSum > maxSum:
                maxSum, maxCoords = curSum, (x-(sqSize-1), y-(sqSize-1))
    return maxSum, maxCoords

##################################

serial = AOCUtils.loadInput(11)

cells = [[None for _ in range(300)] for _ in range(300)]
for x in range(300):
    for y in range(300):
        cells[x][y] = ((((x+10)*y+serial)*(x+10)//100)%10)-5

partials = [[cells[x][y] for y in range(300)] for x in range(300)]
for x in range(300):
    for y in range(300):
        if x-1 >= 0: partials[x][y] += partials[x-1][y]
        if y-1 >= 0: partials[x][y] += partials[x][y-1]
        if x-1 >= 0 and y-1 >= 0: partials[x][y] -= partials[x-1][y-1]

curSum, curCoords = getMaxSum(partials, 3)
print("Part 1: {},{}".format(curCoords[0], curCoords[1]))

maxSum, maxCoords, maxSize = None, None, None
for i in range(1, 301):
    curSum, curCoords = getMaxSum(partials, i)
    if not maxSum or curSum > maxSum:
        maxSum, maxCoords, maxSize = curSum, curCoords, i
print("Part 2: {},{},{}".format(maxCoords[0], maxCoords[1], maxSize))

AOCUtils.printTimeTaken()