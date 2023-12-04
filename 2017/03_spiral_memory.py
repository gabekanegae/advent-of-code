################################
# --- Day 3: Spiral Memory --- #
################################

import AOCUtils

################################

square = AOCUtils.load_input(3)

p1, p2 = None, None

x, y = 0, 0
edge_count = 0
seen = {(0, 0): 1}

while not (p1 and p2):
    loop_start = True

    for _ in range((edge_count//4 + 1) * 2):
        if edge_count % 4 == 0:
            if loop_start: # >
                x += 1
                loop_start = False
            else:
                y -= 1 # ^
        elif edge_count % 4 == 1: # <
            x -= 1
        elif edge_count % 4 == 2: # v
            y += 1
        elif edge_count % 4 == 3: # >
            x += 1
        
        if p2:
            seen[(x, y)] = 0
        else:
            seen[(x, y)] = sum(seen[(x+dx, y+dy)] for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (x+dx, y+dy) in seen)

        if not p1 and len(seen) == square:
            p1 = abs(x) + abs(y)
        if not p2 and seen[(x, y)] > square:
            p2 = seen[(x, y)]
        if p1 and p2:
            break

    edge_count += 1

AOCUtils.print_answer(1, p1)

AOCUtils.print_answer(2, p2)

AOCUtils.print_time_taken()