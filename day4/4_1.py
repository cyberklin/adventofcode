import sys

def parse_line(line):

    num_parts = line.split(':', 2)[1].split('|') 
    return list(map(lambda x: [y.strip() for y in x.split(' ') if y != ''], num_parts))

def main():
    fname = sys.argv[1]
    sum = 0
    with open(fname) as f:
        for line in f:
            winning, our = parse_line(line)
            matches = len(list(set(winning) & set(our)))
            points = 2**(matches - 1) if matches > 0 else 0
            sum = sum + points

    print("sum = {}", sum)

if __name__ == "__main__":
    main()
