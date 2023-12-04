########################################################
# --- Day 23: Experimental Emergency Teleportation --- #
########################################################

import AOCUtils
from heapq import heappush, heappop

class Bot:
    def __init__(self, pos, r):
        self.pos = pos
        self.r = r

    def distance_to(self, other):
        return sum(abs(a-b) for a, b in zip(self.pos, other.pos))

class Box:
    def __init__(self, low, high):
        self.low, self.high = low, high

    def is_in_range_of(self, bot):
        dist = 0
        for box_low, b, box_high in zip(self.low, bot.pos, self.high):
            box_high -= 1
            dist += abs(b - box_low) + abs(b - box_high) - (box_high - box_low)

        return dist // 2 <= bot.r

    def bots_in_range(self, bots):
        return sum(map(self.is_in_range_of, bots))
    
    def origin_distance(self):
        return sum(map(abs, self.low))

    def __lt__(self, other):
        return (self.low, self.high) < (other.low, other.high)

########################################################

raw_data = AOCUtils.load_input(23)
raw_data = [s[5:].split('>, r=') for s in raw_data]

positions = [tuple(map(int, s[0].split(','))) for s in raw_data]
radii = [int(i[1]) for i in raw_data]

bots = [Bot(p, r) for p, r in zip(positions, radii)]

# Sort by largest radius, take first
bots.sort(key=lambda x: x.r, reverse=True)
strongest_bot = bots[0]

bots_in_range = sum(strongest_bot.distance_to(bot) < strongest_bot.r for bot in bots)
AOCUtils.print_answer(1, bots_in_range)

# Create a bounding box big enough for all bots and its ranges
max_coord = max(max(abs(i)+b.r for i in b.pos) for b in bots)
bounding_box = Box((-max_coord, -max_coord, -max_coord), (max_coord, max_coord, max_coord))
bounding_box_size = 2*max_coord

# Create heap ordered by: most bots in range, biggest size, least distance to origin
heap = [(-len(bots), -bounding_box_size, bounding_box.origin_distance(), bounding_box)]
while len(heap) > 0:
    _, size, origin_distance, box = heappop(heap)

    if abs(size) == 1: # Box is 1x1x1 = single point
        AOCUtils.print_answer(2, origin_distance)
        break

    # Break in 8 octants
    octSize = abs(size//2)
    for octant in [(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)]:
        oct_low = ([box_low + octSize*oct_coord for box_low, oct_coord in zip(box.low, octant)])
        oct_high = (oct_low[0]+octSize, oct_low[1]+octSize, oct_low[2]+octSize)
        box_oct = Box(oct_low, oct_high)

        # Calculate bots in octant range and add to heap
        bots_in_range = box_oct.bots_in_range(bots)
        heappush(heap, (-bots_in_range, -octSize, box_oct.origin_distance(), box_oct))

AOCUtils.print_time_taken()