import sys
import collections
import math

EXPANSION_RATE = 1000000

def print_pattern(p):
    print('---- pattern ----')
    for i in range(0, len(p)):
        for j in p[i]:
            print(j,end='')
        print()

def parse_file(fname):

    counts = { 'row': collections.defaultdict(int), 'col': collections.defaultdict(int), }
    galaxies = []
    i = 0
    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            j = 0
            for x in line:
                if x == '#':
                    counts['row'][i] += 1
                    counts['col'][j] += 1
                    galaxies.append((i,j,len(galaxies)+1))
                j += 1
            i += 1

    return galaxies, counts

def calc_1d_distance(x1, x2, counts):
    start = min(x1, x2)
    end = max(x1, x2)
    dist = 0
    for i in range(start, end):
        dist += EXPANSION_RATE if counts[i] == 0 else 1
    return dist


def calc_distance(a, b, counts):
    v_dist = calc_1d_distance(a[0], b[0], counts['row'])
    h_dist = calc_1d_distance(a[1], b[1], counts['col'])
#    print('c_d',(a,b,v_dist,h_dist))

    return v_dist + h_dist

def main():
    fname = sys.argv[1]
    total = 0

    galaxies, counts = parse_file(fname)
    print(galaxies)
    print(counts)

    for i in range(0, len(galaxies) - 1):
        g1 = galaxies[i]
        for j in range(i + 1, len(galaxies)):
            g2 = galaxies[j]
            d = calc_distance(g1, g2, counts)
            print('distance (',g1,',',g2,')',d)
            total += d

    print("result", total)

if __name__ == "__main__":
    main()
