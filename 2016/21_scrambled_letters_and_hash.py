##############################################
# --- Day 21: Scrambled Letters and Hash --- #
##############################################

import AOCUtils

def scramble(password, steps):
    password = list(password)

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
                c = password.index(step[-1])
                n = c + 1 + int(c >= 4)
            else:
                n = int(step[2])
                if step[1] == "left": n *= -1

            n %= len(password)
            password = password[-n:] + password[:-n] # Rotate right
        elif step[0] == "swap":
            if step[1] == "letter":
                a, b = password.index(step[2]), password.index(step[5])
            elif step[1] == "position":
                a, b = int(step[2]), int(step[5])

            password[a], password[b] = password[b], password[a]

    return "".join(password)

def unscramble(password, steps):
    password = list(password)

    for step in reversed(steps):
        step = step.split()
        if step[0] == "move":
            b, a = int(step[2]), int(step[5])
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

                # Rotate 1 left until c is at position i
                # At the 4th rotation, rotate twice
                i = 0
                while True:
                    n = 1 + int(i == 4)
                    password = password[n:] + password[:n] # Rotate left
                    if password[i] == c:
                        break
                    i += 1
            else:
                n = int(step[2])
                if step[1] == "left": n *= -1

                n %= len(password)
                password = password[n:] + password[:n] # Rotate left
        elif step[0] == "swap":
            if step[1] == "letter":
                a, b = password.index(step[2]), password.index(step[5])
            elif step[1] == "position":
                a, b = int(step[2]), int(step[5])

            password[a], password[b] = password[b], password[a]

    return "".join(password)

##############################################

steps = AOCUtils.loadInput(21)

print("Part 1: {}".format(scramble("abcdefgh", steps)))

print("Part 2: {}".format(unscramble("fbgdceah", steps)))

AOCUtils.printTimeTaken()