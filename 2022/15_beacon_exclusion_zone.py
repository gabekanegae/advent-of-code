#########################################
# --- Day 15: Beacon Exclusion Zone --- #
#########################################

import AOCUtils

class Sensor:
    def __init__(self, raw):
        raw = raw.split()

        x, y = raw[2:4]
        beacon_x, beacon_y = raw[-2:]

        self.x = int(x[2:-1])
        self.y = int(y[2:-1])
        self.beacon_x = int(beacon_x[2:-1])
        self.beacon_y = int(beacon_y[2:])

        self.radius = abs(self.x - self.beacon_x) + \
                      abs(self.y - self.beacon_y)

#########################################

raw_sensors = AOCUtils.load_input(15)

sensors = [Sensor(raw_sensor) for raw_sensor in raw_sensors]

occupied_positions = set()
for sensor in sensors:
    occupied_positions.add((sensor.x, sensor.y))
    occupied_positions.add((sensor.beacon_x, sensor.beacon_y))

cant_have_beacon = set()
y_test = 2000000
for sensor in sensors:
    y_dist = abs(sensor.y - y_test)
    x_dist = sensor.radius - y_dist

    for x in range(0, x_dist+1):
        cant_have_beacon.add((sensor.x+x, y_test))
        cant_have_beacon.add((sensor.x-x, y_test))

cant_have_beacon -= occupied_positions

AOCUtils.print_answer(1, len(cant_have_beacon))

possible_points = set()
for sensor in sensors:
    expanded_radius = sensor.radius + 1
    for d in range(expanded_radius):
        delta_x = expanded_radius - d
        delta_y = d

        points = [
            (sensor.x+delta_x, sensor.y+delta_y),
            (sensor.x+delta_x, sensor.y-delta_y),
            (sensor.x-delta_x, sensor.y-delta_y),
            (sensor.x-delta_x, sensor.y+delta_y)
        ]
        for p_x, p_y in points:
            if 0 <= p_x <= 4000000 and 0 <= p_y <= 4000000:
                possible_points.add((p_x, p_y))

for point_x, point_y in possible_points:
    if all(abs(point_x - sensor.x) + abs(point_y - sensor.y) > sensor.radius for sensor in sensors):
        tuning_frequency = point_x * 4000000 + point_y
        break

AOCUtils.print_answer(2, tuning_frequency)

AOCUtils.print_time_taken()