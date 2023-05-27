#######################################
# --- Day 7: The Sum of Its Parts --- #
#######################################

from collections import deque
import AOCUtils

#######################################

rawReqs = AOCUtils.loadInput(7)

reqs = dict()
for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    reqs[c] = set()
for r in rawReqs:
    reqs[r[36]].add(r[5])

done = ""
while len(done) < 26:
    for k, v in reqs.items():
        if k in done: continue

        if v.issubset(set(done)):
            done += k
            break

print("Part 1: {}".format(done))

time = 0
workers = [{"remaining": 0, "letter": "-"} for _ in range(5)]
queue = deque()
doing, done = set(), set()

while len(done) < 26:
    for k, v in reqs.items():
        if k in done: continue
        if k in doing: continue
        if k in queue: continue

        if v.issubset(done):
            queue.append(k)

    while len(queue) > 0:
        idleWorker = None
        for i in range(5):
            if workers[i]["letter"] == "-":
                idleWorker = i
                break
        if idleWorker == None:
            break

        c = queue.popleft()
        doing.add(c)
        workers[idleWorker]["letter"] = c
        workers[idleWorker]["remaining"] = ord(c)-4

    for i in range(5):
        if workers[i]["letter"] != "-":
            workers[i]["remaining"] -= 1
            if workers[i]["remaining"] == 0:
                c = workers[i]["letter"]
                done.add(c)
                doing.remove(c)
                workers[i]["letter"] = "-"

    time += 1

print("Part 2: {}".format(time))

AOCUtils.printTimeTaken()