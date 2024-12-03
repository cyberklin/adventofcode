import sys
import collections

def get_matches(line):

    num_parts = line.split(':', 2)[1].split('|') 
    winning, our = list(map(lambda x: [y.strip() for y in x.split(' ') if y != ''], num_parts))
    return len(list(set(winning) & set(our)))

def main():
    fname = sys.argv[1]
    cards = 0
    copies = collections.defaultdict(int)
    n = 0
    with open(fname) as f:
        for line in f:
            n = n + 1
            matches = get_matches(line)
            for i in range(n + 1, n + 1 + matches):
#                print('add',copies[n] + 1,'for card',i)
                copies[i] = copies[i] + copies[n] + 1

    total_copies = sum(copies.values())
    print(n, 'cards',total_copies,'copies',n+total_copies,'total')


if __name__ == "__main__":
    main()
