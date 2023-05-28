######################################
# --- Day 21: RPG Simulator 20XX --- #
######################################

import AOCUtils
from itertools import combinations, product

def battle(player_hp, player_damage, player_armor, boss_hp, boss_damage, boss_armor):
    player_hits = boss_hp / max(1, player_damage - boss_armor)
    boss_hits = player_hp / max(1, boss_damage - player_armor)
    
    return (player_hits <= boss_hits)

######################################

boss_stats = AOCUtils.load_input(21)

boss_hp, boss_damage, boss_armor = [int(s.split()[-1]) for s in boss_stats]
player_hp = 100

# Cost, Damage, Armor
weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
armor = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
rings = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

weapon_picks = []
for i in range(1, 1+1):
    weapon_picks += combinations(weapons, i)

armor_picks = []
for i in range(0, 1+1):
    armor_picks += combinations(armor, i)

ring_picks = []
for i in range(0, 2+1):
    ring_picks += combinations(rings, i)

setups = []
for picks in product(weapon_picks, armor_picks, ring_picks):
    gold_spent, player_damage, player_armor = 0, 0, 0
    for pick in picks:
        for equip in pick:
            gold_spent += equip[0]
            player_damage += equip[1]
            player_armor += equip[2]

    setups.append((gold_spent, player_damage, player_armor))

setups.sort()

for gold_spent, player_damage, player_armor in setups:
    if battle(player_hp, player_damage, player_armor, boss_hp, boss_damage, boss_armor):
        AOCUtils.print_answer(1, gold_spent)
        break

for gold_spent, player_damage, player_armor in reversed(setups):
    if not battle(player_hp, player_damage, player_armor, boss_hp, boss_damage, boss_armor):
        AOCUtils.print_answer(2, gold_spent)
        break

AOCUtils.print_time_taken()