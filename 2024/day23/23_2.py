import sys
import collections

def key(a, b):
    return (a, b) if a < b else (b, a)

def main():
    fname = sys.argv[1]

    links = {}
    connections = collections.defaultdict(list)
    q = collections.deque()
    for line in open(fname).readlines():
        a, b = line.strip().split('-',2)
        links[key(a, b)] = 1
        q.append(key(a, b))
        connections[a].append(b)
        connections[b].append(a)

    max_clique = []
    max_size = 0
    seen = {}
    while len(q):
        clique = q.popleft()
        size = len(clique)
        if size > max_size:
            max_clique = clique
            max_size = size
        host, rest = clique[0], clique[1:]
        for link in connections[host]:
            connected = 1
            for host2 in rest:
                if key(link, host2) not in links:
                    connected = 0
                    break
            if connected:
                new_clique = tuple(sorted((link, *clique)))
                if new_clique not in seen:
                    seen[new_clique] = 1
                    q.append(new_clique)

    print('result =', max_size, 'clique =', ','.join(max_clique))

if __name__ == "__main__":
    main()