##############################################
# --- Day 2: Inventory Management System --- #
##############################################

import AOCUtils

def getFreq(l):
    freq = dict()
    for e in l:
        freq[e] = freq.get(e, 0) + 1

    return freq

##############################################

boxes = AOCUtils.loadInput(2)

boxes2, boxes3 = 0, 0
for box in boxes:
    counts = set(getFreq(box).values())
    if 2 in counts:
        boxes2 += 1
    if 3 in counts:
        boxes3 += 1

print("Part 1: {}".format(boxes2 * boxes3))

end = False
for boxi in boxes:
    if end: break

    for boxj in boxes:
        if sum(ic != jc for ic, jc in zip(boxi, boxj)) == 1:
            same = ""
            for ic, jc in zip(boxi, boxj):
                if ic == jc:
                    same += ic

            print("Part 2: {}".format(same))
            end = True
            break

AOCUtils.printTimeTaken()