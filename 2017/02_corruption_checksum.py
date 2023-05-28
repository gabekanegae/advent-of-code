######################################
# --- Day 2: Corruption Checksum --- #
######################################

import AOCUtils

######################################

spreadsheet = [[int(i) for i in s.split()] for s in AOCUtils.load_input(2)]

checksum = sum(max(s) - min(s) for s in spreadsheet)
AOCUtils.print_answer(1, checksum)

checksum = 0
for s in spreadsheet:
    for i in range(len(s)):
        for j in range(len(s)):
            if i != j and s[i] % s[j] == 0:
                checksum += s[i] // s[j]

AOCUtils.print_answer(2, checksum)

AOCUtils.print_time_taken()