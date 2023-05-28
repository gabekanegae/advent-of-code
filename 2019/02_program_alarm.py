#####################################
# --- Day 2: 1202 Program Alarm --- #
#####################################

import AOCUtils
from intcodeVM import VM

#####################################

raw_program = AOCUtils.load_input(2)
memory = [int(i) for i in raw_program.split(',')]

vm = VM(memory)
vm[1], vm[2] = 12, 2
vm.run()
AOCUtils.print_answer(1, vm[0])

found = False
for noun in range(100):
    if found: break
    
    for verb in range(100):
        vm = VM(memory)
        vm[1], vm[2] = noun, verb
        
        vm.run()

        if vm[0] == 19690720:
            AOCUtils.print_answer(2, 100*noun + verb)
            found = True
            break

AOCUtils.print_time_taken()