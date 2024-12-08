################################
# --- Day 7: Bridge Repair --- #
################################

import AOCUtils
from math import floor, log

################################

def get_valid_result(equation, part=1):
    result, values = equation

    partial_results = [values[0]]
    for value in values[1:]:
        nxt_partial_results = []
        for partial_result in partial_results:
            sum_result = value + partial_result
            if sum_result <= result:
                nxt_partial_results.append(sum_result)

            mult_result = value * partial_result
            if mult_result <= result:
                nxt_partial_results.append(mult_result)

            concat_result = partial_result * (10 ** (floor(log(value, 10)) + 1)) + value
            if part == 2 and concat_result <= result:
                nxt_partial_results.append(concat_result)
 
        partial_results = nxt_partial_results
 
    for test_result in partial_results:
        if test_result == result:
            return True, test_result
    return False, 0

################################

raw_equations = [list(map(int, l.replace(':', '').split())) for l in AOCUtils.load_input(7)]
equations = {(l[0], tuple(l[1:])) for l in raw_equations}

results_1 = [get_valid_result(equation, part=1) for equation in equations]
results_sum_1 = sum(result for valid, result in results_1 if valid)

AOCUtils.print_answer(1, results_sum_1)

leftover_equations = [equation for equation, (valid, _) in zip(equations, results_1) if not valid]
results_2 = results_1 + [get_valid_result(equation, part=2) for equation in leftover_equations]
results_sum_2 = sum(result for valid, result in results_2 if valid)

AOCUtils.print_answer(2, results_sum_2)

AOCUtils.print_time_taken()
