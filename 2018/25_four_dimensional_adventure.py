##############################################
# --- Day 25: Four-Dimensional Adventure --- #
##############################################

import AOCUtils

def manhattan(p1, p2):
    return sum(abs(a-b) for a, b in zip(p1, p2))

class UnionFind:
    def __init__(self, size):
        self.constellation = [i for i in range(size)]
        self.total_constellations = size

    def find(self, i):
        if self.constellation[i] == i:
            return i
        else:
            return self.find(self.constellation[i])

    def union(self, i, j):
        i, j = self.find(i), self.find(j)

        if i == j: return

        self.constellation[i] = j
        self.total_constellations -= 1

##############################################

raw_points = AOCUtils.load_input(25)
points = [tuple(map(int, p.split(','))) for p in raw_points]

union_find = UnionFind(len(points))

for i, p in enumerate(points):
    for j, q in enumerate(points):
        if manhattan(p, q) <= 3:
            union_find.union(i, j)

AOCUtils.print_answer(1, union_find.total_constellations)

AOCUtils.print_time_taken()