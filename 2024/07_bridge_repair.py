################################
# --- Day 7: Bridge Repair --- #
################################

import AOCUtils
from collections import deque
from math import floor, log

################################

def get_valid_result(equation, part=1):
    result, values = equation

    queue = deque([(1, values[0])])
    while queue:
        idx, partial_result = queue.popleft()

        if idx >= len(values):
            if partial_result == result:
                return True, result
            continue

        value = values[idx]

        sum_result = value + partial_result
        if sum_result <= result:
            queue.append((idx+1, sum_result))

        mult_result = value * partial_result
        if mult_result <= result:
            queue.append((idx+1, mult_result))

        concat_result = partial_result * (10 ** (floor(log(value, 10)) + 1)) + value
        if part == 2 and concat_result <= result:
            queue.append((idx+1, concat_result))
 
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
