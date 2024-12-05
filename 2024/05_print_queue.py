##############################
# --- Day 4: Print Queue --- #
##############################

import AOCUtils
from functools import cmp_to_key
import math

##############################

raw_rules_and_updates = AOCUtils.load_input(5)

rules_and_updates = [s.splitlines() for s in '\n'.join(raw_rules_and_updates).split('\n\n')]
rules = [tuple(map(int, l.split('|'))) for l in rules_and_updates[0]]
updates = [list(map(int, l.split(','))) for l in rules_and_updates[1]]

pages = {i for rule in rules for i in rule}

# Solution assumes graph is complete
assert(len(rules) == math.comb(len(pages), 2))

dependencies = {page: [] for page in pages}
for before, after in rules:
    dependencies[after].append(before)

cmp_dependency = lambda a, b: 1 if a not in dependencies[b] else -1
sorted_updates = [sorted(update, key=cmp_to_key(cmp_dependency)) for update in updates]

valid_updates = []
fixed_invalid_updates = []
for update, sorted_update in zip(updates, sorted_updates):
    if update == sorted_update:
        valid_updates.append(update)
    else:
        fixed_invalid_updates.append(sorted_update)

middle_page_valid_updates = sum(update[len(update)//2] for update in valid_updates)
AOCUtils.print_answer(1, middle_page_valid_updates)

middle_page_fixed_invalid_updates = sum(update[len(update)//2] for update in fixed_invalid_updates)
AOCUtils.print_answer(2, middle_page_fixed_invalid_updates)

AOCUtils.print_time_taken()
