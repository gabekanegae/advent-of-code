######################################
# --- Day 2: Corruption Checksum --- #
######################################

import AOCUtils

######################################

raw_spreadsheet = AOCUtils.load_input(2)
spreadsheet = [list(map(int, s.split())) for s in raw_spreadsheet]

checksum = sum(max(s) - min(s) for s in spreadsheet)
AOCUtils.print_answer(1, checksum)

checksum = 0
for s in spreadsheet:
    for i, s_i in enumerate(s):
        for j, s_j in enumerate(s):
            if i != j and s_i % s_j == 0:
                checksum += s_i // s_j

AOCUtils.print_answer(2, checksum)

AOCUtils.print_time_taken()