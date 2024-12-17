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

def get_combo_op(regs, op):
    if op == 4: op = regs['A']
    elif op == 5: op = regs['B']
    elif op == 6: op = regs['C']
    return op

def adv(regs, op):
    num = regs['A']
    den = 2**get_combo_op(regs, op)
    regs['A'] = int(num / den)
    return (regs, None, None)

def bxl(regs, op):
    regs['B'] = regs['B'] ^ op
    return (regs, None, None)

def bst(regs, op):
    regs['B'] = get_combo_op(regs, op) % 8
    return (regs, None, None)

def jnz(regs, op):
    new_ip = None
    if regs['A'] != 0:
        new_ip = op
    return (regs, new_ip, None)

def bxc(regs, op):
    regs['B'] = regs['B'] ^ regs['C']
    return (regs, None, None)

def out(regs, op):
    out = get_combo_op(regs, op) % 8
    return (regs, None, out)

def bdv(regs, op):
    num = regs['A']
    den = 2**get_combo_op(regs, op)
    regs['B'] = int(num / den)
    return (regs, None, None)

def cdv(regs, op):
    num = regs['A']
    den = 2**get_combo_op(regs, op)
    regs['C'] = int(num / den)
    return (regs, None, None)

def main():
    fname = sys.argv[1]

    regs, cmds = read_input(fname)
    outputs = [] 

    cmds_map = {
        0: adv,
        1: bxl,
        2: bst,
        3: jnz,
        4: bxc,
        5: out,
        6: bdv,
        7: cdv,
    }

    ip = 0
    while ip < len(cmds):
        cmd = cmds[ip]
        op = cmds[ip + 1]

        regs, new_ip, output = cmds_map[cmd](regs, op)
        ip = new_ip if new_ip is not None else ip + 2
        if output is not None: outputs.append(output)

    result = ','.join(map(str, outputs))
    print('result =',result)

if __name__ == "__main__":
    main()
