###############################
# --- Day 21: Fractal Art --- #
###############################

import AOCUtils

class Image:
    def __init__(self, s):
        self.s = s.split('/')

    def update(self, rules):
        size = len(self.s)
        sub_size = 2 if size % 2 == 0 else 3

        # Split s into subsquares
        squares = []
        for x in range(0, size, sub_size):
            sq = []
            for y in range(0, size, sub_size):
                row = []
                for i in range(sub_size):
                    c = []
                    for j in range(sub_size):
                        c.append(self.s[x+i][y+j])
                    row.append(c)
                sq.append(row)
            squares.append(sq)

        # Apply rules to subsquares
        square_amount = len(squares)
        for i in range(square_amount):
            for j in range(square_amount):
                size = len(squares[i][j])

                # Generate all 4 rotations
                rots = [squares[i][j]]
                for _ in range(3):
                    rot = []
                    for y in range(size):
                        r = []
                        for x in range(size)[::-1]:
                            r.append(rots[-1][x][y])
                        rot.append(r)
                    rots.append(rot)

                # Flip all 4 rotated squares
                flips = [[row[:][::-1] for row in rot] for rot in rots]

                # Apply rule if any transformation match
                transformations = rots + flips
                for t in transformations:
                    t = '/'.join(''.join(r) for r in t)
                    if t in rules:
                        squares[i][j] = rules[t].split('/')
                        break

        # Join subsquares into s
        if square_amount == 1:
            self.s = squares[0][0]
        else:
            size = len(squares[0][0])
            self.s = []
            for x in range(square_amount):
                for z in range(size):
                    sq = []
                    for y in range(square_amount):
                        sq.append(squares[x][y][z])
                    self.s.append(''.join(sq))

###############################

raw_rules = AOCUtils.load_input(21)
raw_rules = [s.split(' => ') for s in raw_rules]
rules = {a: b for a, b in raw_rules}

start = '.#./..#/###'

image = Image(start)
for i in range(5):
    image.update(rules)

AOCUtils.print_answer(1, sum(r.count('#') for r in image.s))

image = Image(start)
for _ in range(18):
    image.update(rules)

AOCUtils.print_answer(2, sum(r.count('#') for r in image.s))

AOCUtils.print_time_taken()