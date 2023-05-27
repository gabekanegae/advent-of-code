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

    def _knot(self):
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
            self._knot()

        dense = []
        for i in range(16):
            dense.append(0)
            for j in range(16):
                dense[-1] ^= self.circle[16*i + j]

        return "".join(hex(n)[2:].zfill(2) for n in dense)

#############################

rawInput = AOCUtils.loadInput(10)

s = [int(i) for i in rawInput.split(",")]
print("Part 1: {}".format(KnotHash(s)._knot()))

s = [ord(c) for c in rawInput]
print("Part 2: {}".format(KnotHash(s).hash()))

AOCUtils.printTimeTaken()