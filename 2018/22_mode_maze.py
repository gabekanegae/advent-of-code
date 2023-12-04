#############################
# --- Day 22: Mode Maze --- #
#############################

import AOCUtils
from heapq import heappush, heappop

# Equipment X is not allowed in region X
ROCKY, WET, NARROW = 0, 1, 2
NEITHER, TORCH, CLIMBING = 0, 1, 2

BORDER = 100

class Cave:
    def __init__(self, depth, target, size):
        self.depth = depth
        self.target = target
        self.size = size

        self.geo_index = [[None for _ in range(self.size[1])] for _ in range(self.size[0])]
        for y in range(self.size[0]):
            for x in range(self.size[1]):
                self.geo_index[y][x] = self._get_geo_index((x, y))

    def _get_erosion(self, pos):
        return (self.geo_index[pos[1]][pos[0]] + self.depth) % 20183

    def _get_geo_index(self, pos):
        if pos == (0, 0) or pos == (self.target[1], self.target[0]):
            return 0
        elif pos[0] == 0:
            return pos[1] * 16807
        elif pos[1] == 0:
            return pos[0] * 48271
        else:
            return self._get_erosion((pos[0]-1, pos[1])) * self._get_erosion((pos[0], pos[1]-1))

    def get_risk_level(self):
        risk = 0
        for y in range(self.target[0]+1):
            for x in range(self.target[1]+1):
                risk += (self._get_erosion((x, y)) % 3)
        return risk

    def get_fastest_path(self):
        heap = [(0, (0, 0), TORCH)]
        visited = {(0, TORCH): 0}

        def step():
            for delta in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                npos = (pos[0]+delta[0], pos[1]+delta[1])
               
                # There is a faster path
                if (npos, equip) in visited and visited[(npos, equip)] <= time: continue

                # Out of bounds
                if npos[0] < 0 or npos[0] >= self.size[1] or npos[1] < 0 or npos[1] >= self.size[0]: continue
                
                # Equipment not allowed
                if self._get_erosion(npos) % 3 == equip: continue

                visited[(npos, equip)] = time
                heappush(heap, (time, npos, equip))

        while len(heap) > 0:
            time, pos, equip = heappop(heap)
            
            # Reached target
            if pos == (self.target[1], self.target[0]) and equip == TORCH:
                break

            # No change in equipment
            time += 1
            step()

            # Change in equipment
            time += 7
            for equip in [(equip+1)%3, (equip+2)%3]:
                # Only equipments that are allowed in next region
                if self._get_erosion(pos) % 3 != equip:
                    step()

        return time

#############################

scan = AOCUtils.load_input(22)

depth = int(scan[0].split()[1])
target = tuple(map(int, scan[1].split()[1].split(',')))

cave = Cave(depth, target, (target[0]+BORDER, target[1]+BORDER))

AOCUtils.print_answer(1, cave.get_risk_level())

AOCUtils.print_answer(2, cave.get_fastest_path())

AOCUtils.print_time_taken()