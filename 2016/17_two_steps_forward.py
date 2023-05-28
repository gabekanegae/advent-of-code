#####################################
# --- Day 17: Two Steps Forward --- #
#####################################

import AOCUtils
import hashlib
from collections import deque

#####################################

passcode = AOCUtils.load_input(17)

base_digest = hashlib.md5(passcode.encode())

moves = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
end = (3, 3)

min_path = None
max_path_len = 0

queue = deque([((0, 0), [])])
while queue:
    cur, path = queue.popleft()

    if cur == end:
        min_path = min_path or ''.join(path)
        max_path_len = max(max_path_len, len(path))
        continue

    digest = base_digest.copy()
    digest.update(''.join(path).encode())
    s = digest.hexdigest()

    for i, (p, d) in enumerate(moves.items()):
        if int(s[i], 16) > 10: # bcdef
            nxt = (cur[0]+d[0], cur[1]+d[1])
            if 0 <= nxt[0] <= 3 and 0 <= nxt[1] <= 3:
                queue.append((nxt, path+[p]))

AOCUtils.print_answer(1, min_path)

AOCUtils.print_answer(2, max_path_len)

AOCUtils.print_time_taken()