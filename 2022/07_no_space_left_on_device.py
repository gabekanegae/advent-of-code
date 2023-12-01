##########################################
# --- Day 7: No Space Left On Device --- #
##########################################

import AOCUtils
from collections import deque

class Node:
    def __init__(self, parent, name, size=None):
        self.parent = parent
        self.children = []
        self.name = name
        self.is_file = size is not None

        self._size = size

    @property
    def size(self):
        if self.is_file: return self._size

        return sum(child.size for child in self.children)

##########################################

log = AOCUtils.load_input(7)

assert log[0] == '$ cd /'
tree = Node(None, name='/')

p = 1
cur = tree
while p < len(log):
    if log[p].startswith('$ cd'):
        new_dir = log[p].split()[2]
        
        if new_dir == '..':
            cur = cur.parent
        else:
            new = Node(cur, new_dir)
            cur.children.append(new)
            cur = new

        p += 1
    elif log[p].startswith('$ ls'):
        p += 1
        
        while p < len(log) and not log[p].startswith('$'):
            a, b = log[p].split()

            new = Node(cur, b, size=int(a)) if a.isnumeric() else Node(cur, b)
            cur.children.append(new)
            p += 1

dir_sizes = []
queue = deque([tree])
while queue:
    cur = queue.popleft()
    
    if not cur.is_file:
        t = cur.size
        dir_sizes.append(t)

    for child in cur.children:
        queue.append(child)

total_size_small_dirs = sum(size for size in dir_sizes if size <= 100000)
AOCUtils.print_answer(1, total_size_small_dirs)

total_disk_space = 70000000
free_space_needed = 30000000
min_to_be_deleted = tree.size + free_space_needed - total_disk_space

for size in sorted(dir_sizes):
    if size >= min_to_be_deleted:
        deleted_dir_size = size
        break

AOCUtils.print_answer(2, deleted_dir_size)

AOCUtils.print_time_taken()