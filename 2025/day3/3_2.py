import sys

def joltage(bank, num):

    if num == 0:
        return 0

    max, imax = 0, 0
    for i in range(0, len(bank) - num + 1):

        voltage = int(bank[i])
        if voltage > max:
            max = voltage
            imax = i

    return max * 10**(num-1) + joltage(bank[imax+1:], num - 1)

def main():

    fname = sys.argv[1]
    result = 0

    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            j = joltage(line, 12)
            result += j

    print('result = ', result)

if __name__ == "__main__":
    main()
