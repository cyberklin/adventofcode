import sys
import re

def read_input(fname):
    lines = []
    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            lines.append(line)
    return lines

def get_next_coords(coords, diff):
    return (coords[0] + diff[0], coords[1] + diff[1])

def read_letter(matrix, coords):
    i, j = coords
    if i >=0 and i < len(matrix) and j >= 0 and j < len(matrix[i]):
        return matrix[i][j]
    else:
        return '_'

def read_next_letter(matrix, coords, diff):
    return read_letter(matrix, get_next_coords(coords, diff))

def read_x(matrix, center_coords):
    diffs = [[-1, -1], [1, 1], [1, -1], [-1, 1]]
    res = ''
    for d in diffs:
        res += read_next_letter(matrix, center_coords, d)
#    print('x read from ', center_coords, ' = ', res)
    return res
        
def is_x_mas(s):
    return ((s[0:2] == 'MS' or s[0:2] == 'SM') and (s[2:4] == 'MS' or s[2:4] == 'SM'))

def count_x_mases(matrix):
    count = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == 'A' and is_x_mas(read_x(matrix, (i, j))):
                count += 1
    return count

def main():
    fname = sys.argv[1]

    matrix = read_input(fname)
    result = count_x_mases(matrix)
    print('result = ', result)

if __name__ == "__main__":
    main()
