import sys
import collections
import math

def parse_file(fname):

    ret = [] 
    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            ret.extend(line.split(','))

    return ret

def get_hash(string):
    ret = 0
    for c in string:
        ret = (ret+ord(c))*17 % 256

    return ret

def main():
    fname = sys.argv[1]
    total = 0

    seq = parse_file(fname)

    for i in range(0, len(seq)):
        total += get_hash(seq[i])

    print("result", total)

if __name__ == "__main__":
    main()
