###################################
# --- Day 10: The Stars Align --- #
###################################

import AOCUtils

def getMinMax(a):
    minValue, maxValue = a[0], a[0]
    for e in a[1:]:
        if e < minValue: minValue = e
        if e > maxValue: maxValue = e
    return  minValue, maxValue

def boundingBox(px, py):
    minpx, maxpx = getMinMax(px)
    minpy, maxpy = getMinMax(py)
    return (maxpx - minpx) + (maxpy - minpy)

###################################

rawStars = AOCUtils.loadInput(10)

starsAmt = len(rawStars)
px, py, vx, vy = [], [], [], []
for star in rawStars:
    pxi, pyi = [int(x) for x in star.split("<")[1].split(">")[0].split(",")]
    vxi, vyi = [int(x) for x in star.split("<")[2].split(">")[0].split(",")]
    px.append(pxi)
    py.append(pyi)
    vx.append(vxi)
    vy.append(vyi)

time = 0
while True:
    bBox = boundingBox(px, py)

    for i in range(starsAmt):
        px[i] += vx[i]
        py[i] += vy[i]

    if boundingBox(px, py) > bBox:
        for i in range(starsAmt):
            px[i] -= vx[i]
            py[i] -= vy[i]
        break
    time += 1

print("Part 1:")
stars = set(zip(px, py))
minpx, maxpx = getMinMax(px)
minpy, maxpy = getMinMax(py)
for j in range(minpy, maxpy+1):
    for i in range(minpx, maxpx+1):
        if (i, j) in stars:
            print("#", end="")
        else:
            print(".", end="")
    print()

print("Part 2: {}".format(time))

AOCUtils.printTimeTaken()