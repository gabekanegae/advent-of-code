#####################################
# --- Day 14: Reindeer Olympics --- #
#####################################

import AOCUtils

#####################################

raw_reindeers = AOCUtils.load_input(14)
time_limit = 2503

reindeers = dict()
for raw_reindeer in raw_reindeers:
    raw_reindeer = raw_reindeer.split()

    name = raw_reindeer[0]
    speed = int(raw_reindeer[3])
    fly_time = int(raw_reindeer[6])
    rest_time = int(raw_reindeer[13])

    reindeer = {'speed': speed, 'fly_time': fly_time, 'rest_time': rest_time}
    reindeers[name] = reindeer

positions = {reindeer: 0 for reindeer in reindeers}
points = {reindeer: 0 for reindeer in reindeers}
for t in range(time_limit):
    for name, reindeer in reindeers.items():
        is_flying = (t % (reindeer['fly_time'] + reindeer['rest_time']) < reindeer['fly_time'])
        if is_flying:
            positions[name] += reindeer['speed']

    max_position = max(positions.values())
    for name, reindeer in reindeers.items():
        if positions[name] == max_position:
            points[name] += 1

AOCUtils.print_answer(1, max(positions.values()))

AOCUtils.print_answer(2, max(points.values()))

AOCUtils.print_time_taken()