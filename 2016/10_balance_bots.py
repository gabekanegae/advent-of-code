################################
# --- Day 10: Balance Bots --- #
################################

import AOCUtils

class Bot:
    def __init__(self):
        self.chips = []
        self.low_type, self.low_id = None, None
        self.high_type, self.high_id = None, None

################################

instructions = AOCUtils.load_input(10)

bots = dict()
for inst in instructions:
    inst = inst.split()

    if inst[0] == 'bot':
        bot_id = int(inst[1])
        if bot_id not in bots:
            bots[bot_id] = Bot()
        
        bots[bot_id].low_type = inst[5]
        bots[bot_id].low_id = int(inst[6])
        bots[bot_id].high_type = inst[10]
        bots[bot_id].high_id = int(inst[11])
    elif inst[0] == 'value':
        bot_id = int(inst[5])
        if bot_id not in bots:
            bots[bot_id] = Bot()

        chip = int(inst[1])
        bots[bot_id].chips.append(chip)

output = dict()

active_bots = [bot_id for bot_id, bot in bots.items() if len(bot.chips) == 2]
while active_bots:
    bot_id = active_bots.pop()
    bot = bots[bot_id]

    low_chip, high_chip = sorted(bot.chips)
    if [low_chip, high_chip] == [17, 61]:
        p1 = bot_id

    low = (bot.low_type, bot.low_id, low_chip)
    high = (bot.high_type, bot.high_id, high_chip)
    for target_type, target_id, chip in [low, high]:
        if target_type == 'bot':
            bots[target_id].chips.append(chip)
        elif target_type == 'output':
            output[target_id] = chip

        if target_type == 'bot' and len(bots[target_id].chips) == 2:
            active_bots.append(target_id)

    bot.chips = []

AOCUtils.print_answer(1, p1)

p2 = output[0] * output[1] * output[2]
AOCUtils.print_answer(2, p2)

AOCUtils.print_time_taken()