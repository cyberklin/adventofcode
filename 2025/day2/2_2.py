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
    ids_found = {}

    for i in range(1, max):
        num = int(str(i) + str(i))
        if num > max:
            break        
        while num < max: 
            if num not in ids_found:
                for (start, end) in ranges:
                    if num >= start and num <= end:
                        result += num
                        ids_found[num] = 1
                        continue 
       
            num = int(str(num) + str(i))


        
    print('result = ', result)

if __name__ == "__main__":
    main()
