##################################################
# --- Day 5: If You Give A Seed A Fertilizer --- #
##################################################

import AOCUtils

def apply_transform_1(seed, transform):
    for dst, src, length in transform:
        if src <= seed < src + length:
            return dst + seed - src

    return seed

# AB is input interval, XY is transformation interval
# (*) means transformation was applied, (-) means it wasn't
#       A         B        
#     X | Y       |      (X < A < Y < B) => AY(*)
#       |   X Y   |      (A < X < Y < B) => AX(-), XY(*)
#       |       X | Y    (A < X < B < Y) => AX(-), XB(*)
#     X |         | Y    (X < A < B < Y) => AB(*)
#       |         | X Y  (A < B < X < Y) => AB(-)
# X Y   |         |      (X < Y < A < B) => AB(-)
def apply_transform_2(intervals, transform):
    def get_relative_to_interval(x, interval):
        if x <= interval[0]: return -1
        if interval[0] < x < interval[1]: return 0
        if interval[1] <= x: return 1

    transform = sorted((src, src+length, dst-src) for dst, src, length in transform)

    new_intervals = []
    for a, b in intervals:
        for x, y, delta in transform:
            match (get_relative_to_interval(x, (a, b)), get_relative_to_interval(y, (a, b))):
                case (-1, 0): # X < A < Y < B
                    # XA gets discarded
                    new_intervals.append((a + delta, y + delta)) # AY(*)
                    # YB gets discarded (might be processed in next iterations)
                    a = y
                case (0, 0): # A < X < Y < B
                    new_intervals.append((a, x)) # AX(-)
                    new_intervals.append((x + delta, y + delta)) # XY(*)
                    # YB gets discarded (might be processed in next iterations)
                    a = y
                case (0, 1): # A < X < B < Y
                    new_intervals.append((a, x)) # AX(-)
                    new_intervals.append((x + delta, b + delta)) # XB(*)
                    # BY gets discarded (might be processed in next iterations)
                    a = b
                case (-1, 1): # X < A < B < Y
                    # XA gets discarded
                    new_intervals.append((a + delta, b + delta)) # AB(*)
                    # BY gets discarded (might be processed in next iterations)
                    a = b
                case (1, 1): # A < B < X < Y
                    pass
                case (-1, -1): # X < Y < A < B
                    pass

            if a == b:
                break

        if a != b:
            new_intervals.append((a, b))

    return new_intervals

##################################################

raw_data = AOCUtils.load_input(5)

seeds = list(map(int, raw_data[0].split(':')[1].split()))

raw_transforms = '\n'.join(raw_data[2:]).split('\n\n')
transforms = [[tuple(map(int, l.split())) for l in raw_transform.splitlines()[1:]] for raw_transform in raw_transforms]

min_seed = float('INF')
for seed in seeds:
    for transform in transforms:
        seed = apply_transform_1(seed, transform)
    min_seed = min(min_seed, seed)

AOCUtils.print_answer(1, min_seed)

intervals = [(seeds[i], seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2)]
for transform in transforms:
    intervals = apply_transform_2(intervals, transform)

AOCUtils.print_answer(2, min(a for a, _ in intervals))

AOCUtils.print_time_taken()