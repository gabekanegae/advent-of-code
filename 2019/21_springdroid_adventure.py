#########################################
# --- Day 21: Springdroid Adventure --- #
#########################################

import AOCUtils
from intcodeVM import VM

def run_spring_script(memory, script):
    vm = VM(memory)
    vm.run('\n'.join(script) + '\n')

    return vm.output[-1]

#########################################

raw_program = AOCUtils.load_input(21)
memory = [int(i) for i in raw_program.split(',')]

# Jump if     (has to jump)    and  (can jump)
# Jump if ((hole in A, B or C) and (floor in D))
script_1 = [
'OR A T',   # T = A
'AND B T',  # T = A & B
'AND C T',  # T = A & B & C
'NOT T J',  # J = !(A & B & C)
'AND D J',  # J = !(A & B & C) & D
'WALK'
]

AOCUtils.print_answer(1, run_spring_script(memory, script_1))

# Jump if     (has to jump)    and (can step/jump after) and  (can jump)
# Jump if ((hole in A, B or C) and   (floor in E or H)   and (floor in D))

script_2 = [
'OR A T',   # T = A
'AND B T',  # T = A & B
'AND C T',  # T = A & B & C
'NOT T T',  # T = !(A & B & C)
'OR E J',   # J = E
'OR H J',   # J = E | H
'AND T J',  # J = !(A & B & C) & (E | H)
'AND D J',  # J = !(A & B & C) & (E | H) & D
'RUN'
]

AOCUtils.print_answer(2, run_spring_script(memory, script_2))

AOCUtils.print_time_taken()