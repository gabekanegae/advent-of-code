################################################
# --- Day 24: Immune System Simulator 20XX --- #
################################################

import AOCUtils

def get_targets(atk_army, def_army):
    targeted = set()
    for atk_group in atk_army:
        if len(targeted) < len(def_army):
            damage_given = []
            for def_group in def_army:
                dmg = (def_group.get_damage_taken(atk_group), def_group.get_effective_power(), def_group.initiative, def_group)
                damage_given.append(dmg)
            damage_given.sort(reverse=True)

            # Find best target that hasn't been targeted yet
            take = 0
            while damage_given[take][-1] in targeted:
                take += 1

            # Only select targets that would deal damage to
            if damage_given[take][0] > 0:
                targeted.add(damage_given[take][-1])
                atk_group.target = damage_given[take][-1]
            else:
                atk_group.target = None

def battle(raw_immune, raw_infection, boost=0):
    immune_army = [Group(raw_group) for raw_group in raw_immune]
    infection_army = [Group(raw_group) for raw_group in raw_infection]

    for g in immune_army: g.damage_amount += boost

    immune_army_units = sum(g.units for g in immune_army)
    infection_army_units = sum(g.units for g in infection_army)

    # Main battle round
    while immune_army_units > 0 and infection_army_units > 0:
        # Remove dead groups
        eff_and_init = lambda x: (x.get_effective_power(), x.initiative)
        immune_army = sorted([g for g in immune_army if g.alive], key=eff_and_init, reverse=True)
        infection_army = sorted([g for g in infection_army if g.alive], key=eff_and_init, reverse=True)

        get_targets(immune_army, infection_army)
        get_targets(infection_army, immune_army)

        kills = 0
        all_armies = sorted(immune_army+infection_army, key=lambda x: x.initiative, reverse=True)
        for army in all_armies:
            if army.alive: # Only alive groups can attack, will be removed in the next round
                kills += army.attack()

        if kills == 0: # No kills in round = tie, would result in endless rounds
            return None, None

        immune_army_units = sum(g.units for g in immune_army)
        infection_army_units = sum(g.units for g in infection_army)

    return immune_army_units, infection_army_units

class Group:
    def __init__(self, raw):
        raw_split = raw.split()

        self.units = int(raw_split[0])
        self.hp = int(raw_split[4])

        self.immunities = []
        self.weaknesses = []
        if raw_split[7].startswith('('):
            weaks_and_immunes = raw.split('(')[1].split(')')[0].split('; ')
            for wai in weaks_and_immunes:
                if wai.startswith('weak'): self.weaknesses = wai[8:].split(', ')
                elif wai.startswith('immune'): self.immunities = wai[10:].split(', ')

        self.damage_amount = int(raw_split[-6])
        self.damage_type = raw_split[-5]
        self.initiative = int(raw_split[-1])

        self.alive = True
        self.target = None

    def get_damage_taken(self, attacker):
        damage_amount_mult = 1
        if attacker.damage_type in self.immunities: damage_amount_mult = 0
        if attacker.damage_type in self.weaknesses: damage_amount_mult = 2
        
        return attacker.get_effective_power() * damage_amount_mult

    def receive_attack(self, attacker):
        damage_amount = self.get_damage_taken(attacker)

        units_lost = damage_amount // self.hp
        if units_lost > self.units: units_lost = self.units
        
        self.units -= units_lost

        if self.units <= 0:
            self.alive = False

        return units_lost

    def attack(self):
        units_lost = 0
        if self.target:
            units_lost = self.target.receive_attack(self)
            self.target = None
        return units_lost

    def get_effective_power(self):
        return self.units * self.damage_amount

    # def __repr__(self):
    #     return 'U:{}, HP:{}, IMM:{}, WKN:{}, DMG:{}({}), EP:{}, INI:{}'.format(
    #             self.units, self.hp, self.immunities, self.weaknesses,
    #             self.damage_amount, self.damage_type, self.get_effective_power(), self.initiative)

################################################

raw_reindeer_condition = AOCUtils.load_input(24)
reindeer_condition = list(filter(lambda s: s, raw_reindeer_condition))

immune_start, infection_start = 0, reindeer_condition.index('Infection:')
raw_immune = reindeer_condition[immune_start+1:infection_start]
raw_infection = reindeer_condition[infection_start+1:]

immune_army_units, infection_army_units = battle(raw_immune, raw_infection)
AOCUtils.print_answer(1, max(immune_army_units, infection_army_units))

boost_lo, boost_hi = 0, 1000 # Binary Search
while boost_lo != boost_hi:
    boost = (boost_lo + boost_hi) // 2
    immune_army_units, infection_army_units = battle(raw_immune, raw_infection, boost)
    
    if immune_army_units is None or immune_army_units == 0: # Tie or loss
        boost_lo = boost + 1
    else:
        boost_hi = boost

immune_army_units, _ = battle(raw_immune, raw_infection, boost)
AOCUtils.print_answer(2, immune_army_units)

AOCUtils.print_time_taken()