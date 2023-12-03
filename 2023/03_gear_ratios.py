##############################
# --- Day 3: Gear Ratios --- #
##############################

from collections import defaultdict
import AOCUtils

mov_8 = {(-1, -1), (-1, 0), (-1, 1),
         ( 0, -1),          ( 0, 1),
         ( 1, -1), ( 1, 0), ( 1, 1)}

##############################

schematic = AOCUtils.load_input(3)

height, width = len(schematic), len(schematic[0])
symbols = set(c for l in schematic for c in l if not c.isnumeric() and c != '.')

numbers = []
for row in range(height):
    i = 0
    while i < width:
        if schematic[row][i].isnumeric():
            j = i + 1
            while j < width and schematic[row][j].isnumeric():
                j += 1
            numbers.append(((row, i, j), int(schematic[row][i:j])))
            i = j
        i += 1

part_numbers = set()
for (row, i, j), number in numbers:
    is_part_number = False
    for col in range(i, j):
        for (dr, dc) in mov_8:
            pos = (row+dr, col+dc)
            if 0 <= pos[0] < height and 0 <= pos[1] < width and schematic[pos[0]][pos[1]] in symbols:
                is_part_number = True
                break
        
        if is_part_number:
            part_numbers.add((pos, number))
            break

AOCUtils.print_answer(1, sum(number for pos, number in part_numbers))

gears = defaultdict(list)
for pos, number in part_numbers:
    if schematic[pos[0]][pos[1]] == '*':
        gears[pos].append(number)

AOCUtils.print_answer(2, sum(parts[0] * parts[1] for parts in gears.values() if len(parts) == 2))

AOCUtils.print_time_taken()
