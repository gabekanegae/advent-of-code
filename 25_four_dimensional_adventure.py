##############################################
# --- Day 25: Four-Dimensional Adventure --- #
##############################################

import AOCUtils

def manhattan(p1, p2):
    return sum([abs(a-b) for a, b in zip(p1, p2)])

class UnionFind:
    def __init__(self, size):
        self.constellation = [i for i in range(size)]
        self.totalConstellations = size

    def find(self, i):
        if self.constellation[i] == i:
            return i
        else:
            return self.find(self.constellation[i])

    def union(self, i, j):
        i, j = self.find(i), self.find(j)

        if i == j: return

        self.constellation[i] = j
        self.totalConstellations -= 1

##############################################

rawPoints = AOCUtils.loadInput(25)
points = [tuple([int(i) for i in p.split(",")]) for p in rawPoints]

uf = UnionFind(len(points))

for i, p in enumerate(points):
    for j, q in enumerate(points):
        if manhattan(p, q) <= 3:
            uf.union(i, j)

print("Part 1: {}".format(uf.totalConstellations))

AOCUtils.printTimeTaken()