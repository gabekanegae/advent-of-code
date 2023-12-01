################################
# --- Day 5: Supply Stacks --- #
################################

import AOCUtils

def move_crates(stacks, instructions, order):
    stacks = [stack[:] for stack in stacks]
    
    for instruction in instructions:
        args = instruction.split()
        amt, src, dst = int(args[1]), int(args[3]) - 1, int(args[5]) - 1

        stacks[dst] += stacks[src][-amt:][::order]
        stacks[src] = stacks[src][:-amt]

    stack_tops = ''.join(stack[-1] for stack in stacks)
    return stack_tops

################################

raw_cargo = AOCUtils.load_input(5)

line_break_idx = next(i for i, l in enumerate(raw_cargo) if l == '')

crates = raw_cargo[:line_break_idx-1]
total_crates = len(raw_cargo[line_break_idx-1].split())
instructions = raw_cargo[line_break_idx+1:]

stacks = [[] for _ in range(total_crates)]
for level in range(len(crates)):
    for i in range(1, len(crates[0]), 4):
        crate = crates[level][i]
        if crate != ' ':
            stacks[(i-1)//4].append(crate)

stacks = [stack[::-1] for stack in stacks]

stack_tops = move_crates(stacks, instructions, -1)
AOCUtils.print_answer(1, stack_tops)

stack_tops = move_crates(stacks, instructions, 1)
AOCUtils.print_answer(2, stack_tops)

AOCUtils.print_time_taken()