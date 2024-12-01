#####################################
# --- Day 1: Historian Hysteria --- #
#####################################

import AOCUtils

raw_lists = AOCUtils.load_input(1)

left, right = zip(*[map(int, l.split()) for l in raw_lists])

total_distance = sum(abs(a-b) for a, b in zip(sorted(left), sorted(right)))
AOCUtils.print_answer(1, total_distance)

similarity_score = sum(i * right.count(i) for i in left)
AOCUtils.print_answer(2, similarity_score)

AOCUtils.print_time_taken()
