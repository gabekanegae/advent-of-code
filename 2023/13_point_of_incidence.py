######################################
# --- Day 13: Point of Incidence --- #
######################################

import AOCUtils

class Reflection:
    def __init__(self, v=None, h=None):
        self.v = v
        self.h = h

    def summarize(self):
        return (self.v or 0) + 100 * (self.h or 0)

    def __eq__(self, other):
        return (self.v, self.h) == (other.v, other.h)

def get_vertical_reflections(pattern):
    reflections = []

    for test_reflection in range(len(pattern[0])-1):
        left, mid, right = 0, test_reflection + 1, len(pattern[0])

        if mid - left < right - mid:
            right = mid + (mid - left)
        elif mid - left > right - mid:
            left = mid - (right - mid)

        if all(''.join(l[left:mid]) == ''.join(reversed(l[mid:right])) for l in pattern):
            reflections.append(test_reflection+1)

    return reflections

def get_horizontal_reflections(pattern):
    return get_vertical_reflections(list(zip(*pattern)))

def get_reflections(pattern):
    reflections = []

    for v in get_vertical_reflections(pattern):
        reflections.append(Reflection(v=v))
    for h in get_horizontal_reflections(pattern):
        reflections.append(Reflection(h=h))

    return reflections

######################################

raw_patterns = AOCUtils.load_input(13)

patterns = [l.splitlines() for l in '\n'.join(raw_patterns).split('\n\n')]

p1 = 0
for pattern in patterns:
    reflections = get_reflections(pattern)
    
    assert len(reflections) == 1
    p1 += reflections[0].summarize()

AOCUtils.print_answer(1, p1)

p2 = 0
for pattern in patterns:
    original_reflections = get_reflections(pattern)

    new_patterns = []
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            new_pattern = list(map(list, pattern))
            new_pattern[i][j] = {'#': '.', '.': '#'}[new_pattern[i][j]]

            new_patterns.append(new_pattern)

    for new_pattern in new_patterns:
        new_reflections = get_reflections(new_pattern)

        if new_reflections and new_reflections != original_reflections:
            # If original reflection is still valid, ignore it
            if len(new_reflections) > 1:
                new_reflections.remove(original_reflections[0])
            
            assert len(new_reflections) == 1
            p2 += new_reflections[0].summarize()

            # Only consider first valid smudge removal (otherwise it will be counted twice)
            break

AOCUtils.print_answer(2, p2)

AOCUtils.print_time_taken()
