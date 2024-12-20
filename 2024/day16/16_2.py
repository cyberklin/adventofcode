import sys
import collections
import math

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

def main():
    fname = sys.argv[1]

    n, m, start, end, walls = read_input(fname)
    h = []

    costs = {start: {}}
    q = collections.deque()
    q.append((start, RIGHT, None))

    while len(q):
        pos, dir, prev_pos = q.popleft()
        cur_cost = costs.get(pos, {}).get(prev_pos, 0)
        candidates = get_next_steps(pos, dir, walls)

        for next_pos, next_dir in candidates:
            next_cost_new = cur_cost + 1 + (1000 if next_dir != dir else 0)
            next_cost = costs.get(next_pos, {}).get(pos, math.inf)
            if next_cost_new < next_cost:
                if not next_pos in costs: 
                    costs[next_pos] = {}
                costs[next_pos][pos] = next_cost_new
                q.append((next_pos, next_dir, pos))

    path = {}
    q = collections.deque()
    q.append((end, None))

    while len(q):
        pos, prev_delta = q.popleft()
        path[pos] = 1
        cur_costs = costs.get(pos, {})
        min = math.inf
        for next_pos, next_cost in cur_costs.items():
            delta = (next_pos[0] - pos[0], next_pos[1] - pos[1])
            next_cost += 1000 if (prev_delta is not None and delta != prev_delta) else 0
            if next_cost < min:
                min = next_cost
                prevs = [(next_pos, delta)]
            elif next_cost == min:
                prevs.append((next_pos, delta))
        for prev in prevs:
            if prev[0] not in path:
                q.append(prev)

    for i in range(n):
        for j in range(m):
            s = '.'
            if path.get((i,j),'') != '': s = 'O'
            if walls.get((i,j),''): s = '#'
            print(s,end='')
        print()

    print('result = ', len(path))

if __name__ == "__main__":
    main()
