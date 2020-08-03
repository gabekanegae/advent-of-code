################################
# --- Day 10: Balance Bots --- #
################################

import AOCUtils

class Bot:
    def __init__(self):
        self.chips = []
        self.lowType, self.lowID = None, None
        self.highType, self.highID = None, None

################################

instructions = AOCUtils.loadInput(10)

bots = dict()
for inst in instructions:
    inst = inst.split()

    if inst[0] == "bot":
        botID = int(inst[1])
        if botID not in bots:
            bots[botID] = Bot()
        
        bots[botID].lowType = inst[5]
        bots[botID].lowID = int(inst[6])
        bots[botID].highType = inst[10]
        bots[botID].highID = int(inst[11])
    elif inst[0] == "value":
        botID = int(inst[5])
        if botID not in bots:
            bots[botID] = Bot()

        chip = int(inst[1])
        bots[botID].chips.append(chip)

output = dict()

activeBots = [botID for botID, bot in bots.items() if len(bot.chips) == 2]
while activeBots:
    botID = activeBots.pop()
    bot = bots[botID]

    lowChip, highChip = sorted(bot.chips)
    if [lowChip, highChip] == [17, 61]:
        p1 = botID

    low = (bot.lowType, bot.lowID, lowChip)
    high = (bot.highType, bot.highID, highChip)
    for tgtType, tgtID, chip in [low, high]:
        if tgtType == "bot":
            bots[tgtID].chips.append(chip)
        elif tgtType == "output":
            output[tgtID] = chip

        if tgtType == "bot" and len(bots[tgtID].chips) == 2:
            activeBots.append(tgtID)

    bot.chips = []

print("Part 1: {}".format(p1))

p2 = output[0] * output[1] * output[2]
print("Part 2: {}".format(p2))

AOCUtils.printTimeTaken()