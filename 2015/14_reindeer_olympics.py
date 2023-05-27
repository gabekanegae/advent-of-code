#####################################
# --- Day 14: Reindeer Olympics --- #
#####################################

import AOCUtils

#####################################

rawReindeers = AOCUtils.loadInput(14)
timeLimit = 2503

reindeers = dict()
for rawReindeer in rawReindeers:
    rawReindeer = rawReindeer.split()

    name = rawReindeer[0]
    speed = int(rawReindeer[3])
    flyTime = int(rawReindeer[6])
    restTime = int(rawReindeer[13])

    reindeer = {"speed": speed, "flyTime": flyTime, "restTime": restTime}
    reindeers[name] = reindeer

positions = {reindeer: 0 for reindeer in reindeers}
points = {reindeer: 0 for reindeer in reindeers}
for t in range(timeLimit):
    for name, reindeer in reindeers.items():
        isFlying = (t % (reindeer["flyTime"] + reindeer["restTime"]) < reindeer["flyTime"])
        if isFlying:
            positions[name] += reindeer["speed"]

    maxPosition = max(positions.values())
    for name, reindeer in reindeers.items():
        if positions[name] == maxPosition:
            points[name] += 1

print("Part 1: {}".format(max(positions.values())))

print("Part 2: {}".format(max(points.values())))

AOCUtils.printTimeTaken()