################################
# --- Day 18: Like a Rogue --- #
################################

import AOCUtils

def get_safe_tiles(cur, n):
    cur = list(cur)

    safe_tiles = 0
    for _ in range(n):
        safe_tiles += cur.count('.')

        nxt = []
        for i in range(len(cur)):
            l = cur[i-1] if i-1 >= 0 else '.'
            r = cur[i+1] if i+1 < len(cur) else '.'

            nxt.append('^' if l != r else '.')

        cur = nxt

    return safe_tiles

################################

cur = AOCUtils.load_input(18)

AOCUtils.print_answer(1, get_safe_tiles(cur, 40))

AOCUtils.print_answer(2, get_safe_tiles(cur, 400000))

AOCUtils.print_time_taken()