#######################################
# --- Day 5: Alchemical Reduction --- #
#######################################

import AOCUtils

def diff_polarity(a, b):
    return ord(a) == ord(b)+32 or ord(a)+32 == ord(b)

def react(polymer):
    stack = []
    for p in polymer:
        if len(stack) == 0 or not diff_polarity(p, stack[-1]):
            stack.append(p)
        else:
            stack.pop()

    return len(stack)

#######################################

base_polymer = AOCUtils.load_input(5)

AOCUtils.print_answer(1, react(base_polymer))

min_size, min_type = None, None
for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    polymer = ''.join(p for p in base_polymer if p.upper() != c.upper())
    size = react(polymer)
    if not min_size or size < min_size:
        min_size = size
        min_type = c

AOCUtils.print_answer(2, min_size)

AOCUtils.print_time_taken()