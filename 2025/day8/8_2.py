import sys
import math
import heapq
import collections

def read_input(fname):
 
    coords = []

    with open(fname) as f:
        for line in f:
            coords.append(tuple(map(int, line.rstrip('\n').split(',',3))))

    return coords

def distance(p1, p2):
    return math.dist(p1, p2)

def main():

    coords = read_input(sys.argv[1])

    distances = [] 

    for i in range(0, len(coords) - 1):
        for j in range(i + 1, len(coords)):
            p1, p2 = coords[i], coords[j]
            d = math.dist(p1, p2)
            heapq.heappush(distances, (d, (p1, p2)))

    circuits_num = 0
    circuits = collections.defaultdict(list)
    pmap = {}

    step = 0 
    result = 0

    while True:
        step += 1
        item = heapq.heappop(distances)
        p1, p2 = item[1]
        if p1 not in pmap and p2 not in pmap: # new circuit
            circuits[circuits_num] = [p1, p2]
            pmap[p1] = circuits_num
            pmap[p2] = circuits_num
            circuits_num += 1
        elif p1 in pmap and p2 in pmap: # merge 2 circuits
            target = pmap[p1]
            source = pmap[p2]
            if source != target: 
                for p in circuits[source]:
                    pmap[p] = target
                    circuits[target].append(p)
                del circuits[source]
        elif p1 in pmap:
            circuits[pmap[p1]].append(p2)
            pmap[p2] = pmap[p1]
        elif p2 in pmap:
            circuits[pmap[p2]].append(p1)
            pmap[p1] = pmap[p2]
        
        if step > 5 and len(circuits) == 1:
            c_len = len(list(circuits.items())[0][1])
            if c_len == len(coords):
                result = p1[0] * p2[0]
                break

    print('result = ', result)

if __name__ == "__main__":
    main()
