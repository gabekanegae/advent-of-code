##################################
# --- Day 20: Firewall Rules --- #
##################################

import AOCUtils

##################################

rawRules = AOCUtils.loadInput(20)

rules = [tuple(map(int, rawRule.split("-"))) for rawRule in rawRules]

ip = 0
while ip < 2**32:
    blocked = False
    for ruleStart, ruleEnd in rules:
        if ruleStart <= ip <= ruleEnd:
            ip = ruleEnd

            blocked = True
            break

    if not blocked:
        break

    ip += 1

print("Part 1: {}".format(ip))

total = 0
ip = 0
while ip < 2**32:
    blocked = False
    for ruleStart, ruleEnd in rules:
        if ruleStart <= ip <= ruleEnd:
            ip = ruleEnd

            blocked = True
            break

    if not blocked:
        total += 1

    ip += 1

print("Part 2: {}".format(total))

AOCUtils.printTimeTaken()