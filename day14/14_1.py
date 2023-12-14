import sys
import collections
import math

def print_matrix(p):
    print('----  ----')
    for i in range(0, len(p)):
        for j in p[i]:
            print(j,end='')
        print()

def parse_file(fname):

    pattern = [] 
    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            pattern.append(line)

    return pattern

def main():
    fname = sys.argv[1]
    total = 0

    m = parse_file(fname)
    r,c = len(m),len(m[0])

    for j in range(0, c):
        c_total = 0
        c_num = 0
        for i in range(r - 1, -1, -1):
            load = r - i
            if m[i][j] == 'O':
                c_total += load
                c_num += 1
            elif m[i][j] == '.' and c_num > 0:
                c_total += c_num
            
            if m[i][j] == '#' or i == 0:
                total += c_total
                c_total = 0
                c_num = 0
#            print((i,j,m[i][j],load,c_total,c_num,total))

    print("result", total)

if __name__ == "__main__":
    main()
