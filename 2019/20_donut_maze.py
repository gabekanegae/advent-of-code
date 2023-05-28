##############################
# --- Day 20: Donut Maze --- #
##############################

import AOCUtils
from collections import deque

class Maze:
    def __init__(self, raw):
        self.maze = [s[:] for s in raw]
        self.start, self.end = None, None
        self.size = (len(raw), len(raw[0]))

        raw_inner, raw_outer = dict(), dict()
        for y in range(self.size[0]):
            for x in range(self.size[1]):
                portal_name, portal_pos = self._parse_portal((y, x))
                if not portal_name or not portal_pos: continue

                if portal_name == 'AA':
                    self.start = portal_pos
                elif portal_name == 'ZZ':
                    self.end = portal_pos
                else:
                    if 1 < y < self.size[0]-2 and 1 < x < self.size[1]-2:
                        raw_inner[portal_name] = portal_pos
                    else:
                        raw_outer[portal_name] = portal_pos

        self.outer_portals = {v: raw_inner[k] for k, v in raw_outer.items()}
        self.inner_portals = {v: raw_outer[k] for k, v in raw_inner.items()}

    def _is_portal(self, pos):
        return 0 <= pos[0] <= self.size[0] and 0 <= pos[1] <= self.size[1] and 'A' <= self.maze[pos[0]][pos[1]] <= 'Z'
    def _is_walkable(self, pos):
        return 0 <= pos[0] <= self.size[0] and 0 <= pos[1] <= self.size[1] and self.maze[pos[0]][pos[1]] == '.'

    def _parse_portal(self, pos):
        if not self._is_portal(pos): return None, None
        
        y, x = pos
        name, pos = None, None
        if self._is_portal((y+1, x)): # Vertical (top-to-bottom)
            name = self.maze[y][x] + self.maze[y+1][x]

            # Find portal entrance
            if self._is_walkable((y-1, x)): # Up
                pos = (y-1, x)
            elif self._is_walkable((y+2, x)): # Down
                pos = (y+2, x)

            self.maze[y][x], self.maze[y+1][x] = ' ', ' ' # Erase portal
        elif self._is_portal((y, x+1)): # Horizontal (left-to-right)
            name = self.maze[y][x] + self.maze[y][x+1]

            # Find portal entrance
            if self._is_walkable((y, x-1)): # Left
                pos = (y, x-1)
            elif self._is_walkable((y, x+2)): # Right
                pos = (y, x+2)

            self.maze[y][x], self.maze[y][x+1] = ' ', ' ' # Erase portal

        return name, pos

    def get_min_distance(self):
        queue = deque([(self.start, 0)])
        visited = set()
        while queue:
            cur, dist = queue.popleft()

            if cur in visited: continue
            visited.add(cur)

            if cur == self.end: break

            # Inner and outer portals have the same behavior
            if cur in self.inner_portals:
                queue.append((self.inner_portals[cur], dist+1))
            elif cur in self.outer_portals:
                queue.append((self.outer_portals[cur], dist+1))
            
            for m in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                step = (cur[0]+m[0], cur[1]+m[1])
                if self._is_walkable(step):
                    queue.append((step, dist+1))

        return dist

    def get_min_distance_layers(self):
        queue = deque([(self.start, 0, 0)])
        visited = set()
        while queue:
            cur, level, dist = queue.popleft()

            if (cur, level) in visited: continue
            visited.add((cur, level))

            # End can only be reached if at level 0
            if level == 0 and cur == self.end: break

            # Outer portals decrease level and can only be accessed at level > 0
            # Inner portals increase level, can be accessed at any level
            if level > 0 and cur in self.outer_portals:
                queue.append((self.outer_portals[cur], level-1, dist+1))
            elif cur in self.inner_portals:
                queue.append((self.inner_portals[cur], level+1, dist+1))

            for m in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                step = (cur[0]+m[0], cur[1]+m[1])
                if self._is_walkable(step):
                    queue.append((step, level, dist+1))

        return dist

###########################

raw_maze = [list(s) for s in AOCUtils.load_input(20)]
maze = Maze(raw_maze)

AOCUtils.print_answer(1, maze.get_min_distance())

AOCUtils.print_answer(2, maze.get_min_distance_layers())

AOCUtils.print_time_taken()