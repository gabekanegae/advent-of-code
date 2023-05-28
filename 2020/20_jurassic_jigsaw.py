###################################
# --- Day 20: Jurassic Jigsaw --- #
###################################

import AOCUtils
from collections import deque

class Tile:
    def __init__(self, tile_id, image):
        self.tile_id = tile_id
        self.image = [list(l) for l in image]

    @property
    def image_without_borders(self):
        return [row[1:-1] for row in self.image[1:-1]]
    
    @property
    def sides(self):
        up = self.image[0]
        down = self.image[-1]
        left = [self.image[i][0] for i in range(len(self.image[0]))]
        right = [self.image[i][-1] for i in range(len(self.image[0]))]

        return {'U': up, 'D': down, 'L': left, 'R': right}

def rot_90_cw(matrix):
    return [list(l) for l in zip(*matrix[::-1])]

def flip_h(matrix):
    return [row[::-1] for row in matrix]

###################################

# Loooots of assumptions made for this one to work. Should be
# good for all test cases, but it's very likely they were
# VERY carefully picked for a bunch of reasons.

raw_tiles = AOCUtils.load_input(20)

raw_tiles = '\n'.join(raw_tiles).split('\n\n')

tiles = dict()
for raw_tile in raw_tiles:
    raw_tile = raw_tile.split('\n')

    tile_id = int(raw_tile[0].split()[1][:-1])
    tile = [l for l in raw_tile[1:] if l] # Input has one extra newline at the end

    tiles[tile_id] = Tile(tile_id, tile)

# Assume tiles have equal sizes and are all squares,
# get size of one of them (doesn't matter which one)
tile_size = len(tiles[list(tiles.keys())[0]].image)

# Build tiles adjacency matrix
tile_connections = dict()
for tile_1_id, tile_1 in tiles.items():
    for tile_2_id, tile_2 in tiles.items():
        if tile_1_id == tile_2_id: continue

        for side_1_direction, side_1 in tile_1.sides.items():
            for side_2_direction, side_2 in tile_2.sides.items():
                if side_1 in [side_2, side_2[::-1]]:
                    if tile_1_id not in tile_connections:
                        tile_connections[tile_1_id] = dict()
                    tile_connections[tile_1_id][side_1_direction] = tile_2_id

# Assume there will be only one possible match/choice/placement for each tile
corner_tiles = [tile_id for tile_id, conns in tile_connections.items() if len(conns) == 2]

p1 = 1
for tile_id in corner_tiles:
    p1 *= tile_id

AOCUtils.print_answer(1, p1)

moves_4 = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}

dirs_opposite = {'D': 'U', 'U': 'D', 'L': 'R', 'R': 'L'}
dirs_rot_90_cw = {'D': 'L', 'U': 'R', 'L': 'U', 'R': 'D'}
dirs_flip_h = {k: (v if k in 'LR' else dirs_opposite[v]) for k, v in dirs_opposite.items()}

# Figure out the correct tile placement (after tiles are
# rotated/flipped), building a `grid` matrix made of tile IDs.
# Assume grid is square (i.e. `len(tiles)` is a perfect square)
grid_size = int(len(tiles) ** 0.5)
grid = [[None for _ in range(grid_size)] for _ in range(grid_size)]

# Pick any corner tile (doesn't matter which, as long
# as `start_pos` is set based on their neighbors)
start_tile = corner_tiles[0]
if all(c in tile_connections[start_tile] for c in 'DR'): # Top-left
    start_pos = (0, 0)
elif all(c in tile_connections[start_tile] for c in 'DL'): # Top-right
    start_pos = (0, len(grid)-1)
elif all(c in tile_connections[start_tile] for c in 'UR'): # Bottom-left
    start_pos = (len(grid)-1, 0)
elif all(c in tile_connections[start_tile] for c in 'UL'): # Bottom-right
    start_pos = (len(grid)-1, len(grid)-1)

# BFS starting from the picked corner until the grid is filled
queue = deque([(start_pos, start_tile)])
tiles_placed = set()
while queue:
    pos, tile = queue.popleft()

    if tile in tiles_placed: continue
    tiles_placed.add(tile)

    grid[pos[0]][pos[1]] = tile

    for direction, adj_tile in tile_connections[tile].items():
        # Loop through all possible rotations/flips until the matching one is found
        # Performing these actions yields all possible versions after each one:
        #   nothing, rot_90_cw, rot_90_cw, rot_90_cw, flip_h, rot_90_cw, rot_90_cw, rot_90_cw 
        # TODO: Can be found directly instead of looping through all 8
        tries = 0
        while tiles[adj_tile].sides[dirs_opposite[direction]] != tiles[tile].sides[direction]:
            if tries == 3:
                tiles[adj_tile].image = flip_h(tiles[adj_tile].image)
                tile_connections[adj_tile] = {dirs_flip_h[k]: v for k, v in tile_connections[adj_tile].items()}
            else:
                tiles[adj_tile].image = rot_90_cw(tiles[adj_tile].image)
                tile_connections[adj_tile] = {dirs_rot_90_cw[k]: v for k, v in tile_connections[adj_tile].items()}
            tries += 1

        delta = moves_4[direction]
        nxt_pos = (pos[0]+delta[0], pos[1]+delta[1])
        queue.append((nxt_pos, adj_tile))

# Merge the tiles row by row
image = []
tile_size_without_border = tile_size - 2
for row_index in range(grid_size * tile_size_without_border):
    grid_column = row_index // tile_size_without_border
    tile_row = row_index % tile_size_without_border

    row = []
    for i in range(grid_size):
        row += tiles[grid[grid_column][i]].image_without_borders[tile_row]
    image.append(row)

# Print matrix of tile IDs
# for i in range(len(grid)): print(grid[i])

# Print final image
# print('\n'.join(''.join(row) for row in image))

# Print image but pretty (with borders, tile IDs and separators)
# for row_index in range(grid_size * tile_size):
#     grid_column = row_index // tile_size
#     tile_row = row_index % tile_size
#     if tile_row == 0:
#         print('-' * grid_size * (tile_size+1))
#         tile_ids = [grid[grid_column][i] for i in range(grid_size)]
#         print('   ' + '       '.join([str(s) for s in tile_ids]))
#     print('|'.join(''.join(tiles[grid[grid_column][i]].image[tile_row]) for i in range(grid_size)))

monster = ['                  # ',
           '#    ##    ##    ###',
           ' #  #  #  #  #  #   ']
monster_roughness = sum(row.count('#') for row in monster)

# Assume the correct rotation/flip will be the only one with any monsters
monsters = 0
tries = 0
# Loop through all possible rotations/flips until a monster is found
while monsters == 0:
    for i in range(len(image) - len(monster) + 1):
        for j in range(len(image[0]) - len(monster[0]) + 1):
            roughness = 0
            # Assume a # can be part of more than one monster (although
            # I'm pretty sure this is not the case in any of the actual inputs)
            for m_i in range(len(monster)):
                for m_j in range(len(monster[0])):
                    if monster[m_i][m_j] == '#' and image[i+m_i][j+m_j] == '#':
                        roughness += 1

            monsters += int(roughness == monster_roughness)

    # Performing these actions yields all possible versions after each one:
    #   nothing, rot_90_cw, rot_90_cw, rot_90_cw, flip_h, rot_90_cw, rot_90_cw, rot_90_cw 
    if tries == 3:
        image = flip_h(image)
    else:
        image = rot_90_cw(image)
    tries += 1

total_roughness = sum(row.count('#') for row in image)
p2 = total_roughness - (monsters * monster_roughness)

AOCUtils.print_answer(2, p2)

AOCUtils.print_time_taken()