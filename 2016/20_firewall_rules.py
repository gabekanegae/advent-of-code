##################################
# --- Day 20: Firewall Rules --- #
##################################

import AOCUtils

##################################

rawRules = AOCUtils.loadInput(20)

rules = [tuple(map(int, rawRule.split("-"))) for rawRule in rawRules]

p1done = False
total = 0

ip = 0
while ip < 2**32:
    for ruleStart, ruleEnd in rules:
        if ruleStart <= ip <= ruleEnd:
            ip = ruleEnd
            break
    else:
        total += 1
        if not p1done:
            print("Part 1: {}".format(ip))
            p1done = True

    ip += 1

print("Part 2: {}".format(total))

AOCUtils.printTimeTaken()