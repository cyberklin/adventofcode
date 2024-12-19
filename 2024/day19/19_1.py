import sys
import collections

CACHE = {}

def is_possible(patterns, pmaxlen, design):

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
        if c == '' or is_possible(patterns, pmaxlen, c):
            result = 1
            break

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
            if is_possible(patterns, pmaxlen, line.strip()):
                result += 1
 
    print('result = ', result)
      

if __name__ == "__main__":
    main()
