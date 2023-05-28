##################################
# --- Day 5: Binary Boarding --- #
##################################

import AOCUtils

##################################

boarding_passes = AOCUtils.load_input(5)

seat_ids = []
for boarding_pass in boarding_passes:
    lo, hi = 0, (2 ** len(boarding_pass)) - 1
    for c in boarding_pass:
        mid = (lo + hi) // 2
        if c in 'FL':
            hi = mid
        elif c in 'BR':
            lo = mid

    seat_id = hi
    seat_ids.append(seat_id)

AOCUtils.print_answer(1, max(seat_ids))

all_seats = set(range(min(seat_ids), max(seat_ids) + 1))
missing_seats = all_seats - set(seat_ids) # Assume len(missing_seats) == 1

AOCUtils.print_answer(2, missing_seats.pop())

AOCUtils.print_time_taken()