######################################
# --- Day 17: Reservoir Research --- #
######################################

import AOCUtils
from collections import defaultdict

class Ground:
    def __init__(self, clay, source):
        # For x, water can go up to 1 block to the left/right of existing clay blocks
        min_x, max_x = min(x for x, _ in clay)-1, max(x for x, _ in clay)+1
        min_y, max_y = min(y for _, y in clay),   max(y for _, y in clay)

        self.bounds = ((min_x, max_x+1), (min_y, max_y+1))

        # Move source down to min_y
        self.source = (source[0], max(source[1], min_y))

        self.grid = defaultdict(lambda: '.')
        for c in clay:
            self.grid[c] = '#'

    def _is_valid(self, pos):
        return self.bounds[0][0] <= pos[0] < self.bounds[0][1] and \
               self.bounds[1][0] <= pos[1] < self.bounds[1][1]

    def count(self, c):
        return list(self.grid.values()).count(c)

    def simulate(self):
        stack = [self.source]
        while stack:
            cur = stack[-1] # Peek top
            self.grid[cur] = '|'

            down = (cur[0], cur[1]+1)
            if self._is_valid(down) and self.grid[down] == '.':
                stack.append(down)
            else:
                stack.pop()

                left_wall = None
                scout = cur[0]
                while self._is_valid((scout, cur[1])) and self.grid[(scout, cur[1]+1)] in '~#':
                    scout -= 1
                    if self.grid[(scout, cur[1])] in '~#':
                        left_wall = scout
                        break

                right_wall = None
                scout = cur[0]
                while self._is_valid((scout, cur[1])) and self.grid[(scout, cur[1]+1)] in '~#':
                    scout += 1
                    if self.grid[(scout, cur[1])] in '~#':
                        right_wall = scout
                        break

                if left_wall and right_wall:
                    for i in range(left_wall+1, right_wall):
                        self.grid[(i, cur[1])] = '~'
                elif self._is_valid(down) and self.grid[down] != '|':
                    left = (cur[0]-1, cur[1])
                    if self.grid[left] == '.':
                        stack.append(left)
                
                    right = (cur[0]+1, cur[1])
                    if self.grid[right] == '.':
                        stack.append(right)

    def __str__(self):
        s = []
        for y in range(*self.bounds[1]):
            for x in range(*self.bounds[0]):
                s.append(self.grid[(x, y)])
            s.append('\n')

        return ''.join(s)

######################################

scan = AOCUtils.load_input(17)
source = (500, 0)

clay = set()
for s in scan:
    s = s.split(', ')
    x = s[0].split('=')[1] # Assume first coordinates are x
    y = s[1].split('=')[1]
    if s[0][0] == 'y': x, y = y, x # If first coordinates are y, swap

    min_x, max_x = tuple(map(int, x.split('..'))) if '..' in x else (int(x), int(x))
    min_y, max_y = tuple(map(int, y.split('..'))) if '..' in y else (int(y), int(y))

    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            clay.add((x, y))

ground = Ground(clay, source)
ground.simulate()

# print(ground)

running_water = ground.count('|')
still_water = ground.count('~')

AOCUtils.print_answer(1, running_water + still_water)
AOCUtils.print_answer(2, still_water)

AOCUtils.print_time_taken()