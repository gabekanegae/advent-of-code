###############################
# --- Day 9: Sensor Boost --- #
###############################

import AOCUtils
from intcodeVM import VM

###############################

raw_program = AOCUtils.load_input(9)
memory = list(map(int, raw_program.split(',')))

vm = VM(memory)
vm.run(1)
AOCUtils.print_answer(1, vm.output[0])

vm = VM(memory)
vm.run(2)
AOCUtils.print_answer(2, vm.output[0])

AOCUtils.print_time_taken()