#################################
# --- Day 6: Tuning Trouble --- #
#################################

import AOCUtils

def find_marker(datastream, n):
    i, j = 0, n-1
    
    while j < len(datastream):
        if len(set(datastream[i:j+1])) == n:
            return j+1
        i += 1
        j += 1

    return None

#################################

datastream = AOCUtils.load_input(6)

AOCUtils.print_answer(1, find_marker(datastream, 4))

AOCUtils.print_answer(2, find_marker(datastream, 14))

AOCUtils.print_time_taken()