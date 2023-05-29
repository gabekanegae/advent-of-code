#######################################
# --- Day 7: The Sum of Its Parts --- #
#######################################

from collections import deque
import AOCUtils

#######################################

raw_requirements = AOCUtils.load_input(7)

requirements = dict()
for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    requirements[c] = set()
for r in raw_requirements:
    requirements[r[36]].add(r[5])

done = ''
while len(done) < 26:
    for k, v in requirements.items():
        if k in done: continue

        if v.issubset(set(done)):
            done += k
            break

AOCUtils.print_answer(1, done)

time = 0
workers = [{'remaining': 0, 'letter': '-'} for _ in range(5)]
queue = deque()
doing, done = set(), set()

while len(done) < 26:
    for k, v in requirements.items():
        if k in done: continue
        if k in doing: continue
        if k in queue: continue

        if v.issubset(done):
            queue.append(k)

    while len(queue) > 0:
        idle_worker = None
        for i in range(5):
            if workers[i]['letter'] == '-':
                idle_worker = i
                break
        if idle_worker == None:
            break

        c = queue.popleft()
        doing.add(c)
        workers[idle_worker]['letter'] = c
        workers[idle_worker]['remaining'] = ord(c)-4

    for i in range(5):
        if workers[i]['letter'] != '-':
            workers[i]['remaining'] -= 1
            if workers[i]['remaining'] == 0:
                c = workers[i]['letter']
                done.add(c)
                doing.remove(c)
                workers[i]['letter'] = '-'

    time += 1

AOCUtils.print_answer(2, time)

AOCUtils.print_time_taken()