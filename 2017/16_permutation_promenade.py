#########################################
# --- Day 16: Permutation Promenade --- #
#########################################

import AOCUtils

def dance(programs, moves):
    programs = list(programs)
    for move in moves:
        if move[0] == 's':
            n = int(move[1:])
            programs = programs[-n:] + programs[:-n]
        elif move[0] == 'x':
            a, b = [int(i) for i in move[1:].split('/')]
            programs[a], programs[b] = programs[b], programs[a]
        elif move[0] == 'p':
            a, b = move[1], move[3]
            pa, pb = programs.index(a), programs.index(b)
            programs[pa], programs[pb] = programs[pb], programs[pa]

    return ''.join(programs)

#########################################

moves = AOCUtils.load_input(16).split(',')

original_programs = 'abcdefghijklmnop'

AOCUtils.print_answer(1, dance(original_programs, moves))

programs = original_programs
seen_str = {programs: 0}
seen_id = {0: programs}

i = 1
while True:
    programs = dance(programs, moves)
    if programs in seen_str:
        loop = (seen_str[programs], i)
        break

    seen_str[programs] = i
    seen_id[i] = programs

    i += 1

loop = (1000000000 - loop[0]) % (loop[1] - loop[0])

AOCUtils.print_answer(2, seen_id[loop])

AOCUtils.print_time_taken()