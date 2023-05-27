######################################
# --- Day 21: RPG Simulator 20XX --- #
######################################

import AOCUtils
from itertools import combinations, product

def battle(playerHp, playerDamage, playerArmor, bossHp, bossDamage, bossArmor):
    playerHits = bossHp / max(1, playerDamage - bossArmor)
    bossHits = playerHp / max(1, bossDamage - playerArmor)
    
    return (playerHits <= bossHits)

######################################

rawInput = AOCUtils.loadInput(21)

bossHp, bossDamage, bossArmor = [int(s.split()[-1]) for s in rawInput]
playerHp = 100

# Cost, Damage, Armor
weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
armor = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
rings = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

weaponPicks = []
for i in range(1, 1+1):
    weaponPicks += combinations(weapons, i)

armorPicks = []
for i in range(0, 1+1):
    armorPicks += combinations(armor, i)

ringPicks = []
for i in range(0, 2+1):
    ringPicks += combinations(rings, i)

setups = []
for picks in product(weaponPicks, armorPicks, ringPicks):
    goldSpent, playerDamage, playerArmor = 0, 0, 0
    for pick in picks:
        for equip in pick:
            goldSpent += equip[0]
            playerDamage += equip[1]
            playerArmor += equip[2]

    setups.append((goldSpent, playerDamage, playerArmor))

setups.sort()

for goldSpent, playerDamage, playerArmor in setups:
    if battle(playerHp, playerDamage, playerArmor, bossHp, bossDamage, bossArmor):
        print("Part 1: {}".format(goldSpent))
        break

for goldSpent, playerDamage, playerArmor in reversed(setups):
    if not battle(playerHp, playerDamage, playerArmor, bossHp, bossDamage, bossArmor):
        print("Part 2: {}".format(goldSpent))
        break

AOCUtils.printTimeTaken()