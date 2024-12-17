import sys
import collections
import math

UP    = 0
RIGHT = 1
DOWN  = 2
LEFT  = 3

MOVES = {
    UP    : ('^', [-1,  0]),
    RIGHT : ('>', [ 0, +1]),
    DOWN  : ('v', [+1,  0]), 
    LEFT  : ('<', [ 0, -1]),
}

def get_next_steps(pos, d, walls):
    directions = [d, ((d - 1) % 4), ((d + 1) % 4)]
    new_pos = lambda d: (pos[0] + MOVES[d][1][0], pos[1] + MOVES[d][1][1])
    return [(new_pos(d), d) for d in directions if not walls.get(new_pos(d),0)]

def read_input(fname):
 
    grid = [list(line.strip()) for line in open(fname)]
    n, m = len(grid), len(grid[0])
    walls = { } 
    start, end = (0, 0), (0, 0)

    for i in range(n):
        for j in range(m):
            square = grid[i][j]
            if square == 'S': start = (i,j)
            elif square == 'E': end = (i, j)
            elif square == '#': walls[(i,j)] = 1

    return n, m, start, end, walls

def main():
    fname = sys.argv[1]

    n, m, start, end, walls = read_input(fname)
    h = []

    costs = {start: (0, RIGHT, {})}
    q = collections.deque()
    q.append(start)

    while len(q):
        pos = q.popleft()
        cost, dir, path = costs[pos]
        candidates = get_next_steps(pos, dir, walls)

        for next_pos, next_dir in candidates:
            next_cost_new = cost + 1 + (1000 if next_dir != dir else 0)
            cur_cost = costs.get(next_pos, (math.inf, RIGHT, {}))
            if next_cost_new < cur_cost[0]:
                next_path = path.copy()
                next_path[pos] = dir
                costs[next_pos] = (next_cost_new, next_dir, next_path)
                q.append(next_pos)

    result, _, path = costs[end]

    for i in range(n):
        for j in range(m):
            s = '.'
            if path.get((i,j),'') != '': s = MOVES[path[(i,j)]][0]
            if walls.get((i,j),''): s = '#'
            print(s,end='')
        print()

    print('result = ', result)

if __name__ == "__main__":
    main()
