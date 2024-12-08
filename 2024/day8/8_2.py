import sys
import collections

def get_antinodes(a, b, n, m):
    result = []
    dx, dy = b[0] - a[0], b[1] - a[1]
    for sign in [-1, 1]:
        x,y,i = a[0], a[1], 1
        while 0 <= x < n and 0 <= y < m:
            result.append((x,y))
            x = a[0] + sign*i*dx
            y = a[1] + sign*i*dy
            i += 1

    return result

def read_input(fname):
 
    matrix = []
    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            matrix.append(list(line))
    return matrix

def main():
    fname = sys.argv[1]
    matrix = read_input(fname)
    n, m = len(matrix), len(matrix[0])
    signals = collections.defaultdict(list)
    antinodes = collections.defaultdict(int)

    for i in range(0, n):
        for j in range(0, m):
            node = matrix[i][j]
            if node != '.':
                for s in signals[node]:
                    for a in get_antinodes(s, (i,j), n, m):
                        antinodes[a] = 1
                signals[node].append((i, j))

    print('result = ', len(antinodes))

if __name__ == "__main__":
    main()
