#####################################################
# --- Day 1: The Tyranny of the Rocket Equation --- #
#####################################################

import AOCUtils

def required_fuel(m):
    return (m // 3) - 2

#####################################################

masses = AOCUtils.load_input(1)

fuel_sum = sum(map(required_fuel, masses))
AOCUtils.print_answer(1, fuel_sum)

fuel_sum = 0
for m in masses:
    fuel = required_fuel(m)
    while fuel >= 0:
        fuel_sum += fuel
        fuel = required_fuel(fuel)

AOCUtils.print_answer(2, fuel_sum)

AOCUtils.print_time_taken()