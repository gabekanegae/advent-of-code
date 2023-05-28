######################################
# --- Day 15: Dueling Generators --- #
######################################

import AOCUtils

class Generator:
    def __init__(self, factor, seed):
        self.factor = factor
        self.seed = seed

    def next(self):
        self.seed = (self.seed * self.factor) % 2147483647
        return self.seed

######################################

seeds = AOCUtils.load_input(15)

seed_a, seed_b = int(seeds[0].split()[-1]), int(seeds[1].split()[-1])
gen_a = Generator(16807, seed_a)
gen_b = Generator(48271, seed_b)

mask = 0xFFFF

judge_count = 0
for i in range(40000000):
    gen_a.next()
    gen_b.next()
    
    if gen_a.seed & mask == gen_b.seed & mask:
        judge_count += 1

AOCUtils.print_answer(1, judge_count)

judge_count = 0
for i in range(5000000):
    while gen_a.next() % 4 != 0:
        pass
    while gen_b.next() % 8 != 0:
        pass

    if gen_a.seed & mask == gen_b.seed & mask:
        judge_count += 1

AOCUtils.print_answer(2, judge_count)

AOCUtils.print_time_taken()