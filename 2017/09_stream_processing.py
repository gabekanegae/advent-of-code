####################################
# --- Day 9: Stream Processing --- #
####################################

import AOCUtils

def get_comma(stream, p):
    if p < len(stream):
        while stream[p] == ',':
            p += 1 # ,

    return p

def get_cancel(stream, p):
    if p < len(stream):
        while stream[p] == '!':
            p += 2 # ! and next

    return p

def get_garbage(stream, p):
    removed = 0

    if p < len(stream):
        while stream[p] == '<':
            p += 1 # <

            while stream[p] != '>':
                p = get_cancel(stream, p)

                if stream[p] != '>':
                    p += 1 # garbage
                    removed += 1

            p += 1 # >

            p = get_comma(stream, p)

    return p, removed

def get_group(stream, p=0, level=1):
    score = 0
    removed = 0

    p, n_removed = get_garbage(stream, p)
    removed += n_removed

    while p < len(stream) and stream[p] == '{':
        p += 1 # {
        p, n_score, n_removed = get_group(stream, p, level+1)
        score += n_score
        removed += n_removed

        p, n_removed = get_garbage(stream, p)
        removed += n_removed

        if stream[p] == '}':
            p += 1 # }
            score += level

        p = get_comma(stream, p)

    return (p, score, removed)

####################################

stream = AOCUtils.load_input(9)
_, score, removed = get_group(stream)

AOCUtils.print_answer(1, score)

AOCUtils.print_answer(2, removed)

AOCUtils.print_time_taken()