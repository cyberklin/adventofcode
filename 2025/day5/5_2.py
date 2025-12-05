import sys

def merge_ranges(ranges):

    merged = True
    while merged:
        merged = False
        for i in range(0, len(ranges) - 1):
            r1 = ranges[i]
            for j in range(i + 1, len(ranges)):
                r2 = ranges[j]
                separate = r1[1] < r2[0] or r1[0] > r2[1]
                if not separate: 
                    merged_range = (min(r1[0], r2[0]), max(r1[1], r2[1]))
                    ranges = ranges[:i] + ranges[i+1:j] + [merged_range] + ranges[j+1:]
                    merged = True
                    break
            if merged:
                break
                
    return ranges

def read_input(fname):
 
    ranges, ids = [], []
    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            if not line: 
                break
            range = tuple(map(int, line.split('-',2)))
            ranges.append(range)
        for line in f:
            ids.append(int(line.rstrip('\n')))
            
    return ranges, ids

def main():

    ranges, _ = read_input(sys.argv[1])
    ranges = merge_ranges(ranges)

    result = 0
    for r in ranges:
        result += r[1] - r[0] + 1

    print('result = ', result)

if __name__ == "__main__":
    main()
