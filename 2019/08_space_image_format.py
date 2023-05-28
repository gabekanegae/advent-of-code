#####################################
# --- Day 8: Space Image Format --- #
#####################################

import AOCUtils

#####################################

w, h = 25, 6
image = [int(i) for i in str(AOCUtils.load_input(8))]

layer_amount = len(image) // (w*h)

layers = []
layer_counts = []
for l in range(layer_amount):
    layer = []
    for x in range(h):
        s, e = l*w*h + x*w, l*w*h + (x+1)*w
        layer.append(image[s:e])

    layers.append(layer)

    lc0 = sum(l.count(0) for l in layer)
    lc1 = sum(l.count(1) for l in layer)
    lc2 = sum(l.count(2) for l in layer)
    layer_counts.append((lc0, lc1, lc2))

layer_counts.sort()
checksum = layer_counts[0][1] * layer_counts[0][2]

AOCUtils.print_answer(1, checksum)

image = [[None for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        for layer in layers:
            if image[i][j] is None and layer[i][j] != 2:
                image[i][j] = layer[i][j]

screen = []
for i in range(h):
    l = [image[i][j] == 1 for j in range(w)]
    screen.append(l)

AOCUtils.print_answer(2, screen)

AOCUtils.print_time_taken()