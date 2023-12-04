###########################################
# --- Day 3: Squares With Three Sides --- #
###########################################

import AOCUtils

def is_triangle(t):
    a, b, c = t

    if b + c <= a: return False
    if a + c <= b: return False
    if a + b <= c: return False

    return True

###########################################

raw_triangles = AOCUtils.load_input(3)
triangles = [[int(s.strip()) for s in t.split()] for t in raw_triangles]

triangle_count = sum(map(is_triangle, triangles))
AOCUtils.print_answer(1, triangle_count)

col_triangles = []
for i in range(0, len(triangles), 3):
    for j in range(3):
        triangle = [triangles[i][j], triangles[i+1][j], triangles[i+2][j]]
        col_triangles.append(triangle)

triangle_count = sum(map(is_triangle, col_triangles))
AOCUtils.print_answer(2, triangle_count)

AOCUtils.print_time_taken()