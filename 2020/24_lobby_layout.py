################################
# --- Day 24: Lobby Layout --- #
################################

import AOCUtils

def split_tokens(s, tokens):
    tokens = set(tokens)
    
    i = 0
    j = 0
    out = []
    while j < len(s):
        if s[i:j] in tokens:
            out.append(s[i:j])
            i = j
        j += 1
    out.append(s[i:])
    
    return out

# Y axis rotated 30 deg (L/R is W/E)
directions = {'nw': (1, -1), 'w': (0, -1), 'ne': (1, 0),
              'sw': (-1, 0), 'e': (0, 1),  'se': (-1, 1)}

################################

paths = AOCUtils.load_input(24)

black_tiles = set()
for path in paths:
    cur = (0, 0)
    for direction in split_tokens(path, directions.keys()):
        delta = directions[direction]
        cur = (cur[0]+delta[0], cur[1]+delta[1])

    if cur not in black_tiles:
        black_tiles.add(cur)
    else:
        black_tiles.remove(cur)

AOCUtils.print_answer(1, len(black_tiles))

for _ in range(100):
    to_be_updated = set(black_tiles)
    for tile in black_tiles:
        for delta in directions.values():
            neighbor = (tile[0]+delta[0], tile[1]+delta[1])
            to_be_updated.add(neighbor)

    new_black_tiles = set(black_tiles)
    for tile in to_be_updated:
        black_neighbors = 0
        for delta in directions.values():
            neighbor = (tile[0]+delta[0], tile[1]+delta[1])
            black_neighbors += int(neighbor in black_tiles)

        if tile in black_tiles and (black_neighbors == 0 or black_neighbors > 2):
            new_black_tiles.remove(tile)
        elif tile not in black_tiles and black_neighbors == 2:
            new_black_tiles.add(tile)

    black_tiles = new_black_tiles

AOCUtils.print_answer(2, len(black_tiles))

AOCUtils.print_time_taken()