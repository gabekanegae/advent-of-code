#########################################################
# --- Day 5: Doesn't He Have Intern-Elves For This? --- #
#########################################################

import AOCUtils

def isNice1(s):
    if sum(c in "aeiou" for c in s) < 3: return False
    if not any(s[i-1] == s[i] for i in range(1, len(s))): return False
    if any(c in s for c in ["ab", "cd", "pq", "xy"]): return False

    return True

def isNice2(s):
    # Group indexes of repeated substrings
    substrs = dict()
    for i in range(len(s)-1):
        p = s[i:i+2]
        if p not in substrs:
            substrs[p] = []
        substrs[p].append(i)
    substrs = substrs.values()

    if not any(any(abs(i-j) > 1 for j in c for i in c if i != j) for c in substrs): return False
    if not any(s[i-1] == s[i+1] for i in range(1, len(s)-1)): return False

    return True

#########################################################

strings = AOCUtils.loadInput(5)

count = sum(isNice1(s) for s in strings)
print("Part 1: {}".format(count))

count = sum(isNice2(s) for s in strings)
print("Part 1: {}".format(count))

AOCUtils.printTimeTaken()