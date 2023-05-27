###############################
# --- Day 21: Fractal Art --- #
###############################

import AOCUtils

class Image:
    def __init__(self, s):
        self.s = s.split("/")

    def update(self, rules):
        size = len(self.s)
        subSize = 2 if size % 2 == 0 else 3

        # Split s into subsquares
        squares = []
        for x in range(0, size, subSize):
            sq = []
            for y in range(0, size, subSize):
                row = []
                for i in range(subSize):
                    c = []
                    for j in range(subSize):
                        c.append(self.s[x+i][y+j])
                    row.append(c)
                sq.append(row)
            squares.append(sq)

        # Apply rules to subsquares
        sqAmt = len(squares)
        for i in range(sqAmt):
            for j in range(sqAmt):
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
                    t = "/".join("".join(r) for r in t)
                    if t in rules:
                        squares[i][j] = rules[t].split("/")
                        break

        # Join subsquares into s
        if sqAmt == 1:
            self.s = squares[0][0]
        else:
            size = len(squares[0][0])
            self.s = []
            for x in range(sqAmt):
                for z in range(size):
                    sq = []
                    for y in range(sqAmt):
                        sq.append(squares[x][y][z])
                    self.s.append("".join(sq))

###############################

rawRules = [s.split(" => ") for s in AOCUtils.loadInput(21)]
rules = {a: b for a, b in rawRules}

start = ".#./..#/###"

image = Image(start)
for i in range(5):
    image.update(rules)

print("Part 1: {}".format(sum(r.count("#") for r in image.s)))

image = Image(start)
for _ in range(18):
    image.update(rules)

print("Part 2: {}".format(sum(r.count("#") for r in image.s)))

AOCUtils.printTimeTaken()