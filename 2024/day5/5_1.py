import sys
import collections
import math

def read_input(fname):

    updates = [] 
    rules = collections.defaultdict(int)
    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            if line == '':
                break
            rules[line] = 1
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
                # if there's opposite rule (j|i) -> incorrect update
                if rules[update[j] + '|' + update[i]]:
                    is_correct = 0
        if is_correct:
            result += int(update[math.floor(len(update) / 2)])

    print('result = ', result)



            

if __name__ == "__main__":
    main()
