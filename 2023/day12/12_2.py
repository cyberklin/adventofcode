import sys
import collections
import math
import cProfile

def read_records(fname):

    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            items, groups = line.split(' ', 2)
            groups = collections.deque(map(int,groups.split(',')))
            yield (items, groups)

CACHE = collections.defaultdict(lambda: -1)

def get_variants(record):
    pattern, groups = record

    cache_key = pattern + '_' + str(groups)
    if CACHE[cache_key] != -1:
        return CACHE[cache_key]

    groups = groups.copy()
    
    first_unknown = pattern.find('?')
    i = 0
    count = 0
    next_start = 0
    range_limit = first_unknown if first_unknown != -1 else len(pattern)
    ret = -1

    for i in range(0, range_limit):
        cur = pattern[i]
        if cur == '#':
            if not groups:
                ret = 0
                break
            count += 1
            if count > groups[0]:
                ret = 0
                break
        elif cur == '.' and count > 0:
            next_group = groups.popleft()
            if count != next_group:
                ret = 0
                count = 0
                break
            else:
                next_start = i
                count = 0

    if ret == -1 and i == len(pattern) - 1:
        if count == 0:
            ret = 1 if not groups else 0
        else:
            next_group = groups.popleft()
            if count == next_group and not groups:
                ret = 1
            else:
                ret = 0

    if ret != -1:
        CACHE[cache_key] = ret
        return ret

    next_pattern1 = pattern[:first_unknown] + '.' + pattern[first_unknown+1:]
    next_pattern1 = next_pattern1[next_start:]

    next_pattern2 = pattern[:first_unknown] + '#' + pattern[first_unknown+1:]
    next_pattern2 = next_pattern2[next_start:]

    ret = get_variants((next_pattern1, groups)) + get_variants((next_pattern2, groups))
    CACHE[cache_key] = ret
    return ret

def main():
    fname = sys.argv[1]
    total = 0
    i = 0

    for pattern,groups in read_records(fname):
        i += 1
        r = ('?'.join([pattern]*5), groups*5)
        variants = get_variants(r)
#        print(i, 'PATTERN RESULT',variants)
        total += variants
    print("result", total)

if __name__ == "__main__":
    main()
