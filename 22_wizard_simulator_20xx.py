#########################################
# --- Day 22: Wizard Simulator 20XX --- #
#########################################

import AOCUtils
from collections import deque

def battle(playerHp, playerMana, bossHp, bossDamage, spells, part=1):
    # Explore all combinations using a BFS
    start = (playerHp, playerMana, [], bossHp, True, 0)
    queue = deque([start])
    while queue:
        playerHp, playerMana, effects, bossHp, playerTurn, manaSpent = queue.popleft()
        effects = dict(effects)
        # print(f"Current: HP={playerHp} | Mana={playerMana} | Boss={bossHp} | ManaSpent={manaSpent} | Spells={effects}")

        # Boss is dead, end search
        if bossHp <= 0: return manaSpent

        # Player is dead, invalid combination
        if playerHp <= 0: continue

        # Apply all effects
        playerArmor = 0
        for spell in list(effects.keys()):
            playerHp += spells[spell][1]
            playerMana += spells[spell][2]
            playerArmor += spells[spell][3]
            bossHp -= spells[spell][4]

            effects[spell] -= 1
            if effects[spell] == 0:
                effects.pop(spell)

        if playerTurn:
            # "Hard difficulty"
            if part == 2:
                playerHp -= 1
                if playerHp <= 0: continue

            # Add to queue the usage of every spell
            for spell in spells:
                # Ignore spells that have their effects active
                if spell in effects: continue
                
                # Ignore unaffordable spells
                if spells[spell][0] > playerMana: continue

                # Spend mana
                nxtPlayerMana = playerMana - spells[spell][0]
                nxtManaSpent = manaSpent + spells[spell][0]

                if spells[spell][5] == -1: # Instant spells
                    # print(f"    Player used spell '{spell}', instant")
                    nxtEffects = list(effects.items())
                    
                    nxtPlayerHp = playerHp + spells[spell][1]
                    nxtBossHp = bossHp - spells[spell][4]
                else: # Spells with duration (activate starting the next turn)
                    # print(f"    Player used spell '{spell}', only active next turn")
                    effects[spell] = spells[spell][5]
                    nxtEffects = list(effects.items())
                    effects.pop(spell)

                    nxtPlayerHp = playerHp
                    nxtBossHp = bossHp

                # print(f"        Next: HP={nxtPlayerHp} | Mana={nxtPlayerMana} | Boss={nxtBossHp} | ManaSpent={manaSpent} | Spells={effects}")
                nxt = (nxtPlayerHp, nxtPlayerMana, nxtEffects, nxtBossHp, not playerTurn, nxtManaSpent)
                queue.append(nxt)
        else:
            # print("    Boss attacks!")
            nxtEffects = list(effects.items())

            nxtManaSpent = manaSpent
            nxtPlayerHp = playerHp - max(1, bossDamage - playerArmor)
            nxtBossHp = bossHp
            nxtPlayerMana = playerMana

            # print(f"        Next: HP={nxtPlayerHp} | Mana={nxtPlayerMana} | Boss={nxtBossHp} | ManaSpent={manaSpent} | Spells={effects}")
            nxt = (nxtPlayerHp, nxtPlayerMana, nxtEffects, nxtBossHp, not playerTurn, nxtManaSpent)
            queue.append(nxt)

######################################

rawInput = AOCUtils.loadInput(22)

bossHp, bossDamage = [int(s.split()[-1]) for s in rawInput]
playerHp = 50
playerMana = 500

#                          Cost  +HP  +Mana  +Armor  Damage  Duration
spells = {"Magic Missile": ( 53,  0,    0,      0,     4,      -1),
                  "Drain": ( 73,  2,    0,      0,     2,      -1),
                 "Shield": (113,  0,    0,      7,     0,       6),
                 "Poison": (173,  0,    0,      0,     3,       6),
               "Recharge": (229,  0,  101,      0,     0,       5)
         }

print("Part 1: {}".format(battle(playerHp, playerMana, bossHp, bossDamage, spells, part=1)))

print("Part 2: {}".format(battle(playerHp, playerMana, bossHp, bossDamage, spells, part=2)))

AOCUtils.printTimeTaken()