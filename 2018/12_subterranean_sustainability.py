###############################################
# --- Day 12: Subterranean Sustainability --- #
###############################################

import AOCUtils

MARGIN = 100
GENAMT = 200

def get_sum_pots(gen):
    return sum(i-MARGIN for i in range(len(gen)) if gen[i] == '#')

###############################################

pots_and_rules = AOCUtils.load_input(12)

initial = pots_and_rules[0].split()[2]
rules = dict()
for rule in pots_and_rules[2:]:
    r = rule.split()
    rules[r[0]] = r[2]

generations = []
cur = '.'*MARGIN + initial + '.'*MARGIN
generations.append(cur)

genLen = len(cur)
for i in range(GENAMT):
    nxt = ['.' for _ in range(genLen)]
    for i in range(2, genLen-2):
        nxt[i] = rules[cur[i-2:i+3]]
    generations.append(nxt)
    cur = ''.join(nxt)

sum_pots = [get_sum_pots(generations[i]) for i in range(GENAMT)]

AOCUtils.print_answer(1, sum_pots[20])

delta = sum_pots[1] - sum_pots[0]
for i in range(2, GENAMT-1):
    new_delta = sum_pots[i] - sum_pots[i-1]
    if delta == new_delta:
        AOCUtils.print_answer(2, sum_pots[i] + delta*(50000000000-i))
        break
    else:
        delta = new_delta

AOCUtils.print_time_taken()