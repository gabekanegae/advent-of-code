######################################
# --- Day 14: Regolith Reservoir --- #
######################################

import AOCUtils

sand_source = (500, 0)

# Down, Down-Left, Down-Right
sand_deltas = [(0, 1), (-1, 1), (1, 1)]

def simulate(rock, part):
    max_y = max(y for x, y in rock)
    settled_sand = set()

    while True:
        # Drop new sand block
        sand = sand_source
        while True:
            # Simulate one step
            for delta in sand_deltas:
                nxt_sand = (sand[0]+delta[0], sand[1]+delta[1])
                if nxt_sand not in rock and nxt_sand not in settled_sand:
                    sand = nxt_sand
                    break
            else: # Settled
                break

            if part == 1 and sand[1] > max_y: return settled_sand
            if part == 2 and sand[1] == max_y+1: break

        settled_sand.add(sand)
        if part == 2 and sand == sand_source: return settled_sand

def print_scan(rock, settled_sand):
    blocks = rock | settled_sand | set([sand_source])
    min_x, max_x = min(x for x, y in blocks), max(x for x, y in blocks)
    min_y, max_y = min(y for x, y in blocks), max(y for x, y in blocks)
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x, y) in rock: c = '#'
            elif (x, y) in settled_sand: c = 'o'
            elif (x, y) == sand_source: c = '+'
            else: c = ' '
            print(end=c*2)
        print()

######################################

raw_rock_lines = AOCUtils.load_input(14)

rock_lines = [[tuple(map(int, p.split(','))) for p in l.split(' -> ')] for l in raw_rock_lines]

rock = set()
for line in rock_lines:
    for a, b in zip(line, line[1:]):
        if a[0] == b[0] and a[1] < b[1]:
            delta = (0, 1)
        elif a[0] == b[0] and a[1] > b[1]:
            delta = (0, -1)
        elif a[0] < b[0] and a[1] == b[1]:
            delta = (1, 0)
        elif a[0] > b[0] and a[1] == b[1]:
            delta = (-1, 0)

        rock.add(a)
        while a != b:
            a = (a[0]+delta[0], a[1]+delta[1])
            rock.add(a)

settled_sand = simulate(rock, 1)
# print_scan(rock, settled_sand)
AOCUtils.print_answer(1, len(settled_sand))

settled_sand = simulate(rock, 2)
# print_scan(rock, settled_sand)
AOCUtils.print_answer(2, len(settled_sand))

AOCUtils.print_time_taken()