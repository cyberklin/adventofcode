import sys
import math

def parse_file(fname):

    steps, nodes = '', {}
    with open(fname) as f:

        steps = f.readline().rstrip('\n')
        f.readline()

        for line in f:
            line = line.rstrip('\n')
            node, jumps = line.split(' = ', 2)
            left, right = jumps[1:-1].split(', ', 2)

            nodes[node] = (left, right)

    return steps, nodes

def main():
    fname = sys.argv[1]

    i = 0
    steps, nodes = parse_file(fname)

    node = 'AAA'
    while node != 'ZZZ':
        step = steps[i % len(steps)]
        node = nodes[node][0] if step == 'L' else nodes[node][1]
        i += 1

    print("result = {}", i)

if __name__ == "__main__":
    main()
