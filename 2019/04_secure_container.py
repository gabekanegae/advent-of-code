###################################
# --- Day 4: Secure Container --- #
###################################

import AOCUtils

###################################

password_range = [int(i) for i in AOCUtils.load_input(4).split('-')]

passwords_1 = set()
for pw in range(password_range[0], password_range[1]+1):
    has_repeat, never_decreases = False, True
    pw = str(pw)

    for i in range(len(pw)-1):
        if pw[i+1] < pw[i]:
            never_decreases = False
            break
        if pw[i+1] == pw[i]:
            has_repeat = True

    if has_repeat and never_decreases:
        passwords_1.add(pw)

AOCUtils.print_answer(1, len(passwords_1))

passwords_2 = set()
for pw in passwords_1:
    sequences = [1]

    for i in range(len(pw)-1):
        if pw[i+1] == pw[i]:
            sequences[-1] += 1
        else:
            sequences.append(1)

    if 2 in sequences:
        passwords_2.add(pw)

AOCUtils.print_answer(2, len(passwords_2))

AOCUtils.print_time_taken()