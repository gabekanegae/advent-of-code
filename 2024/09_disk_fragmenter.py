##################################
# --- Day 9: Disk Fragmenter --- #
##################################

import AOCUtils

##################################

def get_checksum(data):
    return sum(i * int(c) for i, c in enumerate(data) if c is not None)

##################################

disk_map = str(AOCUtils.load_input(9))

empty_blocks = []
disk = []
file_idx = 0
for i, c in enumerate(disk_map):
    if i % 2 == 0:
        disk += [str(file_idx)] * int(c)
        file_idx += 1
    else:
        for _ in range(int(c)):
            empty_blocks.append(len(disk))
            disk.append(None)

empty_blocks = empty_blocks[::-1]
for i in reversed(range(0, len(disk))):
    if disk[i] is not None and empty_blocks:
        top = empty_blocks.pop()
        if top < i:
            disk[top] = disk[i]
            disk[i] = None
        else:
            break

AOCUtils.print_answer(1, get_checksum(disk))

file_blocks = []
empty_blocks = []
disk = []
file_idx = 0
for i, c in enumerate(disk_map):
    if i % 2 == 0:
        file_blocks.append([file_idx, int(c), len(disk)])
        disk += [str(file_idx)] * int(c)
        file_idx += 1
    else:
        empty_blocks.append([len(disk), int(c)])
        disk += [None] * int(c)

INF = len(disk) * 2
for file_idx, file_size, file_pos in file_blocks[::-1]:
    min_empty = INF
    for i in range(len(empty_blocks)):
        empty_pos, empty_size = empty_blocks[i]
        if empty_size >= file_size and (min_empty == INF or empty_pos < empty_blocks[min_empty][0]):
            min_empty = i

    if min_empty != INF and empty_blocks[min_empty][0] < file_pos:
        for d in range(file_size):
            disk[file_pos+d] = None
            disk[empty_blocks[min_empty][0]+d] = file_idx
        empty_blocks.append([empty_blocks[min_empty][0]+file_size, empty_blocks[min_empty][1]-file_size])
        empty_blocks[min_empty][1] = 0

AOCUtils.print_answer(2, get_checksum(disk))

AOCUtils.print_time_taken()