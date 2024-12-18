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

def get_next_steps(pos, d, n, m, walls):
    directions = [d, ((d - 1) % 4), ((d + 1) % 4)]
    new_pos = lambda d: (pos[0] + MOVES[d][1][0], pos[1] + MOVES[d][1][1])
    result = []
    for d in directions:
        new_coords = new_pos(d)
        if walls.get(new_coords, 0): continue
        if new_coords[0] < 0 or new_coords[0] >= n or new_coords[1] < 0 or new_coords[1] >= m: continue
        result.append((new_coords, d))
    return result

def main():
    fname = sys.argv[1]
    n, m = 71, 71 # 7, 7
    bytes_limit = 1024 # 12

    lines = [line.strip().split(',') for line in open(fname).readlines()]
    corrupted = {(int(p[1]), int(p[0])) : 1 for p in lines[0:bytes_limit]}

    start, end = (0, 0), (n - 1, m - 1)
    last_path = { }

    for j in range(1024, len(lines)):
        new_byte = (int(lines[j-1][1]), int(lines[j-1][0]))
        if last_path and new_byte not in last_path:
            continue
        corrupted = {(int(p[1]), int(p[0])) : 1 for p in lines[0:j]}

        costs = {start: (0, RIGHT, {})}
        q = collections.deque()
        q.append(start)

        while len(q):
            pos = q.popleft()
            cost, dir, path = costs[pos]
            candidates = get_next_steps(pos, dir, n, m, corrupted)

            for next_pos, next_dir in candidates:
                next_cost_new = cost + 1
                cur_cost = costs.get(next_pos, (math.inf, RIGHT, {}))
                if next_cost_new < cur_cost[0]:
                    next_path = path.copy()
                    next_path[pos] = dir
                    costs[next_pos] = (next_cost_new, next_dir, next_path)
                    q.append(next_pos)

        if end in costs:
            _, _, last_path = costs[end]
        else:
            print('result = ', ','.join(lines[j-1]))
            break

if __name__ == "__main__":
    main()
