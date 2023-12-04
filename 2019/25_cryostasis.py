##############################
# --- Day 25: Cryostasis --- #
##############################

import AOCUtils
from intcodeVM import VM
from itertools import combinations
from collections import deque

def play_game(memory):
    vm = VM(memory)
    vm.run()
    print(''.join(chr(c) for c in vm.output))
    while not vm.halted:
        vm.output = []
        vm.run(input() + '\n')
        print(''.join(chr(c) for c in vm.output))
    exit()

def opposite_door(direction):
    opp = {'north': 'south', 'south': 'north', 'east': 'west', 'west': 'east'}
    return opp[direction]

##############################

raw_program = AOCUtils.load_input(25)

memory = list(map(int, raw_program.split(',')))

# The game can be played manually by uncommenting the line below:
# play_game(memory)

# Items that can't (shouldn't) be picked up
ignored_items = set(['infinite loop', 'molten lava', 'giant electromagnet', 'photons', 'escape pod'])

vm = VM(memory)
vm.run()

# Store the command list that reaches the final room with the maximum amount of items
final_state = None
max_items_found = 0

# BFS through all rooms, storing (room, inventory) visited states
visited = set()
queue = deque([(set(), [], vm)])
while queue:
    inventory, path, vm = queue.popleft()

    # Save output and clear it
    text = ''.join(chr(c) for c in vm.output)
    vm.output = []

    # Get room name
    room = text.split('==')[1].strip()
    # print(sum(p.split()[0] != 'take' for p in path), room, '-->', sorted(inventory))

    # Ignore if already visited, also marks (room, inventory) as visited
    visit_key = (room, tuple(sorted(inventory)))
    if visit_key in visited: continue
    visited.add(visit_key)

    # Parse room's doors and items
    doors, items = [], []
    doors_start = text.find('Doors here lead:')
    items_start = text.find('Items here:')
    if doors_start != -1:
        doors = [line[2:] for line in text[doors_start:items_start].split('\n') if line.startswith('-')]
    if items_start != -1:
        items = [line[2:] for line in text[items_start:].split('\n') if line.startswith('-')]

    # Pick up all items in the room
    for item in items:
        if item in ignored_items: continue # But ignore the game-ending ones
        path.append('take ' + item)
        vm.run('take ' + item + '\n')
        inventory.add(item)

    # After picking items, mark new (room, inventory) as visited also
    visit_key = (room, tuple(sorted(inventory)))
    visited.add(visit_key)

    # Update maximum amount of items found
    max_items_found = max(max_items_found, len(inventory))
    # If less than that, then as this is a BFS, this pathing missed an item, so ignore it
    if len(inventory) < max_items_found: continue

    # If at final room before floor, save as possible answer and ignore this pathing
    if room == 'Security Checkpoint':
        # Get step to reach floor
        floor_direction = doors[0] if doors[0] != opposite_door(path[-1]) else doors[1]
        final_state = (vm, list(inventory), floor_direction)
        continue

    # Queue all next steps, copying the current VM for each one
    for door in doors:
        new_vm = vm.copy()
        new_vm.run(door + '\n')

        queue.append((set(inventory), path+[door], new_vm))

# Get VM at the checkpoint, list of all safe items and direction of pressure-sensitive floor
vm, all_items, floor_direction = final_state
vm.run('\n'.join('drop '+item for item in all_items) + '\n') # Drop all items

# Generate all possible item combinations by increasing length
item_combinations = []
for n in range(len(all_items)):
    item_combinations += list(combinations(all_items, n))

# Bruteforce the pressure floor by trying all of the combinations 
inventory = set()
too_heavy = []
for attempt_items in item_combinations:
    # print('Trying items: {}'.format(list(attempt_items)))

    # If inventory is a superset of any of too_heavy, then it's also going to be too heavy
    if any(set(s).issubset(set(attempt_items)) for s in too_heavy): continue

    # Drop all items that aren't in attempt_items
    to_drop = [item for item in inventory if item not in attempt_items]
    vm.run('\n'.join('drop '+item for item in to_drop) + '\n')
    inventory = inventory.difference(set(to_drop))

    # Pick up all from attempt_items that aren't yet in inventory
    to_pick_up = [item for item in attempt_items if item not in inventory]
    vm.run('\n'.join('take '+item for item in to_pick_up) + '\n')
    inventory = inventory.union(set(to_pick_up))

    # Activate floor
    vm.run(floor_direction+'\n')

    text = ''.join(chr(c) for c in vm.output)
    vm.output = []

    # Verify result
    if text.find('Alert!') == -1:
        # print(text.split('\n\n')[-1].strip())
        AOCUtils.print_answer(1, text.split()[-8])
        break
    elif text.find('lighter') != -1: # Too heavy, add as invalid subset
        too_heavy.append(attempt_items)

AOCUtils.print_time_taken()