import sys
import re

START_LETTER = 'X'
END = '__'
NEXT_LETTER = {
    'X'    : 'M',
    'M'    : 'A',
    'A'    : 'S',
    'S'    : END,
}

MOVES = [
    [-1,  0], # UP
    [-1, +1], # UP RIGHT 
    [ 0, +1], # RIGHT
    [+1, +1], # DOWN RIGHT
    [+1,  0], # DOWN
    [+1, -1], # DOWN LEFT
    [ 0, -1], # LEFT 
    [-1, -1], # UP LEFT
]

def get_next_coords(coords, diff):
    return (coords[0] + diff[0], coords[1] + diff[1])

def get_letter(matrix, coords):
    i, j = coords
    if i >=0 and i < len(matrix) and j >= 0 and j < len(matrix[i]):
        return matrix[i][j]
    else:
        return ''

def get_next_letter(matrix, coords, direction):
    return get_letter(matrix, get_next_coords(coords, direction))

def check_next_letter(matrix, coords, letter, diff, start):
#    print('check next letter ', [coords, letter, diff])
    next_letter = NEXT_LETTER[letter]
    if next_letter == END:
#        print('found! start: ', start, ' end: ', coords, 'direction: ', diff)
        return 1
    elif next_letter == get_next_letter(matrix, coords, diff):
        return check_next_letter(matrix, get_next_coords(coords, diff), next_letter, diff, start)
    else:
        return 0
       

def find_all_words(matrix):
    count = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == START_LETTER:
                for diff in MOVES:
                    if check_next_letter(matrix, (i,j), START_LETTER, diff, (i,j)):
                        count += 1
    return count

def read_input(fname):
 
    lines = []
    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            lines.append(line)

    return lines

def main():
    fname = sys.argv[1]

    matrix = read_input(fname)
    result = find_all_words(matrix)
    print('result = ', result)

if __name__ == "__main__":
    main()
