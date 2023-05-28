############################
# --- Day 16: Aunt Sue --- #
############################

import AOCUtils

############################

raw_aunts = AOCUtils.load_input(16)

aunts = dict()
for raw_aunt in raw_aunts:
    raw_aunt = raw_aunt.split()

    aunt_id = int(raw_aunt[1][:-1])
    aunt = dict()
    for i in range(2, len(raw_aunt), 2):
        thing = raw_aunt[i].rstrip(':')
        amount = int(raw_aunt[i+1].rstrip(','))
        aunt[thing] = amount

    aunts[aunt_id] = aunt

tape = {'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
        }

for aunt, things in aunts.items():
    for thing, amount in things.items():
        if amount != tape[thing]:
            break
    else:
        AOCUtils.print_answer(1, aunt)
        break

for aunt, things in aunts.items():
    for thing, amount in things.items():
        if thing in ['cats', 'trees']:
            if amount <= tape[thing]:
                break
        elif thing in ['pomeranians', 'goldfish']:
            if amount >= tape[thing]:
                break
        elif amount != tape[thing]:
            break
    else:
        AOCUtils.print_answer(2, aunt)
        break

AOCUtils.print_time_taken()