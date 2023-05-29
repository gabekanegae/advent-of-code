#############################################
# --- Day 4: Security Through Obscurity --- #
#############################################

import AOCUtils

alphabet = 'abcdefghijklmnopqrstuvwxyz'

class Room:
    def __init__(self, s):
        s = s.split('[')
        self.checksum = s[1][:-1]
        
        s = s[0].split('-')
        self.name = '-'.join(s[:-1])
        self.sid = int(s[-1])

    def is_real(self):
        counts = dict()
        for c in self.name:
            if c == '-': continue
            if c not in counts:
                counts[c] = 0
            counts[c] += 1

        counts = sorted((-ct, c) for c, ct in counts.items())
        return ''.join(c for ct, c in counts[:5]) == self.checksum

    def decrypt(self):
        decrypted = []

        for c in self.name:
            if c == '-':
                dc = ' '
            else:
                i = alphabet.index(c)
                dc = alphabet[(i+self.sid) % len(alphabet)]

            decrypted.append(dc)

        return ''.join(decrypted)

#############################################

rooms = [Room(s) for s in AOCUtils.load_input(4)]

rooms = [r for r in rooms if r.is_real()]

real_sum = sum(r.sid for r in rooms)
AOCUtils.print_answer(1, real_sum)

for room in rooms:
    name = room.decrypt() 
    if 'object' in name: # 'northpole object storage'
        AOCUtils.print_answer(2, room.sid)
        break

AOCUtils.print_time_taken()