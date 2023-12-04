###########################################
# --- Day 4: High-Entropy Passphrases --- #
###########################################

import AOCUtils

###########################################

raw_passphrases = AOCUtils.load_input(4)
passphrases = [s.split() for s in raw_passphrases]

AOCUtils.print_answer(1, sum(len(p) == len(set(p)) for p in passphrases))

passphrases = [[''.join(sorted(word)) for word in p] for p in passphrases]

AOCUtils.print_answer(2, sum(len(p) == len(set(p)) for p in passphrases))

AOCUtils.print_time_taken()