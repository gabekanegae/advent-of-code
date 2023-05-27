################################
# --- Day 14: One-Time Pad --- #
################################

import AOCUtils
import hashlib

def getOTP(salt, part=1):
    possibleKeys = {k: [] for k in "0123456789abcdef"}
    otpKeys = set()

    baseDigest = hashlib.md5(salt.encode())

    i = 0
    while len(otpKeys) < 64:
        digest = baseDigest.copy()
        digest.update(str(i).encode())
        s = digest.hexdigest()

        if part == 2:
            for _ in range(2016):
                s = hashlib.md5(s.encode()).hexdigest()

        for c in range(len(s)-3-1):
            if len(set(s[c:c+3])) == 1:
                possibleKeys[s[c]].append(i)
                break

        for c in range(len(s)-5-1):
            if len(set(s[c:c+5])) == 1:
                for keyi in possibleKeys[s[c]]:
                    if keyi+1 <= i <= keyi+1000:
                        otpKeys.add(keyi)
                break

        i += 1

    return sorted(otpKeys)[63]

################################

salt = AOCUtils.loadInput(14)

print("Part 1: {}".format(getOTP(salt, part=1)))

print("Part 2: {}".format(getOTP(salt, part=2)))

AOCUtils.printTimeTaken()