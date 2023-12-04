##################################
# --- Day 1: Inverse Captcha --- #
##################################

import AOCUtils

##################################

raw_digits = AOCUtils.load_input(1)
digits = str(raw_digits)

total_sum = sum(int(digits[i]) for i in range(len(digits)) if digits[i] == digits[i-1])
AOCUtils.print_answer(1, total_sum)

skip = len(digits) // 2

total_sum = sum(int(digits[i]) for i in range(len(digits)) if digits[i] == digits[(i+skip) % len(digits)])
AOCUtils.print_answer(2, total_sum)

AOCUtils.print_time_taken()