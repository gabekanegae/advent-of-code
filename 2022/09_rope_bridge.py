##############################
# --- Day 9: Rope Bridge --- #
##############################

import AOCUtils

motion_delta = {
    'U': (-1, 0),
    'D': ( 1, 0),
    'L': (0, -1),
    'R': (0,  1)
}

def move(knots, direction):
    # Move head
    delta = motion_delta[direction]
    knots[0] = (knots[0][0] + delta[0], knots[0][1] + delta[1])

    # Move each knot (tail) based on previous knot (head)
    for i in range(1, len(knots)):
        (h_x, h_y), (t_x, t_y) = knots[i-1], knots[i]

        if abs(t_x - h_x) == 2 or abs(t_y - h_y) == 2:
            # Move knot's x component
            if t_x < h_x:
                t_x += 1
            elif t_x > h_x:
                t_x -= 1

            # Move knot's y component            
            if t_y < h_y:
                t_y += 1
            elif t_y > h_y:
                t_y -= 1

        knots[i] = (t_x, t_y)

    return knots

def simulate(motions, knot_amount):
    knots = [(0, 0) for _ in range(knot_amount)]
    visited = set([(0, 0)])

    for direction, distance in motions:
        for _ in range(distance):
            knots = move(knots, direction)
            visited.add(knots[-1])

    return len(visited)

##############################

raw_motions = AOCUtils.load_input(9)
motions = [(l.split()[0], int(l.split()[1])) for l in raw_motions]

AOCUtils.print_answer(1, simulate(motions, 2))

AOCUtils.print_answer(2, simulate(motions, 10))

AOCUtils.print_time_taken()