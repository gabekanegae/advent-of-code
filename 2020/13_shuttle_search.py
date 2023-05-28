##################################
# --- Day 13: Shuttle Search --- #
##################################

import AOCUtils

# Modular inverse of n (assumes mod is prime, uses Euler's Theorem)
def mod_inv(n, mod):
    return pow(n, mod-2, mod)

# Get smallest x (i.e. unique in mod N) that satisfies a list
# of linear congruences (assumes all elements in mods are coprime)
def chinese_remainder_theorem(mods, remainders):
    # Given linear congruences x%3 = 2, x%5 = 3, x%7 = 2,
    # x = chinese_remainder_theorem([3, 5, 7], [2, 3, 2])

    N = 1
    for m in mods:
        N *= m

    x = sum(r * N//m * mod_inv(N//m, m) for m, r in zip(mods, remainders))
    return x % N

##################################

notes = AOCUtils.load_input(13)

arrived_at_bus_stop = int(notes[0])
schedule = notes[1].split(',')

next_arrivals = []
for i, bus_id in enumerate(schedule):
    if bus_id == 'x': continue
    bus_interval = int(bus_id)

    since_last_arrival = arrived_at_bus_stop % bus_interval
    until_next_arrival = bus_interval - since_last_arrival

    next_arrivals.append((until_next_arrival, bus_interval))

next_arrivals.sort()
nextArrival = next_arrivals[0]

AOCUtils.print_answer(1, nextArrival[0] * nextArrival[1])

# Builds a list of linear congruences as x%mod = remainder
#   Example with schedule=[67,7,x,59,61]:
#       (t+0) % 67 = 0   ->   t % 67 = (67-0)%67   ->   t % 67 =  0 
#       (t+1) %  7 = 0   ->   t %  7 =   (7-1)%7   ->   t %  7 =  6
#       (t+3) % 59 = 0   ->   t % 59 = (59-3)%59   ->   t % 59 = 56 
#       (t+4) % 61 = 0   ->   t % 61 = (61-4)%61   ->   t % 61 = 57
#     mods = [67, 7, 59, 61]
#     remainders = [0, 6, 56, 57]

mods = []
remainders = []
for i, bus_id in enumerate(schedule):
    if bus_id == 'x': continue
    bus_interval = int(bus_id)

    mod = bus_interval
    remainder = (bus_interval - i) % bus_interval

    mods.append(mod)
    remainders.append(remainder)

AOCUtils.print_answer(2, chinese_remainder_theorem(mods, remainders))

AOCUtils.print_time_taken()