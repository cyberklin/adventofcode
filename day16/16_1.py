import sys
import collections
import math

UP = '^'
RIGHT = '>'
DOWN = 'v'
LEFT = '<'

REFLECTIONS = {
    (UP, '/'):     [RIGHT],
    (RIGHT, '/'):  [UP],
    (DOWN, '/'):   [LEFT],
    (LEFT, '/'):   [DOWN],
    (UP, '\\'):    [LEFT],
    (RIGHT, '\\'): [DOWN],
    (DOWN, '\\'):  [RIGHT],
    (LEFT, '\\'):  [UP],
    (UP, '-'):     [LEFT, RIGHT],
    (DOWN, '-'):   [LEFT, RIGHT],
    (LEFT, '|'):   [UP, DOWN],
    (RIGHT, '|'):  [UP, DOWN],
}

field = []
beam = collections.defaultdict(list)

def read_field(fname):
    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            field.append(line)

def print_field():
    r, c = len(field), len(field[0])
    for i in range(0, r):
        for j in range(0, c):
            symbol = field[i][j]
            if symbol == '.':
                passes = beam[(i,j)]
                if len(passes) == 1:
                    symbol = passes[0]
                elif len(passes) > 1:
                    symbol = str(len(passes))
            print(symbol, end='')
        print()

def move(point, m):
    i, j = point
    if m == UP:
        ret = (i - 1, j)
    elif m == DOWN:
        ret = (i + 1, j)
    elif m == RIGHT:
        ret = (i, j + 1)
    elif m == LEFT:
        ret = (i, j - 1)

    return ret

def reflect(point, m):
    i, j = point
    k = (m, field[i][j])
    if k in REFLECTIONS:
        return REFLECTIONS[k]
    else: # if no reflection - keep going same way
        return [m] 


def is_in_field(point):
    i, j = point
    return (len(field) > 0 and i >= 0 and i < len(field) and j >= 0 and j < len(field[0]))

def been_here(point, m):
    return m in beam[point]

def mark_been(point, m):
    beam[point].append(m)

def main():
    fname = sys.argv[1]
    
    read_field(fname)

    moves = collections.deque()
    moves.append(((0,-1),RIGHT))

    while len(moves) > 0:
        point, direction = moves.popleft()
        next_point = move(point, direction)
        if is_in_field(next_point) and not been_here(next_point, direction): 
            mark_been(next_point, direction)
            next_directions = reflect(next_point, direction)
            for d in next_directions:
                moves.append((next_point, d))

#    print_field()
    result = 0
    for p in beam:
        if len(beam[p]) > 0:
            result += 1
    print("result =", result)

if __name__ == "__main__":
    main()
