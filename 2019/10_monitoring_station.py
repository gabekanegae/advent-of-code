######################################
# --- Day 10: Monitoring Station --- #
######################################

import AOCUtils
import math

def count_in_los(station, asteroids, size):
    detected = set()
    for asteroid in asteroids:
        if asteroid != station:
            dx, dy = asteroid[0]-station[0], asteroid[1]-station[1]

            # Divide by gcd to determine direction from origin,
            # reducing all colinear asteroids to one
            g = abs(math.gcd(dx, dy))
            reduced = (dx//g, dy//g)
            detected.add(reduced)

    return detected

######################################

raw_asteroids = AOCUtils.load_input(10)
size = (len(raw_asteroids), len(raw_asteroids[0]))

asteroids = set()
for x in range(size[0]):
    for y in range(size[1]):
        if raw_asteroids[x][y] == '#':
            asteroids.add((x, y))

# Count asteroids in line of sight for all possible station positions
station_counts = []
for station in asteroids:
    in_los = count_in_los(station, asteroids, size)
    station_counts.append((len(in_los), station, in_los))

# Sort by most asteroids in line of sight and get first
station_counts.sort(reverse=True)
amount_in_los, station, in_los = station_counts[0]

AOCUtils.print_answer(1, amount_in_los)

n = 200

# Sort by atan2 of swapped coordinates
# (starts pointing up and rotates cw, instead of pointing right and rotating ccw)
destroyed = [(math.atan2(dy, dx), (dx, dy)) for dx, dy in in_los]
destroyed.sort(reverse=True)

# Assumes nth asteroid can be destroyed in a single full rotation
dx, dy = destroyed[n-1][1]

x, y = station[0]+dx, station[1]+dy
while (x, y) not in asteroids:
    x, y = x+dx, y+dy

AOCUtils.print_answer(2, y*100 + x)

AOCUtils.print_time_taken()