import sys
import collections
import math
import functools

def read_input(fname):

    updates = [] 
    rules = collections.defaultdict(int)
    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            if line == '':
                break
            left, right = line.split('|')
            rules[left + '_' + right] = -1 
            rules[right + '_' + left] = 1
        for line in f:
            updates.append(line.rstrip('\n').split(','))
    return rules, updates

def main():
    fname = sys.argv[1]

    result = 0

    rules, updates = read_input(fname)

    for update in updates:
        is_correct = 1
        for i in range(0, len(update) - 1):
            for j in range(i + 1, len(update)):
                if rules[update[j] + '_' + update[i]] == -1:
                    is_correct = 0
        if not is_correct:
            update = sorted(update, key=functools.cmp_to_key(lambda a,b: rules[a + '_' + b]))
            result += int(update[math.floor(len(update) / 2)])

    print('result = ', result)

if __name__ == "__main__":
    main()
