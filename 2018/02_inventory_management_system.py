##############################################
# --- Day 2: Inventory Management System --- #
##############################################

import AOCUtils

def get_frequency(l):
    frequency = dict()
    for e in l:
        frequency[e] = frequency.get(e, 0) + 1

    return frequency

##############################################

boxes = AOCUtils.load_input(2)

boxes_2, boxes_3 = 0, 0
for box in boxes:
    counts = set(get_frequency(box).values())
    if 2 in counts:
        boxes_2 += 1
    if 3 in counts:
        boxes_3 += 1

AOCUtils.print_answer(1, boxes_2 * boxes_3)

end = False
for box_i in boxes:
    if end: break

    for box_j in boxes:
        if sum(ic != jc for ic, jc in zip(box_i, box_j)) == 1:
            same = ''
            for ic, jc in zip(box_i, box_j):
                if ic == jc:
                    same += ic

            AOCUtils.print_answer(2, same)
            end = True
            break

AOCUtils.print_time_taken()