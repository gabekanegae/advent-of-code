###################################
# --- Day 25: Full of Hot Air --- #
###################################

from math import log, ceil
import AOCUtils

positive_digits = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
negative_digits = {k: -v for k, v in list(positive_digits.items())[::-1]}

def snafu_to_number(snafu, digits):
    return sum(digits[c] * (5 ** i) for i, c in enumerate(reversed(snafu)))

def number_to_snafu(number):
    if number == 0: return '0'

    # Properly handle negative numbers, even
    # though it's probably not in any inputs :)
    digits = positive_digits if number > 0 else negative_digits
    number = abs(number)

    snafu_digits = list(digits.keys())
    
    power = ceil(log(number, 5)) + 1 # +1 because most significant digit can be = or -
    snafu = list(snafu_digits[0] * power)

    for p in range(power):
        for i in range(1, 5):
            snafu[p] = snafu_digits[i]
            if snafu_to_number(snafu, digits) < number:
                snafu[p] = snafu_digits[i-1]
                break

    return ''.join(snafu).lstrip('0')

###################################

snafus = AOCUtils.load_input(25)

total_sum = sum(snafu_to_number(snafu, positive_digits) for snafu in snafus)

AOCUtils.print_answer(1, number_to_snafu(total_sum))

AOCUtils.print_time_taken()