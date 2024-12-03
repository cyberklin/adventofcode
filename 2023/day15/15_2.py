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

hashmap = collections.defaultdict(list)

def set_key(k, v):
    k_hash = get_hash(k)
    if not hashmap[k_hash]:
        hashmap[k_hash] = [(k, v)]
    else:
        added = False
        bucket = hashmap[k_hash]

        for i in range(0, len(bucket)):
            if k == bucket[i][0]:
                bucket[i] = (k, v)
                added = True

        if not added:
            bucket.append((k, v))

def del_key(k):
    k_hash = get_hash(k)
    if hashmap[k_hash]:
        bucket = hashmap[k_hash]
        for i in range(0, len(bucket)):
            if k == bucket[i][0]:
                hashmap[k_hash] = bucket[:i] +  bucket[i+1:]

def get_power():
    ret = 0
    for k_hash in hashmap:
        bucket = hashmap[k_hash]
        for i in range(0, len(bucket)):
            ret += (k_hash + 1) * (i + 1) * bucket[i][1]

    return ret

def main():
    fname = sys.argv[1]
    total = 0

    seq = parse_file(fname)

    for i in range(0, len(seq)):
        cmd = seq[i]
        if cmd[-1:] == '-':
            del_key(cmd[:-1])
        elif cmd[-2:-1] == '=':
            set_key(cmd[:-2],int(cmd[-1:]))

    print("result", get_power())

if __name__ == "__main__":
    main()
