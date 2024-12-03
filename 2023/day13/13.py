import sys
import collections
import math

def print_pattern(p):
    print('---- pattern ----')
    for i in range(0, len(p)):
        for j in p[i]:
            print(j,end='')
        print()

def parse_file(fname):

    patterns = [] 
    with open(fname) as f:
        pattern = []
        for line in f:
            line = line.rstrip('\n')
            if line:
                pattern.append(line)
            else:
                patterns.append(pattern)
                pattern = []
        if pattern:
            patterns.append(pattern)

    return patterns

def get_v_mirror_line(p):

    v_mirror = -1
    smudged_line = -1
    r,c = len(p), len(p[0])
    
    v_mirrors = collections.defaultdict(lambda: True)
    smudges = collections.defaultdict(int)
    for i in range(0, r):
        for j in range(0, c - 1):
            d = 0
            while (j - d) >= 0 and (j + d + 1) < c:
                if p[i][j - d] != p[i][j + d + 1]:
                    v_mirrors[j] = False
                    smudges[j] += 1 
                d += 1

    for j in range(0, c - 1):
        if v_mirrors[j]:
            v_mirror = j
        if smudges[j] == 1:
            smudged_line = j

    return v_mirror, smudged_line

def get_h_mirror_line(p):

    tr = list(zip(*[reversed(x) for x in p])) # rotate left
    return get_v_mirror_line(tr)


def calc_pattern_notes(p):

    ret, ret_smudged = 0, 0
    v, v_smudged = get_v_mirror_line(p)
    h, h_smudged = get_h_mirror_line(p)

    if v != -1:
        ret = v + 1
    elif h != -1:
        ret = 100*(h + 1)

    if v_smudged != -1:
        ret_smudged = v_smudged + 1
    elif h_smudged != -1:
        ret_smudged =  100*(h_smudged + 1)
    
    return ret, ret_smudged

def main():
    fname = sys.argv[1]
    total, total_smudged = 0, 0

    patterns = parse_file(fname)

    for p in patterns:
#        print_pattern(p)
        n, n_smudged = calc_pattern_notes(p)
        total += n
        total_smudged += n_smudged

    print("result", total)
    print("result smudged", total_smudged)

if __name__ == "__main__":
    main()
