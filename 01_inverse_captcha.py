##################################
# --- Day 1: Inverse Captcha --- #
##################################

import AOCUtils

##################################

digits = str(AOCUtils.loadInput(1))

totalSum = sum(int(digits[i]) for i in range(len(digits)) if digits[i] == digits[i-1])
print("Part 1: {}".format(totalSum))

skip = len(digits) // 2

totalSum = sum(int(digits[i]) for i in range(len(digits)) if digits[i] == digits[(i+skip) % len(digits)])
print("Part 2: {}".format(totalSum))

AOCUtils.printTimeTaken()