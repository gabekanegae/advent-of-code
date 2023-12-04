###############################
# --- Day 4: Camp Cleanup --- #
###############################

import AOCUtils

###############################

raw_assignments = AOCUtils.load_input(4)
assignments = [[list(map(int, p.split('-'))) for p in l.split(',')] for l in raw_assignments]

fully_contained = 0
for (a_s, a_e), (b_s, b_e) in assignments:
    fully_contained += int(a_s <= b_s <= b_e <= a_e or b_s <= a_s <= a_e <= b_e)

AOCUtils.print_answer(1, fully_contained)

overlaps = 0
for (a_s, a_e), (b_s, b_e) in assignments:
    overlaps += int(b_s <= a_s <= b_e or b_s <= a_e <= b_e or a_s <= b_s <= a_e or a_s <= b_e <= a_e)

AOCUtils.print_answer(2, overlaps)

AOCUtils.print_time_taken()