################################
# --- Day 1: Report Repair --- #
################################

import AOCUtils
from collections import defaultdict

def two_sum(counts, target):
    for i, ct in counts.items():
        if target-i in counts:
            return i * (target-i)

def three_sum(counts, target):
    for i in counts:
        two_sum_result = two_sum(counts, target-i)
        if two_sum_result is not None:
            return i * two_sum_result

################################

report = AOCUtils.load_input(1)

target = 2020

report_counts = defaultdict(int)
for i in report:
    report_counts[i] += 1

AOCUtils.print_answer(1, two_sum(report_counts, target))

AOCUtils.print_answer(2, three_sum(report_counts, target))

AOCUtils.print_time_taken()
