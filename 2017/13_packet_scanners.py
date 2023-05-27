###################################
# --- Day 13: Packet Scanners --- #
###################################

import AOCUtils

# def crossFirewall(rawScanners, delay=0):
#     scanners = {int(s[0]): {"range": int(s[1]), "pos": 1, "step": 1} for s in rawScanners}
#
#     severity = []
#
#     maxDepth = max(scanners.keys())
#     for depth in range(-delay, maxDepth+1):
#
#         if depth in scanners and scanners[depth]["pos"] == 1:
#             severity.append(depth * scanners[depth]["range"])
#
#         for s in scanners:
#             scanner = scanners[s]
#             scanner["pos"] += scanner["step"]
#             if scanner["pos"] in [1, scanner["range"]]:
#                 scanner["step"] *= -1
#
#
#     return severity

###################################

rawScanners = [s.split(":") for s in AOCUtils.loadInput(13)]

# print("Part 1: {}".format(sum(crossFirewall(rawScanners))))

scanners = {int(s[0]): {"range": int(s[1]), "pos": 1, "step": 1} for s in rawScanners}

severity = 0
for depth in scanners:
    if depth % ((scanners[depth]["range"]-1) * 2) == 0:
        severity += depth * scanners[depth]["range"]

print("Part 1: {}".format(severity))

delay = 1
while any((depth + delay) % ((scanners[depth]["range"]-1) * 2) == 0 for depth in scanners):
    delay += 1

print("Part 2: {}".format(delay))

AOCUtils.printTimeTaken()