######################################
# --- Day 17: Reservoir Research --- #
######################################

import AOCUtils
from sys import setrecursionlimit
setrecursionlimit(5000)

class Ground:
    def __init__(self, x_dim, y_dim):
        self.x_dim, self.y_dim = x_dim, y_dim
        self.x_size, self.y_size = x_dim[1]-x_dim[0]+1, y_dim[1]-y_dim[0]+1
        self.tiles = [['.' for _ in range(self.x_size)] for _ in range(self.y_size)]

    def set_clay(self, clay):
        for c in clay:
            c = (c[0]-self.x_dim[0], c[1]-self.y_dim[0])
            self.tiles[c[1]][c[0]] = '#'

    def get(self, pos): return self.tiles[pos[1]][pos[0]] if self.exists(pos) else None
    def set(self, pos, data): self.tiles[pos[1]][pos[0]] = data

    def exists(self, pos): return 0 <= pos[0] < self.x_size and 0 <= pos[1] < self.y_size
    def is_barrier(self, pos): return (self.get(pos) == '#' or self.get(pos) == '~')

    def simulate(self, waterFountain):
        self._simulate((waterFountain[0]-self.x_dim[0], waterFountain[1]))

    def _simulate(self, pos):
        self.set(pos, '|')

        down = (pos[0], pos[1]+1)
        left = (pos[0]-1, pos[1])
        right = (pos[0]+1, pos[1])

        # If it can still fall, recursive call for down position
        if self.get(down) == '.':
            self._simulate(down)

        left_wall = None
        scout = pos[0]
        while scout > 0 and self.is_barrier((scout, pos[1]+1)):
            scout -= 1
            if self.is_barrier((scout, pos[1])):
                left_wall = scout
                break

        right_wall = None
        scout = pos[0]
        while scout < self.x_size and self.is_barrier((scout, pos[1]+1)):
            scout += 1
            if self.is_barrier((scout, pos[1])):
                right_wall = scout
                break

        # If position is bound by two walls, it can be made into still water
        if left_wall and right_wall:
            for i in range(left_wall+1, right_wall):
                self.set((i, pos[1]), '~')
        else: # Otherwise, recursivelly call for left and right positions
            if self.exists(down) and self.get(down) != '|' and self.get(left) == '.':
                self._simulate(left)

            if self.exists(down) and self.get(down) != '|' and self.get(right) == '.':
                self._simulate(right)

    def count_element(self, element):
        return sum(y.count(element) for y in self.tiles)

######################################

scan = AOCUtils.load_input(17)
clay = set()
min_x, max_x, min_y, max_y = None, None, None, None

for s in scan:
    s = s.split(', ')
    x = s[0].split('=')[1] # Assume first coordinates are x
    y = s[1].split('=')[1]
    if s[0][0] == 'y': x, y = y, x # If first coordinates are y, swap

    x0, x1 = ([int(i) for i in x.split('..')]) if '..' in x else (int(x), int(x))
    if not min_x or x0 < min_x: min_x = x0
    if not max_x or x1 > max_x: max_x = x1

    y0, y1 = ([int(i) for i in y.split('..')]) if '..' in y else (int(y), int(y))
    if not min_y or y0 < min_y: min_y = y0
    if not max_y or y1 > max_y: max_y = y1

    for x in range(x0, x1+1):
        for y in range(y0, y1+1):
            clay.add((x, y))

ground = Ground((min_x-1, max_x+1), (min_y, max_y))
ground.set_clay(clay)

ground.simulate((500, 0))

running_water = ground.count_element('|')
still_water =  ground.count_element('~')
AOCUtils.print_answer(1, running_water + still_water)
AOCUtils.print_answer(2, still_water)

AOCUtils.print_time_taken()