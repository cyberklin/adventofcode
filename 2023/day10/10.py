import sys
import collections
import math

START = 0
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

START_TILE = 'S'

TILES = {
    UP: ['|', 'L', 'J'],
    DOWN: ['|', '7', 'F'],
    LEFT: ['-', 'J', '7'],
    RIGHT: ['-', 'L', 'F'],
}


OPPOSITE = {
    UP: DOWN,
    DOWN: UP,
    LEFT: RIGHT,
    RIGHT: LEFT,
}

def print_grid(grid):
    print('------')
    for i in range(0, len(grid)):
        print("%4d" % i,end='    ')
        for tile in grid[i]:
            print(tile,end='')
        print()
    print('------')

def parse_file(fname):

    grid = [] 
    start = ()
    with open(fname) as f:

        i = 0
        for line in f:
            line = line.rstrip('\n')
            tiles = []
            for j in range(0, len(line)):
                tiles.append(line[j])
                if line[j] == 'S': 
                    start = (i, j)
            grid.append(tiles)
            i += 1

    return grid, start

def get_cycle(grid, start):

    path = [] 
    visited = collections.defaultdict(int)
    r = len(grid)
    c = len(grid[0])
    next = [start, START]
    current = ((), )

    while True:
        prev = current
        current = next
        i,j = current[0]
        visited[current[0]] = 1
        path.append(current)

        around = [
            [(i - 1, j), UP],
            [(i + 1, j), DOWN],
            [(i, j - 1), LEFT],
            [(i, j + 1), RIGHT],
        ]
        
        for a in around:
            ai,aj = a[0]
            if ai >= 0 and ai < r and aj >= 0 and aj < c:
                if (prev[0] != start and (ai,aj) == start) or not visited[(ai,aj)]:
                    current_connected = grid[i][j] == START_TILE or grid[i][j] in TILES[a[1]]
                    # next tile should face opposite
                    a_connected = grid[ai][aj] == START_TILE or grid[ai][aj] in TILES[OPPOSITE[a[1]]] 
                    if current_connected and a_connected:
                        next = [(ai, aj), a[1]]
                        break

        if next == current: 
            break


    return path, visited

def detect_start_tile(path):
    first_move = path[1][1]
    last_move = path[-1][1]

    s_tile = list(set(TILES[first_move]) & set(TILES[OPPOSITE[last_move]]))[0]

    return s_tile


def main():
    fname = sys.argv[1]
    total = 0

    grid, start = parse_file(fname)

    path,boundary = get_cycle(grid, start)

    grid[start[0]][start[1]] = detect_start_tile(path)
    n = 0

    for i in range(0, len(grid)):
        is_in = False
        line_start = ''
        for j in range(0, len(grid[i])):
            tile = grid[i][j]
            if boundary[(i,j)]:
                if tile == '|':
                    is_in = not is_in
                elif tile in ['F','L']:
                    line_start = tile
                elif tile in ['7','J']:
                    if (tile == '7' and line_start == 'L') or (tile == 'J' and line_start == 'F'):
                        is_in = not is_in
                    line_start = ''
            elif not boundary[(i,j)] and is_in:
                n += 1

    print("max distance",math.ceil(len(path)/2) - 1)
    print("inside", n)

if __name__ == "__main__":
    main()
