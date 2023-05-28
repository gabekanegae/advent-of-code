##################################
# --- Day 17: Set and Forget --- #
##################################

import AOCUtils
from intcodeVM import VM

class BotCam:
    def __init__(self, cam):
        self.cam = [list(line) for line in cam]
        self.size = (len(cam), len(cam[0]))
        self.bot_pos, self.bot_facing = None, None

        for x in range(self.size[0]):
            for y in range(self.size[1]):
                if self.cam[x][y] != '.' and self.cam[x][y] != '#':
                    self.bot_pos, self.bot_facing = (x, y), self.cam[x][y]
                    self.cam[x][y] = '#'

    def sum_intersections(self):
        total = 0
        for x in range(1, self.size[0]-2):
            for y in range(1, self.size[1]-2):
                if self.cam[x][y] != '#': continue
                if self.cam[x-1][y] == self.cam[x+1][y] == self.cam[x][y-1] == self.cam[x][y+1]:
                    total += x*y

        return total

    def _rotate(self, direction):
        faces = '^>v<'
        if direction == 'R':
            new_face = (faces.index(self.bot_facing)+1) % len(faces)
        elif direction == 'L':
            new_face = (faces.index(self.bot_facing)-1) % len(faces)

        return faces[new_face]

    def get_path(self):
        moves = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

        path = []
        while True:
            nxtTile = {'fwd': moves[self.bot_facing],
                       'left': moves[self._rotate('L')],
                       'right': moves[self._rotate('R')]}
            
            nxt_step = {'fwd': None,
                       'left': None,
                       'right': None}
            
            for k, v in nxtTile.items():
                if not (0 <= self.bot_pos[0]+v[0] < self.size[0]): continue
                if not (0 <= self.bot_pos[1]+v[1] < self.size[1]): continue

                if self.cam[self.bot_pos[0]+v[0]][self.bot_pos[1]+v[1]] == '#':
                    nxt_step[k] = (self.bot_pos[0]+v[0], self.bot_pos[1]+v[1])

            # Always go forward, if possible
            if nxt_step['fwd']:
                self.bot_pos = nxt_step['fwd']
                path[-1] += 1
            elif nxt_step['left']:
                self.bot_pos = nxt_step['left']
                self.bot_facing = self._rotate('L')
                path += ['L', 1]
            elif nxt_step['right']:
                self.bot_pos = nxt_step['right']
                self.bot_facing = self._rotate('R')
                path += ['R', 1]
            else:
                return path

    # def __repr__(self):
    #     s = ''
    #     for line in self.cam:
    #         s += ''.join(line) + '\n'
    #     return s

def format_input(s):
    return ','.join(str(c) for c in s)

def find_and_replace(l, f, r):
    nl = []
    
    i = 0
    while i < len(l):
        if l[i:i+len(f)] == f:
            nl.append(r)
            i += len(f)
        else:
            nl.append(l[i])
            i += 1

    return nl

def compress_path(path):
    funcNames = list('ABC')

    # Recursive backtracking approach
    def compress_recursive(main, funcs):
        # If we have three functions, do not recurse anymore
        if len(funcs) == 3:
            # If main is short enough and fully compressed, return answer
            if len(format_input(main)) <= 20 and all(c in funcNames for c in main):
                main = format_input(main)
                A, B, C = [format_input(f) for f in funcs]
                return main, A, B, C
            return None

        # Skip to uncompressed portion of path
        cur_pos = 0
        while main[cur_pos] in funcNames: cur_pos += 1

        # Find next function to consider
        cur_func = []
        while True:
            # Next element to add to the current function
            new_element = main[cur_pos]

            # If the element is a function, then this is invalid 
            if new_element in funcNames: break

            cur_func.append(new_element)
            cur_pos += 1

            # If formatted function is longer than 20, also invalid
            if len(format_input(cur_func)) > 20: break

            # Replace in main, add to function list and recurse
            newMain = find_and_replace(main, cur_func, funcNames[len(funcs)])
            newFuncs = funcs + [cur_func]

            solution = compress_recursive(newMain, newFuncs)
            if solution: return solution

        return None

    return compress_recursive(path, [])

##################################

raw_program = AOCUtils.load_input(17)
memory = [int(i) for i in raw_program.split(',')]

vm = VM(memory)
vm.run()
cam = ''.join(chr(c) for c in vm.output).split()

botcam = BotCam(cam)
AOCUtils.print_answer(1, botcam.sum_intersections())

path = botcam.get_path()
main, a, b, c = compress_path(path)
video_feed = 'n'

vm = VM(memory)
vm[0] = 2
vm.run('\n'.join([main, a, b, c, video_feed]) + '\n')
AOCUtils.print_answer(2, vm.output[-1])

AOCUtils.print_time_taken()