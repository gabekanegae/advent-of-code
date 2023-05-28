########################################
# --- Day 19: Medicine for Rudolph --- #
########################################

import AOCUtils

def replaceNth(s, old, new, n):
    find = s.find(old)
    for _ in range(n-1):
        find = s.find(old, find+1)
        if find == -1: return s

    return s[:find] + new + s[find+len(old):]

########################################

rawInput = AOCUtils.load_input(19)

replacements = [r.split(' => ') for r in rawInput[:-2]]
molecule = rawInput[-1]

newMolecules = set()
for old, new in replacements:
    for i in range(molecule.count(old)):
        newMolecule = replaceNth(molecule, old, new, i+1)
        newMolecules.add(newMolecule)

AOCUtils.print_answer(1, len(newMolecules))

'''
X != Rn, Ar, Y

e => XX
X => XX
X => X Rn X Ar | X Rn X Y X Ar | X Rn X Y X Y X Ar

When removed, each Y removes 2 extra atoms
When removed, each Rn/Ar removes 1 extra atom
'''

atoms = sum(atom.isupper() for atom in molecule)
rn = molecule.count('Rn')
ar = molecule.count('Ar')
y = molecule.count('Y')

p2 = atoms - 2*y - (rn+ar) - 1
AOCUtils.print_answer(2, p2)

AOCUtils.print_time_taken()