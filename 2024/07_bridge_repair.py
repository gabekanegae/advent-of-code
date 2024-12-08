################################
# --- Day 7: Bridge Repair --- #
################################

import AOCUtils
from itertools import product

################################

def get_valid_result(equation, operators):
    result, values = equation

    for ops in product(operators, repeat=len(values)-1):
        test_result = values[0]
        for i, value in enumerate(values[1:]):
            if ops[i] == '+':
                test_result += value
            elif ops[i] == '*':
                test_result *= value
            elif ops[i] == '|':
                test_result = int(str(test_result) + str(value))

        if test_result == result:
            return result

    return 0

################################

raw_equations = [list(map(int, l.replace(':', '').split())) for l in AOCUtils.load_input(7)]
equations = {(l[0], tuple(l[1:])) for l in raw_equations}

valid_count_1 = sum(get_valid_result(equation, '+*') for equation in equations)
AOCUtils.print_answer(1, valid_count_1)

valid_count_2 = sum(get_valid_result(equation, '+*|') for equation in equations)
AOCUtils.print_answer(2, valid_count_2)

AOCUtils.print_time_taken()
