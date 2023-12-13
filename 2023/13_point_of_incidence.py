######################################
# --- Day 13: Point of Incidence --- #
######################################

import AOCUtils

class Reflection:
    def __init__(self, v=None, h=None, errors=None):
        self.v = v
        self.h = h
        self.errors = errors

    def summarize(self):
        return (self.v or 0) + 100 * (self.h or 0)

def _get_vertical_reflections(pattern):
    reflections = []

    for reflection_pos in range(len(pattern[0])-1):
        left, mid, right = 0, reflection_pos + 1, len(pattern[0])

        if mid - left < right - mid:
            right = mid + (mid - left)
        elif mid - left > right - mid:
            left = mid - (right - mid)

        errors = 0
        for l in pattern:
            for a, b in zip(l[left:mid], l[mid:right][::-1]):
                errors += a != b

        reflections.append((mid, errors))

    return reflections

def _get_horizontal_reflections(pattern):
    return _get_vertical_reflections(list(zip(*pattern)))

def get_reflections(pattern):
    reflections = []
    for r_v, errors in _get_vertical_reflections(pattern):
        reflections.append(Reflection(v=r_v, errors=errors))
    for r_h, errors in _get_horizontal_reflections(pattern):
        reflections.append(Reflection(h=r_h, errors=errors))

    return reflections

######################################

raw_patterns = AOCUtils.load_input(13)

patterns = [l.splitlines() for l in '\n'.join(raw_patterns).split('\n\n')]

p1 = sum(sum(r.summarize() for r in reflections if r.errors == 0) for reflections in map(get_reflections, patterns))
AOCUtils.print_answer(1, p1)

p2 = sum(sum(r.summarize() for r in reflections if r.errors == 1) for reflections in map(get_reflections, patterns))
AOCUtils.print_answer(2, p2)

AOCUtils.print_time_taken()
