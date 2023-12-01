####################################
# --- Day 10: Cathode-Ray Tube --- #
####################################

import AOCUtils

def get_signal_strength(x_deltas, cycle):
    x = 1 + sum(delta for c, delta in x_deltas.items() if c < cycle)

    return x * cycle

def get_lines(x_deltas, w, h):
    cycle, x = 1, 1

    lit_pixels = set()
    for cycle in range(w * h):
        if cycle in x_deltas:
            x += x_deltas[cycle]

        p_x, p_y = cycle % w, cycle // w
        if abs(x - p_x) <= 1:
            lit_pixels.add((p_x, p_y))

    image = [[(x, y) in lit_pixels for x in range(w)] for y in range(h)]
    return image

####################################

program = AOCUtils.load_input(10)

x_deltas = dict()
cycle = 0
for inst in program:
    if inst == 'noop':
        cycle += 1
    else:
        cycle += 2
        x_deltas[cycle] = int(inst.split()[1])

result = sum(get_signal_strength(x_deltas, cycle) for cycle in range(20, 220+1, 40))
AOCUtils.print_answer(1, result)

image = get_lines(x_deltas, 40, 6)
AOCUtils.print_answer(2, image)

AOCUtils.print_time_taken()