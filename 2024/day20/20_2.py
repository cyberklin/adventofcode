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

def get_next_steps(pos):
    new_pos = lambda d: (pos[0] + MOVES[d][1][0], pos[1] + MOVES[d][1][1])
    return [new_pos(d) for d in MOVES.keys()]

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

    costs = {start: (0, None)}
    q = collections.deque()
    q.append(start)

    while len(q):
        pos = q.popleft()
        cur_cost, _ = costs[pos]
        candidates = get_next_steps(pos)

        for next_pos in candidates:
            if walls.get(next_pos,0):
                continue
            next_cost_new = cur_cost + 1
            next_cost = costs.get(next_pos, (math.inf, None))[0]
            if next_cost_new < next_cost:
                costs[next_pos] = (next_cost_new, pos)
                q.append(next_pos)

    # rebuild path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = costs[current][1]
    path.reverse()

    # find cheats
    cheats = collections.defaultdict(list)
    for i in range(0, len(path)):
        for j in range(i + 3, len(path)):
            path_distance = j - i
            man_distance = abs(path[i][0] - path[j][0]) + abs(path[i][1] - path[j][1])
            if man_distance <= 20 and man_distance < path_distance:
                saving = path_distance - man_distance
                cheats[saving].append((path[i], path[j]))

    result = 0
    for saving in sorted(cheats.keys()):
        if saving >= 100:
            result += len(cheats[saving])

    print('result = ', result)

if __name__ == "__main__":
    main()
