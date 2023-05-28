######################################
# --- Day 2: Password Philosophy --- #
######################################

import AOCUtils

######################################

raw_passwords = AOCUtils.load_input(2)

p1 = 0
p2 = 0
for raw_password in raw_passwords:
    counts, c, password = raw_password.split()
    a, b = [int(i) for i in counts.split('-')]
    c = c[0]

    if a <= password.count(c) <= b:
        p1 += 1
    if (password[a-1] == c) ^ (password[b-1] == c):
        p2 += 1

AOCUtils.print_answer(1, p1)

AOCUtils.print_answer(2, p2)

AOCUtils.print_time_taken()