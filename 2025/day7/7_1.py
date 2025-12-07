import sys
import collections

def read_input(fname):
 
    matrix = []

    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            matrix.append(list(line))

    return matrix, len(matrix), len(matrix[0]), (0, matrix[0].index('S'))

def main():

    matrix, n, m, s = read_input(sys.argv[1])

    result = 0
    end_beams = 0

    q = collections.deque()
    q.append(s)
    seen = collections.defaultdict(int)

    while len(q):
        cur = q.popleft()
        seen[cur] = 1
        next_list = [] 
        if cur[0] == n - 1:
            end_beams += 1
        elif matrix[cur[0] + 1][cur[1]] == '^':
            result += 1
            next_list.append((cur[0] + 1, cur[1] - 1))
            next_list.append((cur[0] + 1, cur[1] + 1))
        else:
            next_list.append((cur[0] + 1, cur[1]))

        for next in next_list:
            if next not in seen and next[1] >=0 and next[1] < m:
                q.appendleft(next)

    print('result = ', result, 'end_beams =', end_beams)

if __name__ == "__main__":
    main()
