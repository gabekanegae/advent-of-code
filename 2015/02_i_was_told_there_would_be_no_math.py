####################################################
# --- Day 2: I Was Told There Would Be No Math --- #
####################################################

import AOCUtils

####################################################

presents = AOCUtils.loadInput(2)

presents = [tuple(map(int, present.split("x"))) for present in presents]

totalPaper = 0
for present in presents:
    l, w, h = present

    paper = 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    totalPaper += paper

print("Part 1: {}".format(totalPaper))

totalRibbon = 0
for present in presents:
    l, w, h = present

    ribbon = 2 * min(l+w, w+h, h+l) + l*w*h
    totalRibbon += ribbon

print("Part 2: {}".format(totalRibbon))

AOCUtils.printTimeTaken()