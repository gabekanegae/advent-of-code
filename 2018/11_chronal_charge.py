##################################
# --- Day 11: Chronal Charge --- #
##################################

import AOCUtils

def get_max_sum(m, square_size):
    max_sum, max_coords = None, None
    for x in range(square_size-1, 300):
        for y in range(square_size-1, 300):
            # 2D Partial Sum
            cur_sum = partials[x][y]
            if x-square_size >= 0: cur_sum -= partials[x-square_size][y]
            if y-square_size >= 0: cur_sum -= partials[x][y-square_size]
            if x-square_size >= 0 and y-square_size >= 0: cur_sum += partials[x-square_size][y-square_size]

            if not max_sum or cur_sum > max_sum:
                max_sum, max_coords = cur_sum, (x-(square_size-1), y-(square_size-1))
    return max_sum, max_coords

##################################

serial = AOCUtils.load_input(11)

cells = [[None for _ in range(300)] for _ in range(300)]
for x in range(300):
    for y in range(300):
        cells[x][y] = ((((x+10)*y + serial) * (x+10) // 100) % 10) - 5

partials = [[cells[x][y] for y in range(300)] for x in range(300)]
for x in range(300):
    for y in range(300):
        if x-1 >= 0: partials[x][y] += partials[x-1][y]
        if y-1 >= 0: partials[x][y] += partials[x][y-1]
        if x-1 >= 0 and y-1 >= 0: partials[x][y] -= partials[x-1][y-1]

cur_sum, cur_coords = get_max_sum(partials, 3)

AOCUtils.print_answer(1, f'{cur_coords[0]},{cur_coords[1]}')

max_sum, max_coords, max_size = None, None, None
for i in range(1, 300+1):
    cur_sum, cur_coords = get_max_sum(partials, i)
    if not max_sum or cur_sum > max_sum:
        max_sum, max_coords, max_size = cur_sum, cur_coords, i

AOCUtils.print_answer(2, f'{max_coords[0]},{max_coords[1]},{max_size}')

AOCUtils.print_time_taken()