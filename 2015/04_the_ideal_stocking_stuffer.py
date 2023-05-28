#############################################
# --- Day 4: The Ideal Stocking Stuffer --- #
#############################################

import AOCUtils
import hashlib

#############################################

key = AOCUtils.load_input(4)
base_digest = hashlib.md5(key.encode())

i = 1
while True:
    digest = base_digest.copy()
    digest.update(str(i).encode())
    s = digest.hexdigest()

    if s.startswith('0'*5):
        AOCUtils.print_answer(1, i)
        break
    
    i += 1

while True:
    digest = base_digest.copy()
    digest.update(str(i).encode())
    s = digest.hexdigest()

    if s.startswith('0'*6):
        AOCUtils.print_answer(2, i)
        break
    
    i += 1

AOCUtils.print_time_taken()