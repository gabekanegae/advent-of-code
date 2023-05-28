##################################
# --- Day 11: Seating System --- #
##################################

import AOCUtils

moves_8 = [(0, 1), (1, 0), (0, -1), (-1, 0),
          (1, 1), (1, -1), (-1, 1), (-1, -1)]

##################################

original_seats = [list(l) for l in AOCUtils.load_input(11)]

seats = [l[:] for l in original_seats]
h, w = len(seats), len(seats[0])

has_changed = True
while has_changed:
    new_seats = [l[:] for l in seats]
    has_changed = False
    for a in range(h):
        for b in range(w):
            n = 0
            for da, db in moves_8:
                if da == 0 and db == 0: continue
                
                if 0 <= a+da < h and 0 <= b+db < w:
                    if seats[a+da][b+db] == '#':
                        n += 1

            if seats[a][b] == 'L' and n == 0:
                new_seats[a][b] = '#'
                has_changed = True
            elif seats[a][b] == '#' and n >= 4:
                new_seats[a][b] = 'L'
                has_changed = True

    seats = new_seats

p1 = sum(l.count('#') for l in seats)
AOCUtils.print_answer(1, p1)

seats = [l[:] for l in original_seats]
h, w = len(seats), len(seats[0])

has_changed = True
while has_changed:
    has_changed = False
    new_seats = [l[:] for l in seats]
    for a in range(h):
        for b in range(w):
            n = 0
            for da, db in moves_8:
                ca, cb = a, b
                while 0 <= ca+da < h and 0 <= cb+db < w:
                    ca += da
                    cb += db

                    if seats[ca][cb] == '#':
                        n += 1

                    if seats[ca][cb] != '.':
                        break

            if seats[a][b] == 'L' and n == 0:
                new_seats[a][b] = '#'
                has_changed = True
            elif seats[a][b] == '#' and n >= 5:
                new_seats[a][b] = 'L'
                has_changed = True

    seats = new_seats

p2 = sum(l.count('#') for l in seats)
AOCUtils.print_answer(2, p2)

AOCUtils.print_time_taken()