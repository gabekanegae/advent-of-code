###############################
# --- Day 9: Marble Mania --- #
###############################

import AOCUtils

class CircularLL:
    def __init__(self, value):
        self.cur = Node(value)
        self.size = 1
        self.cur.prev = self.cur
        self.cur.next = self.cur

    def insert(self, value):
        self.cur = self.cur.next

        new = Node(value)       
        new.prev = self.cur
        new.next = self.cur.next
        self.cur.next.prev = new
        self.cur.next = new

        self.cur = new
        self.size += 1

    def remove(self):
        for _ in range(7):
            self.cur = self.cur.prev

        self.cur.prev.next = self.cur.next
        self.cur.next.prev = self.cur.prev

        value = self.cur.value
        self.cur = self.cur.next
        self.size -= 1

        return value

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

###############################

game = AOCUtils.loadInput(9).split()
playerAmt, marbleAmt = int(game[0]), int(game[6])

playerScores = [0 for _ in range(playerAmt)]

circle = CircularLL(0)

for marble in range(1, marbleAmt*100+1):
    curPlayer = (marble%playerAmt)-1

    if marble % 23 != 0:
        circle.insert(marble)
    else:
        playerScores[curPlayer] += marble
        playerScores[curPlayer] += circle.remove()

    if marble == marbleAmt:
        print("Part 1: {}".format(max(playerScores)))
    elif marble == marbleAmt*100:
        print("Part 2: {}".format(max(playerScores)))

AOCUtils.printTimeTaken()