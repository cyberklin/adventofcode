import sys
import collections
import math

def read_input(fname):

    robots = []
    with open(fname) as f:
        for line in f:
            p, v = line.rstrip('\n').split(' ',2)
            p = tuple(map(int, p.split('=',2)[1].split(',',2)))[::-1]
            v = tuple(map(int, v.split('=',2)[1].split(',',2)))[::-1]
            robots.append((p, v))
    return robots

def simulate(robot, n, m, steps):
    p, v = robot
    return (((p[0] + v[0]*steps) % n , (p[1] + v[1]*steps) % m), v)

def get_quadrant(pos, n, m):
    result = 0
    i, j = pos
    if i < n // 2 and j < m // 2: return 0
    elif i < n // 2 and j > m // 2: return 1
    elif i > n // 2 and j < m // 2: return 2
    elif i > n // 2 and j > m // 2: return 3
    else: return -1

def main():
    fname = sys.argv[1]

    robots = read_input(fname)
    n, m = 103, 101
    
    q_count = collections.defaultdict(int)
    for r in robots:
        r2 = simulate(r, n, m, 100)
        q_count[get_quadrant(r2[0], n, m)] += 1

    result = 1
    for i in range(4):
        result *= q_count.get(i, 1)

    print('result =',result)

if __name__ == "__main__":
    main()
