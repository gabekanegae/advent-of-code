##################################
# --- Day 20: Particle Swarm --- #
##################################

import AOCUtils

class Particle:
    def __init__(self, pid, raw_particle):
        self.pid = pid
        self.removed = False

        p, v, a = raw_particle.split(', ')
        self.p = [int(i) for i in p[3:-1].split(',')]
        self.v = [int(i) for i in v[3:-1].split(',')]
        self.a = [int(i) for i in a[3:-1].split(',')]

    def update(self):
        if not self.removed:
            self.v = tuple(v + a for v, a in zip(self.v, self.a))
            self.p = tuple(p + v for p, v in zip(self.p, self.v))

##################################

raw_particles = AOCUtils.load_input(20)
particles = [Particle(i, p) for i, p in enumerate(raw_particles)]

for _ in range(1000):
    for p in particles:
        p.update()

m = min(particles, key=lambda p: sum(map(abs, p.p)))
AOCUtils.print_answer(1, m.pid)

particles = [Particle(i, p) for i, p in enumerate(raw_particles)]

for _ in range(1000):
    for p in particles:
        p.update()

    collisions = dict()
    for p in particles:
        if p.removed: continue

        if p.p not in collisions:
            collisions[p.p] = []
        collisions[p.p].append(p)

    for collision in collisions.values():
        if len(collision) > 1:
            for p in collision:
                p.removed = True

AOCUtils.print_answer(2, sum(not p.removed for p in particles))

AOCUtils.print_time_taken()