############################
# --- Day 16: Aunt Sue --- #
############################

import AOCUtils

############################

rawAunts = AOCUtils.loadInput(16)

aunts = dict()
for rawAunt in rawAunts:
    rawAunt = rawAunt.split()

    auntID = int(rawAunt[1][:-1])
    aunt = dict()
    for i in range(2, len(rawAunt), 2):
        thing = rawAunt[i].rstrip(":")
        amount = int(rawAunt[i+1].rstrip(","))
        aunt[thing] = amount

    aunts[auntID] = aunt

tape = {"children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
        }

for aunt, things in aunts.items():
    for thing, amount in things.items():
        if amount != tape[thing]:
            break
    else:
        print("Part 1: {}".format(aunt))
        break

for aunt, things in aunts.items():
    for thing, amount in things.items():
        if thing in ["cats", "trees"]:
            if amount <= tape[thing]:
                break
        elif thing in ["pomeranians", "goldfish"]:
            if amount >= tape[thing]:
                break
        elif amount != tape[thing]:
            break
    else:
        print("Part 2: {}".format(aunt))
        break

AOCUtils.printTimeTaken()