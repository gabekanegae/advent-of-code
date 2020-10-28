#########################################
# --- Day 7: Some Assembly Required --- #
#########################################

import AOCUtils

def getWire(commands, wires, wire):
    def get(wire):
        try:
            return int(wire)
        except ValueError:
            pass

        if wire in wires:
            return wires[wire]

        cmd = commands[wire].split()
        if len(cmd) > 1:
            op = cmd[-2]

            if op == "AND":
              out = get(cmd[0]) & get(cmd[2])
            elif op == "OR":
              out = get(cmd[0]) | get(cmd[2])
            elif op == "NOT":
              out = ~get(cmd[1]) & 0xFFFF
            elif op == "LSHIFT":
              out = get(cmd[0]) << get(cmd[2])
            elif op == "RSHIFT":
              out = get(cmd[0]) >> get(cmd[2])
        else:
            out = get(cmd[0])

        wires[wire] = out
        return wires[wire]

    return get(wire)

#########################################

rawCommands = AOCUtils.loadInput(7)

commands = dict()
for cmd in rawCommands:
    op, out = cmd.split(" -> ")
    commands[out] = op

wires = dict()
p1 = getWire(commands, wires, "a")

print("Part 1: {}".format(p1))

wires = {"b": p1}
p2 = getWire(commands, wires, "a")

print("Part 1: {}".format(p2))

AOCUtils.printTimeTaken()