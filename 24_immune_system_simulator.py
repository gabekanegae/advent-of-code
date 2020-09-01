################################################
# --- Day 24: Immune System Simulator 20XX --- #
################################################

import AOCUtils

def getTargets(atkArmy, defArmy):
    targeted = set()
    for atkGroup in atkArmy:
        if len(targeted) < len(defArmy):
            dmgGiven = []
            for defGroup in defArmy:
                dmg = (defGroup.calcDmgTaken(atkGroup), defGroup.getEffectivePower(), defGroup.initiative, defGroup)
                dmgGiven.append(dmg)
            dmgGiven.sort(reverse=True)

            # Find best target that hasn't been targeted yet
            take = 0
            while dmgGiven[take][-1] in targeted:
                take += 1

            # Only select targets that would deal damage to
            if dmgGiven[take][0] > 0:
                targeted.add(dmgGiven[take][-1])
                atkGroup.target = dmgGiven[take][-1]
            else:
                atkGroup.target = None

def battle(rawImmune, rawInfection, boost=0):
    immuneArmy = [Group(rawGroup) for rawGroup in rawImmune]
    infectionArmy = [Group(rawGroup) for rawGroup in rawInfection]

    for g in immuneArmy: g.dmgAmt += boost

    immuneArmyUnits = sum(g.units for g in immuneArmy)
    infectionArmyUnits = sum(g.units for g in infectionArmy)


    # Main battle round
    while immuneArmyUnits > 0 and infectionArmyUnits > 0:
        # Remove dead groups
        effAndInit = lambda x: (x.getEffectivePower(), x.initiative)
        immuneArmy = sorted(g for g in immuneArmy if g.alive, key=effAndInit, reverse=True)
        infectionArmy = sorted(g for g in infectionArmy if g.alive, key=effAndInit, reverse=True)

        getTargets(immuneArmy, infectionArmy)
        getTargets(infectionArmy, immuneArmy)

        kills = 0
        allArmies = sorted(immuneArmy+infectionArmy, key=lambda x: x.initiative, reverse=True)
        for army in allArmies:
            if army.alive: # Only alive groups can attack, will be removed in the next round
                kills += army.attack()

        if kills == 0: # No kills in round = tie, would result in endless rounds
            return None, None

        immuneArmyUnits = sum(g.units for g in immuneArmy)
        infectionArmyUnits = sum(g.units for g in infectionArmy)

    return immuneArmyUnits, infectionArmyUnits

class Group:
    def __init__(self, raw):
        rawSplit = raw.split()

        self.units = int(rawSplit[0])
        self.hp = int(rawSplit[4])

        self.immunities = []
        self.weaknesses = []
        if rawSplit[7].startswith("("):
            weaksAndImmunes = raw.split("(")[1].split(")")[0].split("; ")
            for wai in weaksAndImmunes:
                if wai.startswith("weak"): self.weaknesses = wai[8:].split(", ")
                elif wai.startswith("immune"): self.immunities = wai[10:].split(", ")

        self.dmgAmt = int(rawSplit[-6])
        self.dmgType = rawSplit[-5]
        self.initiative = int(rawSplit[-1])

        self.alive = True
        self.target = None

    def calcDmgTaken(self, attacker):
        dmgAmtMult = 1
        if attacker.dmgType in self.immunities: dmgAmtMult = 0
        if attacker.dmgType in self.weaknesses: dmgAmtMult = 2
        
        return attacker.getEffectivePower() * dmgAmtMult

    def receiveAttack(self, attacker):
        dmgAmt = self.calcDmgTaken(attacker)

        unitsLost = dmgAmt // self.hp
        if unitsLost > self.units: unitsLost = self.units
        
        self.units -= unitsLost

        if self.units <= 0:
            self.alive = False

        return unitsLost

    def attack(self):
        unitsLost = 0
        if self.target:
            unitsLost = self.target.receiveAttack(self)
            self.target = None
        return unitsLost

    def getEffectivePower(self):
        return self.units * self.dmgAmt

    # def __repr__(self):
    #     return "U:{}, HP:{}, IMM:{}, WKN:{}, DMG:{}({}), EP:{}, INI:{}".format(
    #             self.units, self.hp, self.immunities, self.weaknesses,
    #             self.dmgAmt, self.dmgType, self.getEffectivePower(), self.initiative)

################################################

rawInput = [s for s in AOCUtils.loadInput(24) if s]

immuneStart, infectionStart = 0, rawInput.index("Infection:")
rawImmune = rawInput[immuneStart+1:infectionStart]
rawInfection = rawInput[infectionStart+1:]

immuneArmyUnits, infectionArmyUnits = battle(rawImmune, rawInfection)
print("Part 1: {}".format(max(immuneArmyUnits, infectionArmyUnits)))

boostLo, boostHi = 0, 1000 # Binary Search
while boostLo != boostHi:
    boost = (boostLo + boostHi) // 2
    immuneArmyUnits, infectionArmyUnits = battle(rawImmune, rawInfection, boost)
    
    if immuneArmyUnits is None or immuneArmyUnits == 0: # Tie or loss
        boostLo = boost + 1
    else:
        boostHi = boost

immuneArmyUnits, infectionArmyUnits = battle(rawImmune, rawInfection, boost)
print("Part 2: {}".format(immuneArmyUnits))

AOCUtils.printTimeTaken()