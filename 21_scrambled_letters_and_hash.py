##############################################
# --- Day 21: Scrambled Letters and Hash --- #
##############################################

import AOCUtils
from itertools import permutations

def encode(password, steps):
    password = list(password)
    pwdLen = len(password)

    for step in steps:
        step = step.split()
        if step[0] == "move":
            a, b = int(step[2]), int(step[5])
            c = password[a]
            if b > a:
                password[a:b] = password[a+1:b+1]
            else:
                password[b+1:a+1] = password[b:a]
            password[b] = c
        elif step[0] == "reverse":
            a, b = int(step[2]), int(step[4])

            password[a:b+1] = reversed(password[a:b+1])
        elif step[0] == "rotate":
            if step[1] == "based":
                c = step[-1]
                n = password.index(c)
                n += 1 + int(n >= 4)
            else:
                n = int(step[2])
                if step[1] == "left":
                    n *= -1
                elif step[1] == "right":
                    pass

            n %= pwdLen
            password = password[-n:] + password[:-n]
        elif step[0] == "swap":
            if step[1] == "letter":
                ca, cb = step[2], step[5]
                a, b = password.index(ca), password.index(cb)
            elif step[1] == "position":
                a, b = int(step[2]), int(step[5])

            password[a], password[b] = password[b], password[a]

    return "".join(password)

##############################################

steps = AOCUtils.loadInput(21)

print("Part 1: {}".format(encode("abcdefgh", steps)))

for password in permutations("abcdefgh"):
    if encode(password, steps) == "fbgdceah":
        break

print("Part 2: {}".format("".join(password)))