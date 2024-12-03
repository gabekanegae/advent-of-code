####################################
# --- Day 2: Red-Nosed Reports --- #
####################################

import AOCUtils

####################################

def is_report_safe(report):
    return any(all((a - b) * tone in [1, 2, 3] for a, b in zip(report, report[1:])) for tone in [1, -1])

def is_report_safe_with_tolerance(report):
    for tone in [1, -1]:
        for i in range(len(report)-1):
            j = i+1

            if (report[j] - report[i]) * tone not in [1, 2, 3]:
                if is_report_safe(report[:i] + report[i+1:]) or is_report_safe(report[:j] + report[j+1:]):
                    return True
                else:
                    # Check other tone
                    break

    return False

####################################

raw_reports = AOCUtils.load_input(2)
reports = [list(map(int, r.split())) for r in raw_reports]

AOCUtils.print_answer(1, sum(map(is_report_safe, reports)))

AOCUtils.print_answer(2, sum(map(is_report_safe_with_tolerance, reports)))

AOCUtils.print_time_taken()
