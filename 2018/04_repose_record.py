################################
# --- Day 4: Repose Record --- #
################################

import AOCUtils

################################

log = sorted(AOCUtils.loadInput(4))

guards = dict()
for entry in log:
    if "begins shift" in entry:
        guardID = int(entry.split("#")[1].split()[0])
    elif "falls asleep" in entry:
        sleepStart = int(entry.split(":")[1].split("]")[0])
    elif "wakes up" in entry:
        sleepEnd = int(entry.split(":")[1].split("]")[0])
        
        if guardID not in guards:
            guards[guardID] = [0 for _ in range(60)]

        for t in range(sleepStart, sleepEnd):
            guards[guardID][t] += 1

maxID, maxTotal = None, None
for k, v in guards.items():
    total = sum(v)
    if not maxTotal or total > maxTotal:
        maxTotal, maxID = total, k

maxTime = guards[maxID].index(max(guards[maxID]))
print("Part 1: {}".format(maxID*maxTime))

maxID, maxTime, maxCount = None, None, None
for k, v in guards.items():
    for i, count in enumerate(v):
        if not maxCount or count > maxCount:
            maxID = k
            maxTime = i
            maxCount = count

print("Part 2: {}".format(maxID*maxTime))

AOCUtils.printTimeTaken()