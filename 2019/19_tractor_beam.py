################################
# --- Day 19: Tractor Beam --- #
################################

import AOCUtils
from intcodeVM import VM
from collections import deque

def check(memory, x, y):
    vm = VM(memory)
    vm.run([x, y])

    return vm.output[-1]

################################

raw_program = AOCUtils.load_input(19)
memory = [int(i) for i in raw_program.split(',')]

total = 0
x_0 = 0
for y in range(50):
    zeros, ones = 0, 0
    for x in range(x_0, 50):
        if check(memory, x, y) == 1:
            # Assumes that it can start the next line
            # at the pos of first ocurrence of 1 in this one
            if ones == 0: x_0 = x
            ones += 1
        else:
            # Assumes that there won't be 1s after...
            if ones > 0: # '10'
                total += ones
                break
            else: # '00000'
                zeros += 1
                if zeros > 5: break

AOCUtils.print_answer(1, total)

result = None
x_0 = 0
for y in range(100, 10000): # Skip first 100 lines
    if result: break
    for x in range(x_0, 10000):
        # Go along bottom edge of beam (bottom-left square)
        if check(memory, x, y) == 1:
            if check(memory, x+99, y-99) == 1: # Check top-right square
                result = 10000*x + (y-99) # Result is top-left square
            x_0 = x
            break

AOCUtils.print_answer(2, result)

AOCUtils.print_time_taken()