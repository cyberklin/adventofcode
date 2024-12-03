import sys
import math

def parse_file(fname):

    races = []
    with open(fname) as f:

        times = list(map(int, f.readline().replace(' ', '').split(':', 2)[1].split()))
        distances = list(map(int, f.readline().replace(' ', '').split(':', 2)[1].split()))

        races = [(times[i], distances[i]) for i in range(0, len(times))]

    return races

def count_ints_in_range(x1, x2):
    ret = 0
    y = max(x1, x2)
    x = min(x1, x2)
    if int(y) - int(x) != 0:
        if y - int(y) == 0: # y is Z
            ret = int(y) - int(x) - 1
        else:
            ret = int(y) - int(x)
    return ret
    

def calc_wins(race):
    time = race[0]
    dist = race[1]
    ret = 0

    d = time**2 - 4*dist 
    if d > 0: 
        a1 = (time+d**(1/2))/2
        a2 = (time-d**(1/2))/2

        ret = count_ints_in_range(a2, a1)

    return ret


def main():
    fname = sys.argv[1]
    total_wins = 1

    races = parse_file(fname)

    for race in races:
        wins = calc_wins(race)
#        print('race',race,'wins',wins)
        total_wins *= wins

    print("total = {}", total_wins)

if __name__ == "__main__":
    main()
