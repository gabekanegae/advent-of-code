###################################
# --- Day 13: Distress Signal --- #
###################################

import AOCUtils
from functools import cmp_to_key

def cmp(a, b):
    if type(a) is int and type(b) is int:
        if a == b: return 0
        elif a < b: return -1
        elif a > b: return 1
    
    if type(a) is int and type(b) is list:
        a = [a]
    elif type(a) is list and type(b) is int:
        b = [b]

    for a_i, b_i in zip(a, b):
        r = cmp(a_i, b_i)
        if r != 0: return r

    if len(a) == len(b): return 0
    elif len(a) < len(b): return -1
    elif len(a) > len(b): return 1

###################################

raw_packets = AOCUtils.load_input(13)
packets = list(map(eval, filter(lambda l: l.startswith('['), raw_packets)))

packet_pairs = [(packets[i], packets[i+1]) for i in range(0, len(packets), 2)]

ordered_pairs_sum = sum(i+1 for i, (a, b) in enumerate(packet_pairs) if cmp(a, b) == -1)
AOCUtils.print_answer(1, ordered_pairs_sum)

dividers = [[[2]], [[6]]]
packets += dividers

packets.sort(key=cmp_to_key(cmp))

decoder_key = (packets.index(dividers[0]) + 1) * (packets.index(dividers[1]) + 1)
AOCUtils.print_answer(2, decoder_key)

AOCUtils.print_time_taken()