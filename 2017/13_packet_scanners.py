###################################
# --- Day 13: Packet Scanners --- #
###################################

import AOCUtils

# def cross_firewall(raw_scanners, delay=0):
#     scanners = {int(s[0]): {'range': int(s[1]), 'pos': 1, 'step': 1} for s in raw_scanners}
#
#     severity = []
#
#     max_depth = max(scanners.keys())
#     for depth in range(-delay, max_depth+1):
#
#         if depth in scanners and scanners[depth]['pos'] == 1:
#             severity.append(depth * scanners[depth]['range'])
#
#         for s in scanners:
#             scanner = scanners[s]
#             scanner['pos'] += scanner['step']
#             if scanner['pos'] in [1, scanner['range']]:
#                 scanner['step'] *= -1
#
#
#     return severity

###################################

raw_scanners = AOCUtils.load_input(13)
raw_scanners = [s.split(':') for s in raw_scanners]

# AOCUtils.print_answer(1, sum(cross_firewall(raw_scanners)))

scanners = {int(s[0]): {'range': int(s[1]), 'pos': 1, 'step': 1} for s in raw_scanners}

severity = 0
for depth in scanners:
    if depth % ((scanners[depth]['range']-1) * 2) == 0:
        severity += depth * scanners[depth]['range']

AOCUtils.print_answer(1, severity)

delay = 1
while any((depth + delay) % ((scanners[depth]['range']-1) * 2) == 0 for depth in scanners):
    delay += 1

AOCUtils.print_answer(2, delay)

AOCUtils.print_time_taken()