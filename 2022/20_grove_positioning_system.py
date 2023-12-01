############################################
# --- Day 20: Grove Positioning System --- #
############################################

import AOCUtils

def mix(file, rounds):
    length = len(file)
    idxs = list(range(length))

    for _ in range(rounds):
        for i in range(length):
            old_idx = idxs.index(i)
            new_idx = (old_idx+file[i]) % (length-1)
            idxs.insert(new_idx, idxs.pop(old_idx))

    file = [file[i] for i in idxs]
    zero_idx = file.index(0)
    return sum(file[(zero_idx+i) % length] for i in [1000, 2000, 3000])

############################################

file = AOCUtils.load_input(20)

p1 = mix(file, 1)
AOCUtils.print_answer(1, p1)

p2 = mix([f*811589153 for f in file], 10)
AOCUtils.print_answer(2, p2)

AOCUtils.print_time_taken()