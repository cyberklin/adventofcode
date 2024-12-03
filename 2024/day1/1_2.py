import sys
import collections


def parse_file(fname):

    left = []
    counts = collections.defaultdict(int)

    with open(fname) as f:

        for line in f:
            line = line.rstrip('\n')
            a, b = map(int, line.split('   ', 2))
            left.append(a)
            counts[b] += 1

    return left, counts


def main():
    fname = sys.argv[1]

    left, counts  = parse_file(fname)
    
    similarity = 0
    for i in range(0, len(left)):
        similarity += left[i] * counts[left[i]]

    print('result = ', similarity)


if __name__ == "__main__":
    main()
