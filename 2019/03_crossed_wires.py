################################
# --- Day 3: Crossed Wires --- #
################################

import AOCUtils

################################

wires = [w.split(',') for w in AOCUtils.load_input(3)]

wire_paths = [set() for _ in wires]
wire_paths_length = [dict() for _ in wires]

moves = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

for w, wire in enumerate(wires):
    pos = (0, 0)
    steps_count = 0
    for step in wire:
        direction, distance = step[0], int(step[1:])
        for i in range(distance):
            m = moves[direction]
            pos = (pos[0]+m[0], pos[1]+m[1])

            wire_paths[w].add(pos)

            # Add step count for Part 2
            steps_count += 1
            if pos not in wire_paths_length[w]:
                wire_paths_length[w][pos] = steps_count
            wire_paths_length[w][pos] = min(wire_paths_length[w][pos], steps_count)

intersections = set.intersection(*wire_paths)

# Calculate Manhattan distance for every intersection and take min
distances = [abs(p[0]) + abs(p[1]) for p in intersections]

AOCUtils.print_answer(1, min(distances))

# Calculate distance sum to every intersection and take min
intersections_steps = [sum(wl[i] for wl in wire_paths_length) for i in intersections]

AOCUtils.print_answer(2, min(intersections_steps))

AOCUtils.print_time_taken()