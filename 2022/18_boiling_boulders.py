####################################
# --- Day 18: Boiling Boulders --- #
####################################

import AOCUtils
from collections import deque

deltas = [(0,0,-1), (0,0,1), (0,-1,0), (0,1,0), (-1,0,0), (1,0,0)]

def get_exposed_faces_count(cubes):
    exposed_faces_count = 0
    for cube in cubes:
        for delta in deltas:
            neighbor_cube = (cube[0] + delta[0], cube[1] + delta[1], cube[2] + delta[2])
            if neighbor_cube not in cubes:
                exposed_faces_count += 1

    return exposed_faces_count

####################################

lava_cubes = AOCUtils.load_input(18)

lava_cubes = set(tuple(map(int, cube.split(','))) for cube in lava_cubes)

AOCUtils.print_answer(1, get_exposed_faces_count(lava_cubes))

min_x, max_x = min(x for x, _, _ in lava_cubes), max(x for x, _, _ in lava_cubes)
min_y, max_y = min(y for _, y, _ in lava_cubes), max(y for _, y, _ in lava_cubes)
min_z, max_z = min(z for _, _, z in lava_cubes), max(z for _, _, z in lava_cubes)

air_cubes = set()
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        for z in range(min_z, max_z + 1):
            if (x,y,z) not in lava_cubes:
                air_cubes.add((x,y,z))

internal_air_cubes = set()
unvisited = set(air_cubes)
while unvisited:
    visited = set()
    is_exposed = False

    queue = deque([unvisited.pop()])
    while queue:
        cur = queue.popleft()

        if cur in visited: continue
        visited.add(cur)

        x, y, z = cur
        if not min_x < x < max_x or not min_y < y < max_y or not min_z < z < max_z:
            is_exposed = True
            break

        for delta in deltas:
            neighbor_cube = (cur[0] + delta[0], cur[1] + delta[1], cur[2] + delta[2])
            if neighbor_cube in air_cubes:
                queue.append(neighbor_cube)

    unvisited -= visited
    if not is_exposed:
        internal_air_cubes |= visited

AOCUtils.print_answer(2, get_exposed_faces_count(lava_cubes | internal_air_cubes))

AOCUtils.print_time_taken()