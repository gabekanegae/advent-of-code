
################################
# --- Day 13: Care Package --- #
################################

import AOCUtils
from intcodeVM import VM

def draw_screen(blocks):
    block_arts = [' ', '#', 'X', '-', '*']

    for y in range(20):
        for x in range(50):
            if (x, y) in blocks:
                block = blocks[(x, y)]
            else:
                block = 0
            print(block_arts[block]*2, end='')
        print()

    print('Score: {}'.format(score))
    # input()

################################

raw_program = AOCUtils.load_input(13)
memory = list(map(int, raw_program.split(',')))

vm = VM(memory)
vm.run()

block_amount = vm.output[2:len(vm.output):3].count(2)
AOCUtils.print_answer(1, block_amount)

movement = 0
score = 0
blocks = dict()
ball_pos, paddle_pos = None, None

vm = VM(memory)
vm[0] = 2

while not vm.halted:
    vm.run(movement)

    # Parse screen data
    for i in range(0, len(vm.output), 3):
        pos = (vm.output[i], vm.output[i+1])
        block = vm.output[i+2]
        
        # Get ball and paddle positions
        if pos[0] >= 0 and pos[1] >= 0:
            if block == 3:
                ball_pos = pos
            elif block == 4:
                paddle_pos = pos
            blocks[pos] = block

        # Get score
        if pos == (-1, 0):
            score = block

    # Clear parsed data
    vm.output = []

    # Paddle AI
    if ball_pos[0] < paddle_pos[0]:
        movement = 1
    elif ball_pos[0] > paddle_pos[0]:
        movement = -1
    else:
        movement = 0

    # draw_screen(blocks)

AOCUtils.print_answer(2, score)

AOCUtils.print_time_taken()