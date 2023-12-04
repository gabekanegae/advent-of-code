###############################################
# --- Day 12: Subterranean Sustainability --- #
###############################################

import AOCUtils

GENERATIONS = 1000

###############################################

pots_and_rules = AOCUtils.load_input(12)

initial_plants = set(i for i, c in enumerate(pots_and_rules[0].split()[2]) if c == '#')

rules = dict()
for raw_rule in pots_and_rules[2:]:
    rule = raw_rule.split()
    rules[rule[0]] = rule[2]

generations = []
cur = initial_plants

for i in range(GENERATIONS):
    generations.append(cur)
    min_plant, max_plant = min(cur), max(cur)

    # print(''.join('#' if i in cur else '.' for i in range(min_plant, max_plant+1)))

    nxt = set()
    for i in range(min_plant-2, max_plant+2+1):
        rule = ''.join('#' if i+delta in cur else '.' for delta in range(-2, 2+1))
        if rules[rule] == '#':
            nxt.add(i)

    cur = nxt

target = 20

AOCUtils.print_answer(1, sum(generations[target]))

target = 50000000000

# Iterate until it converges, extrapolate from there
delta = sum(generations[1]) - sum(generations[0])
for i in range(2, GENERATIONS-1):
    new_delta = sum(generations[i]) - sum(generations[i-1])
    if delta == new_delta:
        AOCUtils.print_answer(2, sum(generations[i]) + delta*(target-i))
        break
    else:
        delta = new_delta

AOCUtils.print_time_taken()