################################
# --- Day 15: Lens Library --- #
################################

import AOCUtils

def get_hash(s):
    cur = 0
    for c in s:
        cur += ord(c)
        cur *= 17
        cur %= 256

    return cur

################################

raw_steps = AOCUtils.load_input(15)
steps = raw_steps.split(',')

AOCUtils.print_answer(1, sum(map(get_hash, steps)))

boxes = [dict() for _ in range(256)]
for step in steps:
    if step[-1] == '-':
        label = step[:-1]

        boxes[get_hash(label)].pop(label, None)
    else:
        label, focal_length = step[:-2], int(step[-1])
        
        boxes[get_hash(label)][label] = focal_length

total_focusing_power = 0
for box_i, box in enumerate(boxes):
    for lens_i, (label, focal_length) in enumerate(box.items(), start=1):
        total_focusing_power += (1 + box_i) * lens_i * focal_length

AOCUtils.print_answer(2, total_focusing_power)

AOCUtils.print_time_taken()
