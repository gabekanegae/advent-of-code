#####################################
# --- Day 13: Mine Cart Madness --- #
#####################################

import AOCUtils

class Track:
    def __init__(self, track):
        self.track = [list(t) for t in track]
        self.size_x, self.size_y = len(track[0]), len(track)
        self.carts = []
        self.crashes = []
        self.tick_count = 0

    # def __repr__(self):
    #     track = [t[:] for t in self.track]
    #     for c in self.carts: track[c.y][c.x] = c.facing
    #     return '\n'.join(''.join(t) for t in track)

    def add_cart(self, y, x, facing):
        self.carts.append(Cart(y, x, facing))

    def tick(self):
        self.tick_count += 1
        self.carts = sorted(self.carts, key=lambda p: [p.y, p.x])

        for i, c in enumerate(self.carts):
            if c.dead: continue

            nxt_x, nxt_y = c.move()
            c.updateState(self.track[nxt_y][nxt_x])
            
            for j, c2 in enumerate(self.carts):
                if c2.dead: continue
                if i != j and (c.x, c.y) == (c2.x, c2.y):
                    c.dead = True
                    c2.dead = True
                    self.crashes.append((c.x, c.y))
                    # print('Crash @ {},{} (tick {})'.format(c.x, c.y, self.tick_count))

        self.carts = [c for c in self.carts if not c.dead]

class Cart:
    def __init__(self, y, x, facing):
        self.x, self.y = x, y
        self.facing = facing
        self.turn = 0
        self.dead = False

    def __repr__(self): return '{},{}'.format(self.x, self.y)

    def move(self):
        if self.facing == '>': self.x += 1
        elif self.facing == '<': self.x -= 1
        elif self.facing == 'v': self.y += 1
        elif self.facing == '^': self.y -= 1
        return self.x, self.y

    def updateState(self, nxt):
        if self.facing == '>':
            if nxt == '/': self.facing = '^'
            elif nxt == '\\': self.facing = 'v'
            elif nxt == '+':
                if self.turn == 0: self.facing = '^'
                elif self.turn == 2: self.facing = 'v'
                self.turn = (self.turn+1) % 3
        elif self.facing == '<':
            if nxt == '/': self.facing = 'v'
            elif nxt == '\\': self.facing = '^'
            elif nxt == '+':
                if self.turn == 0: self.facing = 'v'
                elif self.turn == 2: self.facing = '^'
                self.turn = (self.turn+1) % 3
        elif self.facing == 'v':
            if nxt == '/': self.facing = '<'
            elif nxt == '\\': self.facing = '>'
            elif nxt == '+':
                if self.turn == 0: self.facing = '>'
                elif self.turn == 2: self.facing = '<'
                self.turn = (self.turn+1) % 3
        elif self.facing == '^':
            if nxt == '/': self.facing = '>'
            elif nxt == '\\': self.facing = '<'
            elif nxt == '+':
                if self.turn == 0: self.facing = '<'
                elif self.turn == 2: self.facing = '>'
                self.turn = (self.turn+1) % 3

#####################################

track = Track(AOCUtils.load_input(13))

for y in range(track.size_y):
    for x in range(track.size_x):
        if track.track[y][x] in '<v>^':
            track.add_cart(y, x, track.track[y][x])
            if track.track[y][x] in '<>':
                track.track[y][x] = '-'
            elif track.track[y][x] in 'v^':
                track.track[y][x] = '|'

while len(track.carts) > 1:
    track.tick()

px, py = track.crashes[0]
AOCUtils.print_answer(1, f'{px},{py}')

AOCUtils.print_answer(2, track.carts[0])

AOCUtils.print_time_taken()