##############################################
# --- Day 18: Settlers of The North Pole --- #
##############################################

import AOCUtils

class Landscape:
    def __init__(self, land):
        self.land = land
        self.size = (len(land), len(land[0]))

    def _get_updated_cell(self, pos):
        open_acres, wooded_acres, lumberyard_acres = 0, 0, 0

        for i in range(pos[0]-1, pos[0]+2):
            for j in range(pos[1]-1, pos[1]+2):
                if (i, j) == pos: continue
                if not 0 <= i < self.size[0] or not 0 <= j < self.size[1]: continue
                
                if self.land[i][j] == '.': open_acres += 1
                elif self.land[i][j] == '|': wooded_acres += 1
                elif self.land[i][j] == '#': lumberyard_acres += 1

        if self.land[pos[0]][pos[1]] == '.' and wooded_acres >= 3: return '|'
        if self.land[pos[0]][pos[1]] == '|' and lumberyard_acres >= 3: return '#'
        if self.land[pos[0]][pos[1]] == '#' and (lumberyard_acres == 0 or wooded_acres == 0): return '.'
        return None

    def update(self):
        updates = dict()
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                pos = (i, j)
                updated = self._get_updated_cell(pos)
                if updated: updates[pos] = updated

        for pos, new in updates.items():
            self.land[pos[0]][pos[1]] = new

    def get_resource_value(self):
        wooded_acres = sum(s.count('|') for s in self.land)
        lumberyard_acres = sum(s.count('#') for s in self.land)
        return wooded_acres * lumberyard_acres

##############################################

raw_land = AOCUtils.load_input(18)
landscape = Landscape(list(map(list, raw_land)))

minute = 0
while minute < 10:
    minute += 1
    landscape.update()

AOCUtils.print_answer(1, landscape.get_resource_value())

# Find period
last_seen_at = dict()
test_period = None
while True:
    value = landscape.get_resource_value()

    if not test_period:
        if value in last_seen_at:
            test_period = minute - last_seen_at[value]
        else:
            last_seen_at[value] = minute
    else:
        if value in last_seen_at and minute - last_seen_at[value] == test_period:
            period = test_period
            break
        else:
            test_period = None

    minute += 1
    landscape.update()

# Record repeated values
values = []
for i in range(period):
    values.append(landscape.get_resource_value())
    landscape.update()

final_value = values[(1000000000 - minute) % period]
AOCUtils.print_answer(2, final_value)

AOCUtils.print_time_taken()