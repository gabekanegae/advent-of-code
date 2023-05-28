####################################
# --- Day 2: Bathroom Security --- #
####################################

import AOCUtils

moves = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

def keypad_walk(keypad, instructions):
    size = (len(keypad), len(keypad[0]))
    pos = (size[0]//2, size[1]//2)
    
    code = []
    for instruction in instructions:
        for move in instruction:
            delta = moves[move]
            nxt = (pos[0]+delta[0], pos[1]+delta[1])
            if 0 <= nxt[0] < size[0] and 0 <= nxt[1] < size[1] and keypad[nxt[0]][nxt[1]] != ' ':
                pos = nxt

        code.append(keypad[pos[0]][pos[1]])

    return ''.join(code)

####################################

instructions = AOCUtils.load_input(2)

keypad1 = ['123',
           '456',
           '789']

AOCUtils.print_answer(1, keypad_walk(keypad1, instructions))

keypad2 = ['  1  ',
           ' 234 ',
           '56789',
           ' ABC ',
           '  D  ']

AOCUtils.print_answer(2, keypad_walk(keypad2, instructions))

AOCUtils.print_time_taken()