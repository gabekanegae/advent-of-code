##############################
# --- Day 6: Wait For It --- #
##############################

import AOCUtils

def get_wins_count(time, distance):
    time, distance = int(time), int(distance)
    return sum((t * (time - t)) > distance for t in range(time+1))

##############################

raw_races = AOCUtils.load_input(6)

times, distances = [l.split(':')[1].split() for l in raw_races]

ways = 1
for time, distance in zip(times, distances):
    ways *= get_wins_count(time, distance)

AOCUtils.print_answer(1, ways)

time, distance = [l.split(':')[1].replace(' ', '') for l in raw_races]

AOCUtils.print_answer(2, get_wins_count(time, distance))

AOCUtils.print_time_taken()
