#################################################
# --- Day 16: Flawed Frequency Transmission --- #
#################################################

import AOCUtils

def get_multiplier(pos, i):
    pattern = [0, 1, 0, -1]
    if i < pos:
        return pattern[0]
    else:
        i = ((i-pos) // (pos+1)) + 1
        return pattern[i%len(pattern)]

#################################################

raw_signal = AOCUtils.load_input(16)
raw_signal = str(raw_signal)
signal = list(map(int, raw_signal))

size = len(signal)

for _ in range(100):
    for i in range(size):
        new_signal = sum(signal[j] * get_multiplier(i, j) for j in range(size))
        signal[i] = abs(new_signal) % 10

first_eight = ''.join(map(str, signal[:8]))
AOCUtils.print_answer(1, first_eight)

signal = list(map(int, raw_signal)) * 10000
offset = int(''.join(str(i) for i in signal[:7]))
signal = signal[offset:]
size = len(signal)

# Partial Sum (% 10), assuming offset > size/2
for _ in range(100):
    total = 0
    for i in range(size, 0, -1):
        total = (total + signal[i-1]) % 10
        signal[i-1] = total

message = ''.join(map(str, signal[:8]))
AOCUtils.print_answer(2, message)

AOCUtils.print_time_taken()