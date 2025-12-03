import sys

def joltage(bank):
    max1, max2 = 0, 0
    for i in range(0, len(bank)):
        voltage = int(bank[i])
        if i < len(bank) - 1 and voltage > max1: 
            max1 = voltage
            max2 = int(bank[i+1])
        elif voltage > max2:
            max2 = voltage

    return max1 * 10 + max2

def main():

    fname = sys.argv[1]

    result = 0

    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            j = joltage(line)
            result += j

    print('result = ', result)

if __name__ == "__main__":
    main()
