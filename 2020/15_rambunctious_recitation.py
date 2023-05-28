###########################################
# --- Day 15: Rambunctious Recitation --- #
###########################################

import AOCUtils

def memoryGame(start, n):
    seen = dict()
    last = None

    for i in range(n):
        if i < len(start):
            speak = start[i]
        elif len(seen[last]) < 2:
            speak = 0
        else:
            speak = seen[last][-1] - seen[last][-2]

        if speak not in seen:
            seen[speak] = []
        seen[speak].append(i)
        last = speak

    return speak

###########################################

start = AOCUtils.load_input(15)

start = [int(i) for i in start.split(',')]

AOCUtils.print_answer(1, memoryGame(start, 2020))

AOCUtils.print_answer(2, memoryGame(start, 30000000))

AOCUtils.print_time_taken()