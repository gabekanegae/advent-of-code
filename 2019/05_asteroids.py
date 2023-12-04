###################################################
# --- Day 5: Sunny with a Chance of Asteroids --- #
###################################################

import AOCUtils
from intcodeVM import VM

###################################################

raw_program = AOCUtils.load_input(5)
memory = list(map(int, raw_program.split(',')))

vm = VM(memory)
vm.run(1)
AOCUtils.print_answer(1, vm.output[-1])

vm = VM(memory)
vm.run(5)
AOCUtils.print_answer(2, vm.output[-1])

AOCUtils.print_time_taken()