import sys

def read_input():

    fname = sys.argv[1]

    max = 0 
    ranges = []     

    with open(fname) as f:
        for line in f:
            str_ranges = line.rstrip('\n').split(',')
            for range in str_ranges:
                start, end = map(int, range.split('-',2))
                ranges.append((start, end))
                if end > max:
                    max = end

    return ranges, max

def main():

    ranges, max = read_input()

    result = 0

    for i in range(0, max):
        num = int(str(i) + str(i))
        if num > max:
            break
        for (start, end) in ranges:
            if num >= start and num <= end:
                result += num
                continue
        
    print('result = ', result)

if __name__ == "__main__":
    main()
