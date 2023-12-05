import sys
import collections

def parse_file(fname):
    
    seeds = []
    maps = []
    with open(fname) as f:
        ranges = list(map(int, f.readline().split(':', 2)[1].split()))
        i = 0 
        while i < len(ranges):
            seeds.append([ranges[i], ranges[i+1]])
            i = i + 2

        m_name = ''
        m = [] 
        for line in f:
            line = line.rstrip('\n')
            if line == '' and m_name:
                src,dst = m_name.split('-to-', 2)
                maps.append({'ranges': m, 'to': dst, 'from':src})
            elif line[-5:] == ' map:':
                m_name = line.split()[0]
                m = []
            else: 
                m.append(list(map(int, line.split())))

        if m_name:
            src,dst = m_name.split('-to-', 2)
            maps.append({'ranges': m, 'to': dst, 'from':src})

    return seeds, maps

def apply_map_range(seed_range, map_range):
    mapped_range = []
    unmapped_ranges = []

    r = seed_range
    r_left, r_right = r[0], r[0] + r[1] - 1
    map_left, map_right, map_shift = map_range[1], map_range[1] + map_range[2] - 1, map_range[0] - map_range[1]

    if map_left <= r_left:
        if map_right >= r_right: # all r is inside the map
            mapped_range = [r_left + map_shift, r[1]]
            unmapped_ranges = []
        elif map_right >= r_left: # map_right splits r in 2
            mapped_range = [r_left + map_shift, map_right - r_left + 1]
            unmapped_ranges = [[map_right + 1, r_right - map_right]]
        else: # no overlap, put back r for other map_ranges
            unmapped_ranges = [r]
    elif map_left > r_right: # no overlap, put back r for other map_ranges
            unmapped_ranges = [r]
    else: # map_left > r_left && map_left <= r_right
        if map_right >= r_right: # map_left splits r in 2
            mapped_range = [map_left + map_shift, r_right - map_left + 1]
            unmapped_ranges = [[r_left, map_left - r_left]]
        else: # map inside r, so splitting into 3
            mapped_range = [map_left + map_shift, map_right - map_left + 1]
            unmapped_ranges = [[r_left, map_left - r_left], [map_right + 1, r_right - map_right]]

    return mapped_range, unmapped_ranges

def apply_map(r, m):

    ret = []
    ranges = [r]
    for map_range in m['ranges']:
        next_ranges = [] 
        for cur_range in ranges:

            mapped, unmapped = apply_map_range(cur_range, map_range)
            if mapped: 
                ret.append(mapped)
            next_ranges = next_ranges + unmapped
        ranges = next_ranges 

    ret = ret + ranges

    return ret

def main():
    fname = sys.argv[1]
    sum = 0

    seeds, maps = parse_file(fname)

    ranges = seeds
    for m in maps:
        new_ranges = []
        for r in ranges:
            mapped = apply_map(r, m)
            new_ranges = new_ranges + mapped

        ranges = new_ranges
            
    min_location = 99999999999
    for i in ranges:
        if i[0] < min_location:
            min_location = i[0]

    print("min_location = {}", min_location)

if __name__ == "__main__":
    main()
