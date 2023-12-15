import sys
import collections
import math

def read_records(fname):

    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            items, groups = line.split(' ', 2)
            groups = collections.deque(map(int,groups.split(',')))
            yield (items, groups)

def get_variants(record):
    pattern, groups = record
    groups = groups.copy()
    
#    print('---- starting variants for',pattern,'groups',groups)

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
#                print('prefix with 0 variants:',pattern[0:i],'next group',next_group,groups)
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
#        print('ret ',ret,'for',record)
        return ret

    next_pattern1 = pattern[:first_unknown] + '.' + pattern[first_unknown+1:]
    next_pattern1 = next_pattern1[next_start:]

    next_pattern2 = pattern[:first_unknown] + '#' + pattern[first_unknown+1:]
    next_pattern2 = next_pattern2[next_start:]

    return get_variants((next_pattern1, groups)) + get_variants((next_pattern2, groups))

def main():
    fname = sys.argv[1]
    total = 0

    for r in read_records(fname):
#        print('PATTERN',r)
        variants = get_variants(r)
        print('PATTERN RESULT',variants)
        total += variants
    print("result", total)

if __name__ == "__main__":
    main()
