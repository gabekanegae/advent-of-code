###########################################
# --- Day 9: Explosives in Cyberspace --- #
###########################################

import AOCUtils

def parse_marker(file):
    marker = file[1:].split(')')[0]
    marker_length = len(marker) + 2
    chr_amount, repeat_amount = map(int, marker.split('x'))

    return marker_length, chr_amount, repeat_amount

def decompress_file(file, first_level_only=False):
    total_length = 0

    i = 0
    while i < len(file):
        if file[i] == '(':
            marker_length, chr_amount, repeat_amount = parse_marker(file[i:])

            i += marker_length

            if first_level_only:
                total_length += chr_amount * repeat_amount
            else:
                total_length += decompress_file(file[i:i+chr_amount]) * repeat_amount

            i += chr_amount
        else:
            data_length = len(file[i:].split('(')[0])

            i += data_length
            total_length += data_length

    return total_length

###########################################

file = AOCUtils.load_input(9)

AOCUtils.print_answer(1, decompress_file(file, True))

AOCUtils.print_answer(2, decompress_file(file))

AOCUtils.print_time_taken()