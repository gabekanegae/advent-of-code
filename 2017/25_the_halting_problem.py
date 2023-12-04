#######################################
# --- Day 25: The Halting Problem --- #
#######################################

import AOCUtils

#######################################

raw_code = AOCUtils.load_input(25)
code = [s.strip()[:-1] if s else '' for s in raw_code]

start_state = code[0][-1]
steps = int(code[1].split()[-2])

raw_states = [s.split()[-1] for s in code[2:] if s]

states = dict()
for i in range(0, len(raw_states), 9):
    cur = raw_states[i]

    state = dict()
    for j in range(i, i+2*4, 4):
        value = int(raw_states[j+1])
        write = int(raw_states[j+2])
        move = 1 if raw_states[j+3] == 'right' else -1
        nxt = raw_states[j+4]

        state[value] = {'write': write, 'move': move, 'nxt': nxt}

    states[cur] = state

cur_state = start_state
cur_pos = 0

tape = dict()
for step in range(steps):
    if cur_pos not in tape:
        tape[cur_pos] = 0

    action = states[cur_state][tape[cur_pos]]

    tape[cur_pos] = action['write']
    cur_pos += action['move']
    cur_state = action['nxt']

AOCUtils.print_answer(1, sum(tape.values()))

AOCUtils.print_time_taken()