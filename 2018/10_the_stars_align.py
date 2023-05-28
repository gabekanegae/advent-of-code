###################################
# --- Day 10: The Stars Align --- #
###################################

import AOCUtils

def get_min_max(a):
    min_value, max_value = a[0], a[0]
    for e in a[1:]:
        if e < min_value: min_value = e
        if e > max_value: max_value = e
    return  min_value, max_value

def bounding_box(px, py):
    min_px, max_px = get_min_max(px)
    min_py, max_py = get_min_max(py)
    return (max_px - min_px) + (max_py - min_py)

###################################

rawStars = AOCUtils.load_input(10)

starsAmt = len(rawStars)
px, py, vx, vy = [], [], [], []
for star in rawStars:
    px_i, py_i = [int(x) for x in star.split('<')[1].split('>')[0].split(',')]
    vx_i, vy_i = [int(x) for x in star.split('<')[2].split('>')[0].split(',')]
    px.append(px_i)
    py.append(py_i)
    vx.append(vx_i)
    vy.append(vy_i)

time = 0
while True:
    bBox = bounding_box(px, py)

    for i in range(starsAmt):
        px[i] += vx[i]
        py[i] += vy[i]

    if bounding_box(px, py) > bBox:
        for i in range(starsAmt):
            px[i] -= vx[i]
            py[i] -= vy[i]
        break
    time += 1

stars = set(zip(px, py))

min_px, max_px = get_min_max(px)
min_py, max_py = get_min_max(py)

stars_image = []
for j in range(min_py, max_py+1):
    l = [(i, j) in stars for i in range(min_px, max_px+1)]
    stars_image.append(l)

AOCUtils.print_answer(1, stars_image)

AOCUtils.print_answer(2, time)

AOCUtils.print_time_taken()