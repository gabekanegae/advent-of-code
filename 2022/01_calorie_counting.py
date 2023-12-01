###################################
# --- Day 1: Calorie Counting --- #
###################################

import AOCUtils

###################################

calories = AOCUtils.load_input(1)

total_calories_per_elf = [sum(map(int, l.split())) for l in '\n'.join(calories).split('\n\n')]

max_calories = max(total_calories_per_elf)
AOCUtils.print_answer(1, max_calories)

sum_top_3_elves = sum(sorted(total_calories_per_elf, reverse=True)[:3])
AOCUtils.print_answer(2, sum_top_3_elves)

AOCUtils.print_time_taken()