#############################################
# --- Day 4: The Ideal Stocking Stuffer --- #
#############################################

import AOCUtils
import hashlib

#############################################

key = AOCUtils.loadInput(4)
baseDigest = hashlib.md5(key.encode())

i = 1
while True:
    digest = baseDigest.copy()
    digest.update(str(i).encode())
    s = digest.hexdigest()

    if s.startswith("0"*5):
        print("Part 1: {}".format(i))
        break
    
    i += 1

while True:
    digest = baseDigest.copy()
    digest.update(str(i).encode())
    s = digest.hexdigest()

    if s.startswith("0"*6):
        print("Part 2: {}".format(i))
        break
    
    i += 1

AOCUtils.printTimeTaken()