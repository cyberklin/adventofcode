import sys
import re

def main():
    fname = sys.argv[1]

    result = 0
    memory = ''

    with open(fname) as f:
        for line in f:
            memory += line.rstrip('\n')

    do_parts= memory.split('do()')
    for do_part in do_parts:
        do_part = do_part.split('don\'t()')[0]
        muls = re.findall(r'mul\((\d+)\,(\d+)\)', do_part)
        for a, b in muls:
            result += int(a) * int(b)

    print('result = ', result)



            

if __name__ == "__main__":
    main()
