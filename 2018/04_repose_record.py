################################
# --- Day 4: Repose Record --- #
################################

import AOCUtils

################################

log = AOCUtils.load_input(4)

log.sort()

guards = dict()
for entry in log:
    if 'begins shift' in entry:
        guard_id = int(entry.split('#')[1].split()[0])
    elif 'falls asleep' in entry:
        sleepStart = int(entry.split(':')[1].split(']')[0])
    elif 'wakes up' in entry:
        sleepEnd = int(entry.split(':')[1].split(']')[0])
        
        if guard_id not in guards:
            guards[guard_id] = [0 for _ in range(60)]

        for t in range(sleepStart, sleepEnd):
            guards[guard_id][t] += 1

max_id, max_total = None, None
for k, v in guards.items():
    total = sum(v)
    if not max_total or total > max_total:
        max_total, max_id = total, k

max_time = guards[max_id].index(max(guards[max_id]))

AOCUtils.print_answer(1, max_id * max_time)

max_id, max_time, max_count = None, None, None
for k, v in guards.items():
    for i, count in enumerate(v):
        if not max_count or count > max_count:
            max_id = k
            max_time = i
            max_count = count

AOCUtils.print_answer(2, max_id * max_time)

AOCUtils.print_time_taken()