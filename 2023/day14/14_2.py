import sys
import collections
import math

CYCLES_NUM = 1000000000

def print_matrix(p):
    print('----  ----')
    for i in range(0, len(p)):
        for j in p[i]:
            print(j,end='')
        print()

def parse_file(fname):

    pattern = [] 
    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            pattern.append(list(line))

    return pattern

def rotate_clockwise(m):
    return [list(a) for a in zip(*m[::-1])]

def tilt_north(m):

    r,c = len(m),len(m[0])

    for j in range(0, c):
        c_num = 0
        for i in range(r - 1, -1, -1):
            load = r - i
            if m[i][j] == 'O':
                c_num += 1
            elif m[i][j] == '.' and c_num > 0:
                m[i][j] = 'O'
                m[i + c_num][j] = '.'
            
            if m[i][j] == '#' or i == 0:
                c_num = 0

    return m

def tilt_cycle(m):

    for i in range(0,4):
        m = tilt_north(m)
        m = rotate_clockwise(m)

    return m

def calc_load(m):
    r,c = len(m),len(m[0])
    load = 0
    fingerprint = ''

    for j in range(0, c):
        for i in range(r - 1, -1, -1):
            if m[i][j] == 'O':
                load += r - i
                fingerprint += str(i) + ',' + str(j) + ','

    return load, fingerprint

def main():
    fname = sys.argv[1]
    cycles = CYCLES_NUM
    total = 0

    m = parse_file(fname)

    fingerprints = collections.defaultdict(lambda: ())
    loads = []

    for i in range(0,cycles):
        m = tilt_cycle(m)
        load, fingerprint = calc_load(m)
#        print(i,'result = ',load)
        loads.append(load)
        if not fingerprints[fingerprint]:
            fingerprints[fingerprint] = i
        else:
            # we entered into a cycle
            start = fingerprints[fingerprint] + 1
            length = i - start + 1
            load = loads[((cycles - start) % length) + start - 1]
            break

    print("result", load)

if __name__ == "__main__":
    main()
