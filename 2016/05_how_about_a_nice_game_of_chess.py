##################################################
# --- Day 5: How About a Nice Game of Chess? --- #
##################################################

import AOCUtils
import hashlib

##################################################

door_id = AOCUtils.load_input(5)
base_digest = hashlib.md5(door_id.encode())

password_1 = []
password_2 = ['_' for _ in range(8)]

i = 0
while len(password_1) < 8 or '_' in password_2:
    digest = base_digest.copy()
    digest.update(str(i).encode())
    s = digest.hexdigest()

    if s.startswith('00000'):
        if len(password_1) < 8:
            password_1.append(s[5])

        if '_' in password_2:
            idx = int(s[5], 16)
            if idx < 8 and password_2[idx] == '_':
                password_2[idx] = s[6]
    
    i += 1

AOCUtils.print_answer(1, ''.join(password_1))

AOCUtils.print_answer(2, ''.join(password_2))

AOCUtils.print_time_taken()