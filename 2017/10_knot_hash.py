#############################
# --- Day 10: Knot Hash --- #
#############################

import AOCUtils

class KnotHash:
    def __init__(self, lengths):
        self.circle = list(range(256))
        self.lengths = lengths
        self.cur = 0
        self.skip = 0

    def knot(self):
        for length in self.lengths:
            a = (self.cur) % len(self.circle)
            b = (self.cur+length) % len(self.circle)

            if b >= a:
                self.circle[a:b] = self.circle[a:b][::-1]
            else:
                s = (self.circle[a:] + self.circle[:b])[::-1]
                self.circle[a:] = s[:len(self.circle)-a]
                self.circle[:b] = s[len(self.circle)-a:]

            self.cur += length + self.skip
            self.skip += 1

        return self.circle[0] * self.circle[1]

    def hash(self):
        self.lengths += [17, 31, 73, 47, 23]

        for _ in range(64):
            self.knot()

        dense = []
        for i in range(16):
            dense.append(0)
            for j in range(16):
                dense[-1] ^= self.circle[16*i + j]

        return ''.join(hex(n)[2:].zfill(2) for n in dense)

#############################

raw = AOCUtils.load_input(10)

s = [int(i) for i in raw.split(',')]
AOCUtils.print_answer(1, KnotHash(s).knot())

s = [ord(c) for c in raw]
AOCUtils.print_answer(2, KnotHash(s).hash())

AOCUtils.print_time_taken()