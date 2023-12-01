############################
# --- Day 1: Trebuchet --- #
############################

import AOCUtils

numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def get_calibration_value_1(s):
    digits = [c for c in s if c.isnumeric()]
    return int(digits[0] + digits[-1])

def get_calibration_value_2(s):
    max_window = max(len(k) for k in numbers)

    digits = []
    i, j = 0, 1
    while i < len(s):
        if s[i].isnumeric():
            digits.append(s[i])
            i = j
        elif s[i:j] in numbers:
            digits.append(numbers[s[i:j]])
            i += 1
            j = i
        elif j-i == max_window or j > len(s):
            i += 1
            j = i
        
        j += 1

    # print(s, ''.join(digits))
    return int(digits[0] + digits[-1])

############################

document = AOCUtils.load_input(1)

AOCUtils.print_answer(1, sum(map(get_calibration_value_1, document)))

AOCUtils.print_answer(2, sum(map(get_calibration_value_2, document)))

AOCUtils.print_time_taken()
