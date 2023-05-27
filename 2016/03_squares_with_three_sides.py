###########################################
# --- Day 3: Squares With Three Sides --- #
###########################################

import AOCUtils

def isTriangle(t):
    a, b, c = t

    if b + c <= a: return False
    if a + c <= b: return False
    if a + b <= c: return False

    return True

###########################################

triangles = AOCUtils.loadInput(3)
triangles = [[int(s.strip()) for s in t.split()] for t in triangles]

triangleAmt = sum(isTriangle(triangle) for triangle in triangles)
print("Part 1: {}".format(triangleAmt))

colTriangles = []
for i in range(0, len(triangles), 3):
    for j in range(3):
        triangle = [triangles[i][j], triangles[i+1][j], triangles[i+2][j]]
        colTriangles.append(triangle)

triangleAmt = sum(isTriangle(triangle) for triangle in colTriangles)
print("Part 2: {}".format(triangleAmt))

AOCUtils.printTimeTaken()