OP_READ, OP_WRITE = False, True

class VM:
    def __init__(self, memory, pc=0, base=0):
        self.memory = {k: memory[k] for k in range(len(memory))}
        self.pc = pc
        self.base = base
        self.input_ptr = 0
        self.input_buffer = []
        self.output = []
        self.halted = False

    # Returns a copy of itself (ignoring input and output buffer)
    def copy(self):
        return VM(self.memory.copy(), self.pc, self.base)

    def _parse_mode(self, data, mode, op):
        if op == OP_READ:
            if mode == 0: return self[data]
            elif mode == 1: return data
            elif mode == 2: return self[self.base+data]
        elif op == OP_WRITE:
            if mode == 0: return data
            elif mode == 1: return data
            elif mode == 2: return self.base+data

    def _get_input(self):
        # Read from input_buffer, increment input_ptr
        if self.input_ptr < len(self.input_buffer):
            self.input_ptr += 1
            return self.input_buffer[self.input_ptr-1]

    def __getitem__(self, pos):
        if type(pos) is not int: raise Exception(f'Can\'t access non-int memory address ({pos})')
        if pos < 0: raise Exception(f'Can\'t acess negative memory address ({pos}).')

        if pos not in self.memory:
            self.memory[pos] = 0
        return self.memory[pos]

    def __setitem__(self, pos, data):
        if type(pos) is not int: raise Exception(f'Can\'t access non-int memory address ({pos})')
        if pos < 0: raise Exception(f'Can\'t acess negative memory address ({pos}).')

        self.memory[pos] = data

    def run(self, input_value=None):
        # Load input into input_buffer
        try:
            if type(input_value) is list:
                self.input_buffer += [int(i) for i in input_value]
            elif type(input_value) is str:
                self.input_buffer += [ord(c) for c in input_value]
            elif input_value is not None:
                self.input_buffer.append(int(input_value))
        except:
            raise TypeError('Couldn\'t parse input given.')

        # Run VM
        while self.pc in self.memory:
            param_and_opcode = '{:05}'.format(self[self.pc])
            opcode = int(param_and_opcode[-2:])
            mode_c, mode_b, mode_a = [int(i) for i in param_and_opcode[:3]]

            # Parse parameters according to modes and operation types
            a, b, c = None, None, None
            if opcode in [4, 9]: # out, arb
                a = self._parse_mode(self[self.pc+1], mode_a, OP_READ)
                npc = self.pc+2
            elif opcode in [3]: # in
                a = self._parse_mode(self[self.pc+1], mode_a, OP_WRITE)
                npc = self.pc+2
            elif opcode in [5, 6]: # jit, jif
                a = self._parse_mode(self[self.pc+1], mode_a, OP_READ)
                b = self._parse_mode(self[self.pc+2], mode_b, OP_READ)
                npc = self.pc+3
            elif opcode in [1, 2, 7, 8]: # add, mul, lt, eq
                a = self._parse_mode(self[self.pc+1], mode_a, OP_READ)
                b = self._parse_mode(self[self.pc+2], mode_b, OP_READ)
                c = self._parse_mode(self[self.pc+3], mode_c, OP_WRITE)
                npc = self.pc+4

            # Execute operation
            if opcode == 1: # add
                self[c] = a + b
            elif opcode == 2: # mul
                self[c] = a * b
            elif opcode == 3: # in
                i = self._get_input()
                
                # If no input is buffered, pause execution until some is given
                if i is not None:
                    self[a] = i
                else:
                    return
            elif opcode == 4: # out
                self.output.append(a)
            elif opcode == 5: # jit
                if a != 0: npc = b
            elif opcode == 6: # jif
                if a == 0: npc = b
            elif opcode == 7: # lt
                self[c] = int(a < b)
            elif opcode == 8: # eq
                self[c] = int(a == b)
            elif opcode == 9: # arb
                self.base += a
            elif opcode == 99: # hlt
                break

            # Update PC
            self.pc = npc

        self.halted = True
        return