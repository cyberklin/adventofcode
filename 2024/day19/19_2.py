import sys
import collections

CACHE = {}

def count_possible(patterns, pmaxlen, design):

    if design in CACHE:
        return CACHE[design]

    candidates = []
    max_prefix = design[:pmaxlen]
    for i in range(len(max_prefix), 0, -1):
        prefix = max_prefix[:i]
        if prefix in patterns:
            candidates.append(design[len(prefix):])

    result = 0
    for c in candidates:
        if c == '':
            result += 1
        else:
            result += count_possible(patterns, pmaxlen, c)

    CACHE[design] = result
    return result

def main():
    fname = sys.argv[1]

    result = 0
    with open(fname) as f:
        patterns = {p: 1 for p in f.readline().strip().split(', ')}
        pmaxlen = max(map(len, patterns.keys()))
        f.readline()
        for line in f:
            result += count_possible(patterns, pmaxlen, line.strip())
 
    print('result = ', result)
      

if __name__ == "__main__":
    main()
