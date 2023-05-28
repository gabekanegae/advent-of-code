#########################################
# --- Day 10: Elves Look, Elves Say --- #
#########################################

import AOCUtils

def look_and_say(s):
    out = []

    last = s[0]
    count = 1
    for c in s[1:]:
        if c == last:
            count += 1
        else:
            out.append(str(count))
            out.append(last)

            count = 1
            last = c

    out.append(str(count))
    out.append(last)

    return out

#########################################

sequence = str(AOCUtils.load_input(10))

for _ in range(40):
    sequence = look_and_say(sequence)

AOCUtils.print_answer(1, len(sequence))

sequence = str(AOCUtils.load_input(10))

for _ in range(50):
    sequence = look_and_say(sequence)

AOCUtils.print_answer(2, len(sequence))

AOCUtils.print_time_taken()