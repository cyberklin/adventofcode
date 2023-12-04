import sys
import collections

limit = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def parse_line(line):
    ret = {} 
    game = {}

    split = line.split(':', 2)
    if (len(split) != 2): 
        return ret

    (game_part, sets_part) = split

    game['num'] = game_part[5:]
    if not game['num'].isdigit():
        return ret

    game['num'] = int(game['num'])
    game['sets'] = [] 

    sets = sets_part.split(';')
    for i in sets:
        set = {}
        colours = i.split(',')
        for k in colours:
            colour_parts = k.strip().split(' ', 2)
            if len(colour_parts) != 2 or not colour_parts[0].isdigit():
                return ret

            (colour_num, colour_name) = colour_parts
            set[colour_name] = int(colour_num)

        game['sets'].append(set)

    print(game)
    ret = game
    return ret

def is_possible(game):
    ret = 1
    for set in game['sets']:
        for colour in set:
            # possible means we have that colour and number is >= that we've seen 
            possible = (colour in limit and set[colour] <= limit[colour])
            if not possible:
                ret = 0
        if not ret: # no need to go further if not possible already
            break
    return ret

def calc_power(game):
    min_set = collections.defaultdict(int)
    for set in game['sets']:
        for colour in set:
            if set[colour] > min_set[colour]:
                min_set[colour] = set[colour]

    print(min_set)
    ret = 1 if len(min_set) else 0
    for k in min_set:
        ret = ret*min_set[k]

    print(ret)
    return ret







def main():
    fname = sys.argv[1]
    sum = 0
    with open(fname) as f:
        for line in f:
            line = line.rstrip()
            print(line)
            game = parse_line(line)
            power = calc_power(game)
            sum = sum + power


    print("sum = {}", sum)



if __name__ == "__main__":
    main()
