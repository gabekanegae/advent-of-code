#####################################
# --- Day 13: Mine Cart Madness --- #
#####################################

import AOCUtils

class Track:
    def __init__(self, track):
        self.track = [list(t) for t in track]
        self.sizeX, self.sizeY = len(track[0]), len(track)
        self.carts = []
        self.crashes = []
        self.tickCount = 0

    # def __repr__(self):
    #     track = [t[:] for t in self.track]
    #     for c in self.carts: track[c.y][c.x] = c.facing
    #     return "\n".join(["".join(t) for t in track])

    def addCart(self, y, x, facing):
        self.carts.append(Cart(y, x, facing))

    def tick(self):
        self.tickCount += 1
        self.carts = sorted(self.carts, key=lambda p: [p.y, p.x])

        for i, c in enumerate(self.carts):
            if c.dead: continue

            newx, newy = c.move()
            c.updateState(self.track[newy][newx])
            
            for j, c2 in enumerate(self.carts):
                if c2.dead: continue
                if i != j and (c.x, c.y) == (c2.x, c2.y):
                    c.dead = True
                    c2.dead = True
                    self.crashes.append((c.x, c.y))
                    # print("Crash @ {},{} (tick {})".format(c.x, c.y, self.tickCount))

        self.carts = [c for c in self.carts if not c.dead]

class Cart:
    def __init__(self, y, x, facing):
        self.x, self.y = x, y
        self.facing = facing
        self.turn = 0
        self.dead = False

    def __repr__(self): return "{},{}".format(self.x, self.y)

    def move(self):
        if self.facing == ">": self.x += 1
        elif self.facing == "<": self.x -= 1
        elif self.facing == "v": self.y += 1
        elif self.facing == "^": self.y -= 1
        return self.x, self.y

    def updateState(self, nxt):
        if self.facing == ">":
            if nxt == "/": self.facing = "^"
            elif nxt == "\\": self.facing = "v"
            elif nxt == "+":
                if self.turn == 0: self.facing = "^"
                elif self.turn == 2: self.facing = "v"
                self.turn = (self.turn+1)%3
        elif self.facing == "<":
            if nxt == "/": self.facing = "v"
            elif nxt == "\\": self.facing = "^"
            elif nxt == "+":
                if self.turn == 0: self.facing = "v"
                elif self.turn == 2: self.facing = "^"
                self.turn = (self.turn+1)%3
        elif self.facing == "v":
            if nxt == "/": self.facing = "<"
            elif nxt == "\\": self.facing = ">"
            elif nxt == "+":
                if self.turn == 0: self.facing = ">"
                elif self.turn == 2: self.facing = "<"
                self.turn = (self.turn+1)%3
        elif self.facing == "^":
            if nxt == "/": self.facing = ">"
            elif nxt == "\\": self.facing = "<"
            elif nxt == "+":
                if self.turn == 0: self.facing = "<"
                elif self.turn == 2: self.facing = ">"
                self.turn = (self.turn+1)%3

#####################################

rawTrack = AOCUtils.loadInput(13)
track = Track(rawTrack)

for y in range(track.sizeY):
    for x in range(track.sizeX):
        if track.track[y][x] in "<v>^":
            track.addCart(y, x, track.track[y][x])
            if track.track[y][x] in "<>":
                track.track[y][x] = "-"
            elif track.track[y][x] in "v^":
                track.track[y][x] = "|"

while len(track.carts) > 1:
    track.tick()

px, py = track.crashes[0]
print("Part 1: {},{}".format(px, py))

print("Part 2: {}".format(track.carts[0]))

AOCUtils.printTimeTaken()