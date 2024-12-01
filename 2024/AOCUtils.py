from time import perf_counter
import os

_start_time = None

def load_input(day):
    global _start_time

    _start_time = perf_counter()

    day = str(day)
    filename = f'input{day.zfill(2)}.txt'
    filepath = os.path.join('inputs', filename)

    with open(filepath) as f:
        content = [l.rstrip('\n') for l in f.readlines()]

    if len(content) == 1:
        try:
            return int(content[0])
        except:
            try:
                return [int(i) for i in content[0].split()]
            except:
                return content[0]
    else:
        try:
            return [int(i) for i in content]
        except:
            return content

def print_time_taken():
    global _start_time
    _end_time = perf_counter()
    
    delta = _end_time - _start_time
    print(f'Time: {delta:.3f}s')

def print_answer(part, answer):
    if isinstance(answer, list):
        answer = ocr(answer)

    print(f'Part {part}: {answer}')

################################################################################

alphabets = dict()
alphabets[6] = ('ABCEFGHIJKLOPRSUYZ',
    [' ##  ###   ##  #### ####  ##  #  # ###   ## #  # #     ##  ###  ###   ### #  # #   # ####',
     '#  # #  # #  # #    #    #  # #  #  #     # # #  #    #  # #  # #  # #    #  # #   #    #',
     '#  # ###  #    ###  ###  #    ####  #     # ##   #    #  # #  # #  # #    #  #  # #    # ',
     '#### #  # #    #    #    # ## #  #  #     # # #  #    #  # ###  ###   ##  #  #   #    #  ',
     '#  # #  # #  # #    #    #  # #  #  #  #  # # #  #    #  # #    # #     # #  #   #   #   ',
     '#  # ###   ##  #### #     ### #  # ###  ##  #  # ####  ##  #    #  # ###   ##    #   ####'])
alphabets[10] = ('ABCEFGHJKLNPRXZ',
    ['  ##   #####   ####  ###### ######  ####  #    #    ### #    # #      #    # #####  #####  #    # ######',
     ' #  #  #    # #    # #      #      #    # #    #     #  #   #  #      ##   # #    # #    # #    #      #',
     '#    # #    # #      #      #      #      #    #     #  #  #   #      ##   # #    # #    #  #  #       #',
     '#    # #    # #      #      #      #      #    #     #  # #    #      # #  # #    # #    #  #  #      # ',
     '#    # #####  #      #####  #####  #      ######     #  ##     #      # #  # #####  #####    ##      #  ',
     '###### #    # #      #      #      #  ### #    #     #  ##     #      #  # # #      #  #     ##     #   ',
     '#    # #    # #      #      #      #    # #    #     #  # #    #      #  # # #      #   #   #  #   #    ',
     '#    # #    # #      #      #      #    # #    # #   #  #  #   #      #   ## #      #   #   #  #  #     ',
     '#    # #    # #    # #      #      #   ## #    # #   #  #   #  #      #   ## #      #    # #    # #     ',
     '#    # #####   ####  ###### #       ### # #    #  ###   #    # ###### #    # #      #    # #    # ######'])

def _strip_image(image):
    image_height, image_width = len(image), len(image[0])
    empty_columns = [c for c in range(image_width) if not any(image[i][c] for i in range(image_height))]

    # Remove all but one sequential vertical spaces
    to_remove = set([empty_columns[i] for i in range(1, len(empty_columns)) if empty_columns[i] - empty_columns[i-1] == 1])

    # Strip left and right spaces
    col = 0
    while not any(image[i][col] for i in range(image_height)):
        to_remove.add(col)
        col += 1
    col = image_width-1
    while not any(image[i][col] for i in range(image_height)):
        to_remove.add(col)
        col -= 1

    return [[c for i, c in enumerate(l) if i not in to_remove] for l in image]

def _slice_image(image):
    image = _strip_image(image)
    
    image_height, image_width = len(image), len(image[0])

    empty_columns = [c for c in range(image_width) if not any(image[i][c] for i in range(image_height))]
    unspaced_image = [[c for i, c in enumerate(l) if i not in empty_columns] for l in image]

    empty_columns = [-1] + empty_columns + [image_width]
    widths = [b-a-1 for a, b in zip(empty_columns, empty_columns[1:])]

    sliced_image = []
    col = 0
    for w in widths:
        sliced_image.append('\n'.join([''.join(['#' if c else ' ' for c in l[col:col+w]]) for l in unspaced_image]))
        col += w

    return sliced_image

def ocr(image):
    h = len(image)
    if h not in alphabets:
        raise ValueError(f'Image is of height {h} - only 6 and 10 are supported.')

    alphabet_keys, alphabet_values = alphabets[h]
    alphabet_values = _slice_image([[c == '#' for c in l] for l in alphabet_values])

    letters_dict = dict(zip(alphabet_values, alphabet_keys))

    sliced_image = _slice_image(image)

    for c in sliced_image:
        if c not in letters_dict:
            raise ValueError(f'Letter below wasn\'t found in the alphabet of height {h}:\n\n{c}')

    return ''.join(letters_dict[c] for c in sliced_image)

if __name__ == '__main__':
    assert alphabets[6][0] == ocr([[c == '#' for c in l] for l in alphabets[6][1]])
    assert alphabets[10][0] == ocr([[c == '#' for c in l] for l in alphabets[10][1]])