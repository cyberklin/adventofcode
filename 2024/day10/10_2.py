import sys
import collections

UP    = 1
RIGHT = 2
DOWN  = 4
LEFT  = 8

MOVES = {
    UP    : [-1,  0], 
    RIGHT : [ 0, +1], 
    DOWN  : [+1,  0], 
    LEFT  : [ 0, -1], 
}

def get_next_coords(coords, direction):
    diff = MOVES[direction]
    return (coords[0] + diff[0], coords[1] + diff[1])

def get_height(matrix, coords):
    i, j = coords
    if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[i]):
        return int(matrix[i][j])
    else:
        return -1

def read_input(fname):
 
    matrix = []
    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            matrix.append(list(line))

    return matrix

def main():
    fname = sys.argv[1]

    matrix = read_input(fname)
    n, m = len(matrix), len(matrix[0])
    queue = collections.deque()

    for i in range(0, n):
        for j in range(0, m):
            if matrix[i][j] == '0':
                queue.append([(i,j)])

    trails = []

    while len(queue):
        trailpart = queue.popleft()
        last_pos = trailpart[-1]
        last_height = int(matrix[last_pos[0]][last_pos[1]])
        if last_height == 9:
            trails.append(trailpart)
            continue

        for direction in MOVES:
            next_pos = get_next_coords(last_pos, direction)
            next_height = get_height(matrix, next_pos)
            if next_height == last_height + 1: 
                next_trailpart = trailpart.copy()
                next_trailpart.append(next_pos)
                queue.appendleft(next_trailpart)

    result = len(trails)
    print('result = ', result)

if __name__ == "__main__":
    main()
