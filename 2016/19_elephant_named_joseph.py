############################################
# --- Day 19: An Elephant Named Joseph --- #
############################################

import AOCUtils
from collections import deque

def steal_presents(delta):
    # Model a Circular Linked List as two dequeues:
    # left[0] is the current element,
    # and element to be removed is always at the center
    # (left[-1] or right[0], depending on which one's the largest)

    left = deque(range(1, delta+1))
    right = deque(range(delta+1, elf_amount+1))

    while left and right:
        # Remove center element
        if len(left) > len(right):
            left.pop()
        else:
            right.popleft()

        # Rotate right
        right.append(left.popleft())
        left.append(right.popleft())

    return left[0] or right[0]

############################################

elf_amount = AOCUtils.load_input(19)

# class Node:
#     def __init__(self, n):
#         self.n = n
#         self.next = None

# head = Node(1)
# p = head
# for i in range(2, elf_amount+1):
#     p.next = Node(i)
#     p = p.next
# p.next = head

# p = head
# for _ in range(elf_amount):
#     p.next = p.next.next
#     p = p.next

# AOCUtils.print_answer(1, p.n))

# First elf to steal from is +1 from the start
AOCUtils.print_answer(1, steal_presents(1))

# First elf to steal from is +(elf_amount//2) from the start
AOCUtils.print_answer(2, steal_presents(elf_amount // 2))

AOCUtils.print_time_taken()