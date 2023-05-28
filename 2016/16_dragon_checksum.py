###################################
# --- Day 16: Dragon Checksum --- #
###################################

import AOCUtils

def getChecksum(data, diskLen):
    inv = {'0': '1', '1': '0'}
    data = list(data)

    while len(data) < diskLen:
        b = [inv[c] for c in data[:][::-1]]
        data += ['0']
        data += b

    data = data[:diskLen]

    while len(data) % 2 == 0:
        new_data = []
        for i in range(0, len(data), 2):
            c = '1' if data[i] == data[i+1] else '0'
            new_data.append(c)
        data = new_data

    return ''.join(data)

###################################

data = str(AOCUtils.load_input(16))

AOCUtils.print_answer(1, getChecksum(data, 272))

AOCUtils.print_answer(2, getChecksum(data, 35651584))

AOCUtils.print_time_taken()