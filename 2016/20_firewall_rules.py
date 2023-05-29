##################################
# --- Day 20: Firewall Rules --- #
##################################

import AOCUtils

##################################

rules = [tuple(map(int, r.split('-'))) for r in AOCUtils.load_input(20)]

p1_done = False
total = 0

ip = 0
while ip < 2**32:
    for rule_start, rule_end in rules:
        if rule_start <= ip <= rule_end:
            ip = rule_end
            break
    else:
        total += 1
        if not p1_done:
            AOCUtils.print_answer(1, ip)
            p1_done = True

    ip += 1

AOCUtils.print_answer(2, total)

AOCUtils.print_time_taken()