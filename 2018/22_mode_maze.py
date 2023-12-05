#############################
# --- Day 22: Mode Maze --- #
#############################

import AOCUtils
from heapq import heappush, heappop

# Equipment X is not allowed in region X
ROCKY, WET, NARROW = 0, 1, 2
NEITHER, TORCH, CLIMBING = 0, 1, 2

class Cave:
    def __init__(self, depth, target, border):
        self.depth = depth
        self.target = target
        self.size = (target[0] + border, target[1] + border)

        self.geo_index = dict()
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                self.geo_index[(x, y)] = self._get_geo_index(x, y)

    def _get_erosion(self, x, y):
        return (self.geo_index[(x, y)] + self.depth) % 20183

    def _get_geo_index(self, x, y):
        if (x, y) in [(0, 0), self.target]:
            return 0
        elif y == 0:
            return x * 16807
        elif x == 0:
            return y * 48271
        else:
            return self._get_erosion(x-1, y) * self._get_erosion(x, y-1)

    def get_risk_level(self):
        risk = 0
        for x in range(self.target[0]+1):
            for y in range(self.target[1]+1):
                risk += (self._get_erosion(x, y) % 3)
        return risk

    def get_fastest_path(self):
        start = ((0, 0), TORCH)
        heap = [(0, start)]
        visited = {start: 0}

        def step():
            for delta in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nxt = (cur[0] + delta[0], cur[1] + delta[1])

                # There is a faster path
                if (nxt, equip) in visited and visited[(nxt, equip)] <= time: continue

                # Out of bounds
                if not (0 <= nxt[0] < self.size[0] and 0 <= nxt[1] < self.size[1]): continue
                
                # Equipment not allowed
                if self._get_erosion(nxt[0], nxt[1]) % 3 == equip: continue

                visited[(nxt, equip)] = time
                heappush(heap, (time, (nxt, equip)))

        while heap:
            time, (cur, equip) = heappop(heap)
            
            # Reached target
            if cur == self.target and equip == TORCH:
                break

            # No change in equipment
            time += 1
            step()

            # Change in equipment
            time += 7
            for equip in [(equip+1)%3, (equip+2)%3]:
                # Only equipments that are allowed in next region
                if self._get_erosion(cur[0], cur[1]) % 3 != equip:
                    step()

        return time

#############################

scan = AOCUtils.load_input(22)

depth = int(scan[0].split()[1])

target = tuple(map(int, scan[1].split()[1].split(',')))

border = 100 # Allow BFS to go beyond target by this much
cave = Cave(depth, target, border)

AOCUtils.print_answer(1, cave.get_risk_level())

AOCUtils.print_answer(2, cave.get_fastest_path())

AOCUtils.print_time_taken()