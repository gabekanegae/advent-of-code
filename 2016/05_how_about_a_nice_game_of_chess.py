##################################################
# --- Day 5: How About a Nice Game of Chess? --- #
##################################################

import AOCUtils
import hashlib

##################################################

doorID = AOCUtils.loadInput(5)
baseDigest = hashlib.md5(doorID.encode())

password1 = []
password2 = ["_" for _ in range(8)]

i = 0
while len(password1) < 8 or "_" in password2:
    digest = baseDigest.copy()
    digest.update(str(i).encode())
    s = digest.hexdigest()

    if s.startswith("00000"):
        if len(password1) < 8:
            password1.append(s[5])

        if "_" in password2:
            idx = int(s[5], 16)
            if idx < 8 and password2[idx] == "_":
                password2[idx] = s[6]
    
    i += 1

print("Part 1: {}".format("".join(password1)))

print("Part 2: {}".format("".join(password2)))

AOCUtils.printTimeTaken()