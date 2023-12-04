##################################
# --- Day 6: Binary Boarding --- #
##################################

import AOCUtils

##################################

raw_answers = AOCUtils.load_input(6)

for i in range(len(raw_answers)):
    if raw_answers[i] == '':
        raw_answers[i] = '\n'

raw_groups = ' '.join(raw_answers).split('\n')

groups = [list(map(set, g.split())) for g in raw_groups]

p1 = sum(len(set.union(*group)) for group in groups)
AOCUtils.print_answer(1, p1)

p2 = sum(len(set.intersection(*group)) for group in groups)
AOCUtils.print_answer(2, p2)

AOCUtils.print_time_taken()