#########################################
# --- Day 22: Wizard Simulator 20XX --- #
#########################################

import AOCUtils
from heapq import heappush, heappop

def battle(player_hp, player_mana, boss_hp, boss_damage, spells, part=1):
    # Explore all combinations using Dijkstra (i.e. BFS with min-heap instead of queue)
    heap = []
    
    start = (0, player_hp, player_mana, [], boss_hp, True)
    heappush(heap, start)
    while heap:
        mana_spent, player_hp, player_mana, effects, boss_hp, player_turn = heappop(heap)
        effects = dict(effects)
        # print(f'Current: ManaSpent={mana_spent} | HP={player_hp} | Mana={player_mana} | Boss={boss_hp} | Spells={effects}')

        # Boss is dead, end search
        if boss_hp <= 0: return mana_spent

        # Player is dead, invalid combination
        if player_hp <= 0: continue

        # Apply all effects
        player_armor = 0
        for spell in list(effects.keys()):
            player_hp += spells[spell][1]
            player_mana += spells[spell][2]
            player_armor += spells[spell][3]
            boss_hp -= spells[spell][4]

            effects[spell] -= 1
            if effects[spell] == 0:
                effects.pop(spell)

        if player_turn:
            # 'Hard difficulty'
            if part == 2:
                player_hp -= 1
                if player_hp <= 0: continue

            # Add to queue the usage of every spell
            for spell in spells:
                # Ignore spells that have their effects active
                if spell in effects: continue
                
                # Ignore unaffordable spells
                if spells[spell][0] > player_mana: continue

                # Spend mana
                nxtplayer_mana = player_mana - spells[spell][0]
                nxt_mana_spent = mana_spent + spells[spell][0]

                if spells[spell][5] == -1: # Instant spells
                    # print(f'    Player used spell '{spell}', instant')
                    nxtEffects = list(effects.items())
                    
                    nxt_player_hp = player_hp + spells[spell][1]
                    nxt_boss_hp = boss_hp - spells[spell][4]
                else: # Spells with duration (activate starting the next turn)
                    # print(f'    Player used spell '{spell}', only active next turn')
                    effects[spell] = spells[spell][5]
                    nxtEffects = list(effects.items())
                    effects.pop(spell)

                    nxt_player_hp = player_hp
                    nxt_boss_hp = boss_hp

                # print(f'        Next: ManaSpent={mana_spent} | HP={nxt_player_hp} | Mana={nxtplayer_mana} | Boss={nxt_boss_hp} | Spells={effects}')
                nxt = (nxt_mana_spent, nxt_player_hp, nxtplayer_mana, nxtEffects, nxt_boss_hp, not player_turn)
                heappush(heap, nxt)
        else:
            # print('    Boss attacks!')
            nxtEffects = list(effects.items())

            nxt_mana_spent = mana_spent
            nxt_player_hp = player_hp - max(1, boss_damage - player_armor)
            nxt_boss_hp = boss_hp
            nxtplayer_mana = player_mana

            # print(f'        Next: ManaSpent={mana_spent} | HP={nxt_player_hp} | Mana={nxtplayer_mana} | Boss={nxt_boss_hp} | Spells={effects}')
            nxt = (nxt_mana_spent, nxt_player_hp, nxtplayer_mana, nxtEffects, nxt_boss_hp, not player_turn)
            heappush(heap, nxt)

######################################

rawInput = AOCUtils.load_input(22)

boss_hp, boss_damage = [int(s.split()[-1]) for s in rawInput]
player_hp = 50
player_mana = 500

#                          Cost  +HP  +Mana  +Armor  Damage  Duration
spells = {'Magic Missile': ( 53,  0,    0,      0,     4,      -1),
                  'Drain': ( 73,  2,    0,      0,     2,      -1),
                 'Shield': (113,  0,    0,      7,     0,       6),
                 'Poison': (173,  0,    0,      0,     3,       6),
               'Recharge': (229,  0,  101,      0,     0,       5)
         }

AOCUtils.print_answer(1, battle(player_hp, player_mana, boss_hp, boss_damage, spells, part=1))

AOCUtils.print_answer(2, battle(player_hp, player_mana, boss_hp, boss_damage, spells, part=2))

AOCUtils.print_time_taken()