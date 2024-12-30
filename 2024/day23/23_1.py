import sys
import collections

def main():
    fname = sys.argv[1]

    links = {}
    connections = collections.defaultdict(list)
    for line in open(fname).readlines():
        a, b = line.strip().split('-',2)
        links[(a, b)] = 1
        links[(b, a)] = 1
        connections[a].append(b)
        connections[b].append(a)

    result = {}
    for host1, conns in connections.items():
        if host1[0] == 't':
            for host2 in conns:
                for host3 in connections[host2]:
                    if (host3, host1) in links:
                        name = sorted([host1, host2, host3])
                        result[tuple(name)] = 1

    print('result =', len(result))

if __name__ == "__main__":
    main()