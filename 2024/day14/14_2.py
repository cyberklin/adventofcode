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

def count_max_strike(n, m, r_dict):
    max_strike = 0
    for i in range(n):
        strike = 0
        for j in range(m):
            c = r_dict.get((i,j),0)
            strike = strike + 1 if c > 0 else 0
            if strike > max_strike:
                max_strike = strike
    return max_strike

def print_field(n, m, r_dict):
    for i in range(n):
        for j in range(m):
            count = r_dict.get((i,j), 0)
            print('.' if count == 0 else count, end='')
        print()

def main():
    fname = sys.argv[1]

    robots = read_input(fname)
    n, m = 103, 101
    
    strikes_num = 0
    min_strike_to_print = 10
    t = 0
    while True:
        r_dict = {}
        for r in robots:
            steps = 11 + 101 * t
            r2 = simulate(r, n, m, steps)
            r_dict[r2[0]] = r_dict.get(r2[0],0) + 1
        max_strike = count_max_strike(n, m, r_dict)
        if max_strike >= min_strike_to_print:
            print('======== field after',steps,t)
            print_field(n, m, r_dict)
            strikes_num += 1
            if strikes_num > 10:
                break
        if t % 1000 == 0:
            print('t = ',t)
        t += 1

if __name__ == "__main__":
    main()
