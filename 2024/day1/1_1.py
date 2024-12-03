import sys

def parse_file(fname):

    left, right = [], []
    with open(fname) as f:

        for line in f:
            line = line.rstrip('\n')
            a, b = map(int, line.split('   ', 2))
            left.append(a)
            right.append(b)

    return left, right


def main():
    fname = sys.argv[1]

    left, right = parse_file(fname)

    left.sort()
    right.sort()

    delta = 0
    for i in range(0, len(left)):
        delta += abs(left[i] - right[i])

    print('delta = ', delta)

if __name__ == "__main__":
    main()
