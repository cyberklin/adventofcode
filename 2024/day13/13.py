import sys
import math

def read_input(fname):

    with open(fname) as f:
        lines = f.readlines()
        for i in range(0, len(lines), 4):
            a = [int(x[x.index('+')+1:]) for x in lines[i].split(',', 2)]
            b = [int(x[x.index('+')+1:]) for x in lines[i+1].split(',', 2)]
            prize = [int(x[x.index('=')+1:]) for x in lines[i+2].split(',', 2)]
            yield (a[0], a[1], b[0], b[1], prize[0], prize[1])

def win_machine(machine, offset = 0):
    ax, ay, bx, by, px, py = machine
    px, py = px + offset, py + offset
    a = (px * by - bx * py) / (ax * by - bx * ay)
    b = (py - ay * a) / by

    is_integer = lambda a: math.floor(a) == math.ceil(a)
    result = 0
    if is_integer(a) and is_integer(b):
        result = int(a) * 3 + int(b)

    return result

def main():
    fname = sys.argv[1]

    result1 = 0
    result2 = 0

    for machine in read_input(fname):
        result1 += win_machine(machine)
        result2 += win_machine(machine, 10000000000000)


    print('part1 = ', result1)
    print('part2 = ', result2)

if __name__ == "__main__":
    main()
