##############################################
# --- Day 18: Many-Worlds Interpretation --- #
##############################################

import AOCUtils
from collections import deque

class Tunnels:
    def __init__(self, tunnels):
        self.tunnels = tunnels
        self.size = (len(tunnels), len(tunnels[0]))
        self.bots = []
        self.keys = dict()
        
        for x in range(len(tunnels)):
            for y in range(len(tunnels[0])):
                if tunnels[x][y] == '@':
                    self.keys[len(self.bots)] = (x, y)
                    self.bots.append((x, y))
                elif self._is_keys(tunnels[x][y]):
                    self.keys[tunnels[x][y]] = (x, y)

        self.keys_to_keys = self._get_keys_to_keys_distance()

    def _is_door(self, tile): return 'A' <= tile <= 'Z'
    def _is_keys(self, tile): return 'a' <= tile <= 'z'

    def _get_keys_to_keys_distance(self):
        # Dict of dicts with (distance from key_a to key_b, doors inbetween)
        keys_to_keys = {k: dict() for k in self.keys}
        
        # For each key, BFS to find all the others
        for key_a, pos_key_a in self.keys.items():
            queue = deque([(pos_key_a, 0, [])])
            visited = set()

            while queue:
                cur, dist, doors = queue.popleft()
                cur_tile = self.tunnels[cur[0]][cur[1]]

                if cur in visited: continue
                visited.add(cur)

                new_doors = doors[:]
                if self._is_door(cur_tile):
                    new_doors.append(cur_tile)

                key_b = cur_tile
                if key_b != key_a and self._is_keys(key_b):
                    keys_to_keys[key_a][key_b] = (dist, new_doors)
                    keys_to_keys[key_b][key_a] = (dist, new_doors)

                for m in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                    step = (cur[0]+m[0], cur[1]+m[1])
                    if self.tunnels[step[0]][step[1]] != '#':
                        queue.append((step, dist+1, new_doors))

        return keys_to_keys

    def distance_to_all_keys(self):
        memo = dict() # Memoization of distance_to_all_keys given (bots, inventory)

        def explore_recursive(bots, inventory):
            memo_key = (tuple(sorted(bots)), tuple(sorted(inventory)))
            if memo_key in memo: return memo[memo_key]

            # Calculate all distances to all reachable keys
            distances = []
            for bot_id, bot_pos in enumerate(bots):
                bot_title = self.tunnels[bot_pos[0]][bot_pos[1]]
                if bot_title == '@': bot_title = bot_id # Not on a key, but at starting position

                for key, (dist, doors) in self.keys_to_keys[bot_title].items():
                    # If not a key but a bot, ignore it
                    if type(key) is int: continue

                    # If key is already taken, ignore it
                    if key in inventory: continue

                    # If there are locked doors between bot and key, it can't be reached
                    if not set(d.lower() for d in doors).issubset(inventory): continue

                    # Move bot to key
                    new_bots = bots[:]
                    new_bots[bot_id] = self.keys[key]

                    # Add key to inventory
                    new_inventory = inventory | set(key)

                    # Add to possible paths (recurse)
                    distances.append(dist + explore_recursive(new_bots, new_inventory))

            # If no keys are reachable, min_distance is 0
            min_distance = min(distances) if distances else 0

            memo[memo_key] = min_distance
            return min_distance

        return explore_recursive(self.bots, set())

    # def __repr__(self):
    #     s = ''
    #     for line in self.tunnels:
    #         s += ''.join(line) + '\n'
    #     return s

##############################################

raw_tunnels = [list(s) for s in AOCUtils.load_input(18)]

tunnels = Tunnels(raw_tunnels)
AOCUtils.print_answer(1, tunnels.distance_to_all_keys())

# Modify map center according to instructions
pos = tunnels.bots[0]
for w in [(-1, 0), (0, 0), (1, 0), (0, -1), (0, 1)]:
    raw_tunnels[pos[0]+w[0]][pos[1]+w[1]] = '#'
for b in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
    raw_tunnels[pos[0]+b[0]][pos[1]+b[1]] = '@'

tunnels = Tunnels(raw_tunnels)
AOCUtils.print_answer(2, tunnels.distance_to_all_keys())

AOCUtils.print_time_taken()