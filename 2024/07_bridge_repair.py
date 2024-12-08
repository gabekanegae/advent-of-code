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

            # Since all operators are strictly increasing (for positive operands),
            # if partial result is larger than expected result, we can break early 
            if test_result > result:
                break

        if test_result == result:
            return True, result

    return False, 0

################################

raw_equations = [list(map(int, l.replace(':', '').split())) for l in AOCUtils.load_input(7)]
equations = {(l[0], tuple(l[1:])) for l in raw_equations}

results_1 = [get_valid_result(equation, '+*') for equation in equations]
results_sum_1 = sum(result for valid, result in results_1 if valid)

AOCUtils.print_answer(1, results_sum_1)

leftover_equations = [equation for equation, (valid, _) in zip(equations, results_1) if not valid]
results_2 = results_1 + [get_valid_result(equation, '+*|') for equation in leftover_equations]
results_sum_2 = sum(result for valid, result in results_2 if valid)

AOCUtils.print_answer(2, results_sum_2)

AOCUtils.print_time_taken()
