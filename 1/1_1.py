import sys

def find_digit(line, r):
    ret = -1
    for i in r:
        if line[i].isnumeric():
            ret = line[i]
            break
    return ret

def main():
    fname = sys.argv[1]
    sum = 0
    with open(fname) as f:
        for line in f:
            print(line, end='')
            first = find_digit(line, range(0, len(line) - 1))
            last = find_digit(line, range(len(line) - 1, -1, -1))
            print("first = ", first, ", last = ", last)
            if first == -1 or last == -1:
                print("error: ", line, end='')
            value = int(first + last)
            sum = sum + value


    print("sum = {}", sum)



if __name__ == "__main__":
    main()
