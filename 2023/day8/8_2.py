import sys
import collections
import numpy as np

def parse_file(fname):

    steps, nodes, a_nodes = '', {}, []
    with open(fname) as f:

        steps = f.readline().rstrip('\n')
        f.readline()

        for line in f:
            line = line.rstrip('\n')
            node, jumps = line.split(' = ', 2)
            left, right = jumps[1:-1].split(', ', 2)

            nodes[node] = (left, right)
            if node[-1:] == 'A': 
                a_nodes.append(node)

    return steps, nodes, a_nodes

def main():
    fname = sys.argv[1]

    steps, nodes, a_nodes = parse_file(fname)
    state = a_nodes
    distances_to_z = collections.defaultdict(int)
    i = 0

    while True:
        i += 1
        step = steps[(i - 1) % len(steps)]
        for n in range(0, len(state)):
            node = state[n]
            next_node = nodes[node][0] if step == 'L' else nodes[node][1]
            state[n] = next_node

            if next_node[-1:] == 'Z' and not distances_to_z[n]:
                distances_to_z[n] = i

        if len(distances_to_z) == len(state):
            break
    

    arr = np.array(list(distances_to_z.values()))
    result = np.lcm.reduce(arr)

    print("result = {}", result)

if __name__ == "__main__":
    main()
