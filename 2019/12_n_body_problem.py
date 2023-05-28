######################################
# --- Day 12: The N-Body Problem --- #
######################################

import AOCUtils
from math import gcd

class Moon:
    def __init__(self, rawPos, vel=None):
        self.pos = [int(c.split('=')[1]) for c in rawPos[1:-1].split(',')]
        self.vel = vel or [0, 0, 0]

    def get_state(self, c):
        return (self.pos[c], self.vel[c])

class MoonSystem:
    def __init__(self, moons):
        self.moons = moons

    def step(self):
        for c in range(3):
            for mooni in self.moons:
                for moonj in self.moons:
                    if mooni is moonj: continue
                    if mooni.pos[c] > moonj.pos[c]:
                        mooni.vel[c] -= 1
                    elif mooni.pos[c] < moonj.pos[c]:
                        mooni.vel[c] += 1

            for mooni in self.moons:
                mooni.pos[c] += mooni.vel[c]

    def get_total_energy(self):
        pot = [sum(abs(x) for x in moon.pos) for moon in self.moons]
        kin = [sum(abs(x) for x in moon.vel) for moon in self.moons]
        return sum(p*k for p, k in zip(pot, kin))

    def get_state(self, c):
        return str([moon.get_state(c) for moon in self.moons])

# Get LCM of 2 values
def lcm_2(x, y):
    return abs(x*y) // gcd(x,y)

# Get LCM of a list of N values
def lcm_N(a):
    l = lcm_2(a[0], a[1])
    for i in a[2:]:
        l = lcm_2(l, i)
    
    return l

######################################

raw_moons = AOCUtils.load_input(12)
moons = [Moon(raw_moon) for raw_moon in raw_moons]

system = MoonSystem(moons)
for _ in range(1000):
    system.step()

AOCUtils.print_answer(1, system.get_total_energy())

# Find periods of each axis
periods = [0 for _ in range(3)]
seen = [set() for _ in range(3)]

system = MoonSystem(moons)
step = 0
while not all(periods):
    for c in range(3):
        if not periods[c]:
            state = system.get_state(c)
            if state in seen[c]:
                periods[c] = step
            else:
                seen[c].add(state)

    system.step()
    step += 1

# Get LCM of all periods
AOCUtils.print_answer(2, lcm_N(periods))

AOCUtils.print_time_taken()