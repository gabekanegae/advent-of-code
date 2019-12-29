###############################
# --- Day 9: Marble Mania --- #
###############################

import AOCUtils
from collections import deque

###############################

game = AOCUtils.loadInput(9).split()
playerAmt, marbleAmt = int(game[0]), int(game[6])

playerScores = [0 for _ in range(playerAmt)]
circle = deque([0])

for marble in range(1, marbleAmt*100+1):
    curPlayer = marble % playerAmt

    if marble % 23 != 0:
        circle.rotate(-1)
        circle.append(marble)
    else:
        circle.rotate(7)
        playerScores[curPlayer] += marble
        playerScores[curPlayer] += circle.pop()
        circle.rotate(-1)

    if marble == marbleAmt:
        print("Part 1: {}".format(max(playerScores)))
    elif marble == marbleAmt*100:
        print("Part 2: {}".format(max(playerScores)))

AOCUtils.printTimeTaken()