##############################
# --- Day 8: Matchsticks --- #
##############################

import AOCUtils

def count_code(s):
    # Remove first and last chars (")
    s = s[1:-1]
    n = 2

    i = 0
    while i < len(s):
        if s[i] == '\\':
            n += 1 # Skip \
            i += 1
            if i < len(s) and s[i] == 'x':
                n += 2 # Skip xn
                i += 2
        i += 1

    return n

def encode(s):
    encoded = ''

    for c in s:
        if c in '"\\':
            encoded += '\\'
        encoded += c

    return '"' + ''.join(encoded) + '"'

##############################

strings = AOCUtils.load_input(8)

total = sum(count_code(s) for s in strings)
AOCUtils.print_answer(1, total)

strings = [encode(s) for s in strings]

total = sum(count_code(s) for s in strings)
AOCUtils.print_answer(2, total)

AOCUtils.print_time_taken()