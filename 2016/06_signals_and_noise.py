####################################
# --- Day 6: Signals and Noise --- #
####################################

from collections import defaultdict
import AOCUtils

####################################

messages = AOCUtils.load_input(6)

counts = [defaultdict(int) for _ in messages[0]]
for message in messages:
    for i, c in enumerate(message):
        counts[i][c] += 1

corrected = ''.join(max((ct, c) for c, ct in count.items())[1] for count in counts)
AOCUtils.print_answer(1, corrected)

corrected = ''.join(max((-ct, c) for c, ct in count.items())[1] for count in counts)
AOCUtils.print_answer(2, corrected)

AOCUtils.print_time_taken()