##########################################################
# --- Day 11: Radioisotope Thermoelectric Generators --- #
##########################################################

import AOCUtils
from collections import deque

def assemble(floors, floor_amount):
    items = dict()
    for i, floor in enumerate(floors):
        for item in floor:
            mat, obj = item.split()
            mat = mat.split('-')[0]
            obj = 'MG'.index(obj[0].upper())

            if mat not in items:
                items[mat] = [None, None]
            items[mat][obj] = i

    visited = set()

    start = (0, tuple(sorted(tuple(items[mat]) for mat in items)))
    queue = deque([(start, 0)])
    while queue:
        cur_state, dist = queue.popleft()

        if cur_state in visited: continue
        visited.add(cur_state)

        cur_floor, cur_items = cur_state

        # All items are at the last floor
        if all(item == (floor_amount-1, floor_amount-1) for item in cur_items):
            return dist

        ms = [mat[0] for mat in cur_items]
        gs = [mat[1] for mat in cur_items]

        # Check if any chips are fried
        fried = False
        for i, m in enumerate(ms):
            if fried: break
            for j, g in enumerate(gs):
                if i == j: continue
                # If a chip is in the same area as another RTG,
                # and it's not connected to its own RTG.
                if m == g and gs[i] != m:
                    fried = True
                    break
        if fried: continue
    
        single_picks = [i for i, f in enumerate(ms + gs) if f == cur_floor]
        double_picks = list(set(tuple(sorted((i, j))) for i in single_picks for j in single_picks if i != j))
        single_picks = [(i,) for i in single_picks]

        n = len(items)
        for move in [1, -1]:
            if move == 1: # If going up, take two items when possible
                picks = double_picks or single_picks
            else: # If going down, take one item when possible
                picks = single_picks or double_picks

            nxt_floor = cur_floor + move
            if not 0 <= nxt_floor < floor_amount: continue

            for pick in picks:
                nxt_items = [list(mat) for mat in cur_items]
                for i in pick: nxt_items[i%n][i//n] += move
                
                nxt_state = (nxt_floor, tuple(sorted(tuple(i) for i in nxt_items)))
                queue.append((nxt_state, dist+1))

    return None

##########################################################

raw_floors = AOCUtils.load_input(11)

floors_1 = []
for raw_floor in raw_floors:
    if 'nothing relevant' in raw_floor:
        floor = []
    else:
        floor = ' '.join(raw_floor[:-1].split()[4:])
        floor = [f.split('and') for f in floor.split(',')]
        floor = [item.strip() for f in floor for item in f if item.strip()]
        floor = [' '.join(f.split()[1:]) for f in floor]

    floors_1.append(floor)

AOCUtils.print_answer(1, assemble(floors_1, 4))

floors_2 = [f[:] for f in floors_1]
floors_2[0] += ['elerium generator',
               'elerium-compatible microchip',
               'dilithium generator',
               'dilithium-compatible microchip']

AOCUtils.print_answer(2, assemble(floors_2, 4))

AOCUtils.print_time_taken()