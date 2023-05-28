####################################################
# --- Day 2: I Was Told There Would Be No Math --- #
####################################################

import AOCUtils

####################################################

presents = AOCUtils.load_input(2)

presents = [tuple(map(int, present.split('x'))) for present in presents]

total_paper = 0
for present in presents:
    l, w, h = present

    paper = 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    total_paper += paper

AOCUtils.print_answer(1, total_paper)

total_ribbon = 0
for present in presents:
    l, w, h = present

    ribbon = 2 * min(l+w, w+h, h+l) + l*w*h
    total_ribbon += ribbon

AOCUtils.print_answer(2, total_ribbon)

AOCUtils.print_time_taken()