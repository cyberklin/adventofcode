import sys
import collections
import math

def read_input(fname):

    regs = {}
    cmds = [] 

    with open(fname) as f:
        line = f.readline().strip()
        while line != '':
            parts = line.split(': ',2)
            reg_name = parts[0].split(' ',2)[1]
            reg_value = int(parts[1])
            regs[reg_name] = reg_value
            line = f.readline().strip()
        line = f.readline().strip()
        cmds = list(map(int,line.split(': ',2)[1].split(',')))

    return (regs, cmds)

def run(A):
    outputs = [] 

    while A != 0: 
        C = (int(A / 2**((A % 8) ^ 1)))
        B = (((A % 8) ^ 1) ^ 4) ^ (int(A / 2**((A % 8) ^ 1)))
        outputs.append(str(B % 8))
        A = int(A / 8)

    return ''.join(outputs)

def main():
    fname = sys.argv[1]

    _, cmds = read_input(fname)
    target = ''.join(map(str, cmds))

    q = collections.deque()
    q.append(0)
    result = math.inf
    while len(q):
        base = q.popleft()
        for j in range(0,8):
            r = run(base+j)
            if r == '': continue
            if r == target: # we found something, let's use only minimal
                if (base + j) < result:
                    result = base + j
            if len(r) <= len(target) and target[-len(r):] == r:
                q.appendleft((base+j)*8)
    
    print('run for',result,run(result),target)
    print('result = ',result)

if __name__ == "__main__":
    main()
