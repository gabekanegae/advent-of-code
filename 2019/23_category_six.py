################################
# --- Day 23: Category Six --- #
################################

import AOCUtils
from intcodeVM import VM

################################

raw_program = AOCUtils.load_input(23)
memory = [int(i) for i in raw_program.split(',')]

vms = [VM(memory) for _ in range(50)]
for i, vm in enumerate(vms):
    vm.run(i)

p1_done = False

nat = None
seen = set()

queues = [[] for i in range(50)]
while True:
    idle = True

    for i, vm in enumerate(vms):
        # Receive packets from queue
        if queues[i]:
            idle = False
            vm.run(queues[i])
            queues[i] = [] # Clear queue
        else:
            vm.run(-1)

        # Send packets
        while vm.output:
            idle = False
            dest, x, y = vm.output[:3]
            vm.output = vm.output[3:]
            if dest == 255:
                if not p1_done:
                    AOCUtils.print_answer(1, y)
                    p1_done = True
                
                # Update NAT
                nat = (x, y)
            else:
                queues[dest] += [x, y]

        vm.output = []

    # NAT
    if idle:
        queues[0] += nat
        if nat in seen:
            AOCUtils.print_answer(2, nat[1])
            break
        seen.add(nat)

AOCUtils.print_time_taken()