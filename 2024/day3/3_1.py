import sys
import re

def main():
    fname = sys.argv[1]

    result = 0

    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            muls = re.findall(r'mul\((\d+)\,(\d+)\)', line)
            for a, b in muls:
                result += int(a) * int(b)

    print('result = ', result)

if __name__ == "__main__":
    main()
