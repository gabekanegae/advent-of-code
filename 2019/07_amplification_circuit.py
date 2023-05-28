########################################
# --- Day 7: Amplification Circuit --- #
########################################

import AOCUtils
from intcodeVM import VM
from itertools import permutations

########################################

raw_program = AOCUtils.load_input(7)
memory = [int(i) for i in raw_program.split(',')]

thruster_signals = dict()
for phase in permutations([0, 1, 2, 3, 4]):
    signal = 0
    for i in range(5):
        vm = VM(memory)
        vm.run([phase[i], signal])
        signal = vm.output[0]

    thruster_signals[phase] = signal

AOCUtils.print_answer(1, max(thruster_signals.values()))

thruster_signals = dict()
for phase in permutations([5, 6, 7, 8, 9]):
    vms = [VM(memory) for _ in range(5)]
    vm_outputs = [0 for _ in range(5)]

    for i in range(5): # Send phase setting, does not expect any output
        vms[i].run(phase[i])

    while not any(vm.halted for vm in vms):
        for i in range(5): # Run each of the amps in order
            vms[i].run(vm_outputs[(i-1)%5])
            signal = vms[i].output[-1]
            vm_outputs[i] = signal

    thruster_signals[phase] = signal

AOCUtils.print_answer(2, max(thruster_signals.values()))

AOCUtils.print_time_taken()