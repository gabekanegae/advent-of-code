###########################################
# --- Day 9: Explosives in Cyberspace --- #
###########################################

import AOCUtils

def parse_marker(file):
    marker = file[1:].split(')')[0]
    marker_len = len(marker) + 2
    chr_amount, repeat_amount = map(int, marker.split('x'))

    return marker_len, chr_amount, repeat_amount

def decompress_file(file, first_level_only=False):
    totalLen = 0

    i = 0
    while i < len(file):
        if file[i] == '(':
            marker_len, chr_amount, repeat_amount = parse_marker(file[i:])

            i += marker_len

            if first_level_only:
                totalLen += chr_amount * repeat_amount
            else:
                totalLen += decompress_file(file[i:i+chr_amount]) * repeat_amount

            i += chr_amount
        else:
            dataLen = len(file[i:].split('(')[0])

            i += dataLen
            totalLen += dataLen

    return totalLen

###########################################

file = AOCUtils.load_input(9)

AOCUtils.print_answer(1, decompress_file(file, True))

AOCUtils.print_answer(2, decompress_file(file))

AOCUtils.print_time_taken()