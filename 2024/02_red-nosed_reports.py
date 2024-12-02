####################################
# --- Day 2: Red-Nosed Reports --- #
####################################

def is_report_safe(report):
    safety_checks = [
        lambda r: r in [sorted(r), sorted(r, reverse=True)],
        lambda r: all(1 <= abs(a-b) <= 3 for a, b in zip(r, r[1:]))
    ]

    return all(is_safe(report) for is_safe in safety_checks)

def is_report_safe_with_tolerance(report):
    report_variations = [report[:i] + report[i+1:] for i in range(len(report))]

    return any(map(is_report_safe, report_variations))

####################################

import AOCUtils

raw_reports = AOCUtils.load_input(2)

reports = [list(map(int, r.split())) for r in raw_reports]

AOCUtils.print_answer(1, sum(map(is_report_safe, reports)))

AOCUtils.print_answer(2, sum(map(is_report_safe_with_tolerance, reports)))

AOCUtils.print_time_taken()
