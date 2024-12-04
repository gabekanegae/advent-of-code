###############################
# --- Day 3: Mull It Over --- #
###############################

import AOCUtils

###############################

digits = set('0123456789')

def parse_corrupted_memory(memory):
    total = 0

    muls = memory.split('mul(')[1:]
    for mul in muls:
        mul_operands = mul.split(')')[0].split(',')
        
        if len(mul_operands) != 2: continue
        if any(any(c not in digits for c in op) for op in mul_operands): continue
        if any(not (1 <= len(op) <= 3) for op in mul_operands): continue

        mul_result = int(mul_operands[0]) * int(mul_operands[1])
        total += mul_result

    return total

###############################

memory = '\n'.join(AOCUtils.load_input(3))

AOCUtils.print_answer(1, parse_corrupted_memory(memory))

enabled_memory = ''
enabled = True
for i in range(len(memory)):
    if memory[i:].startswith('do()'):
        enabled = True

    if memory[i:].startswith('don\'t()'):
        enabled = False
    
    if enabled:
        enabled_memory += memory[i]

AOCUtils.print_answer(2, parse_corrupted_memory(enabled_memory))

AOCUtils.print_time_taken()
