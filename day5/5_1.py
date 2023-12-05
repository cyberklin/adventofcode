import sys

def parse_file(fname):
    
    seeds = []
    maps = {}
    with open(fname) as f:
        seeds = list(map(int, f.readline().split(':', 2)[1].split()))
        m_name = ''
        m = [] 
        for line in f:
            line = line.rstrip('\n')
            if line == '' and m_name:
                src,dst = m_name.split('-to-', 2)
                maps[src] = {'map': m, 'to': dst}
            elif line[-5:] == ' map:':
                m_name = line.split()[0]
                m = []
            else: 
                m.append(list(map(int, line.split())))

        if m_name:
            src,dst = m_name.split('-to-', 2)
            maps[src] = {'map': m, 'to': dst}

    return seeds, maps


def main():
    fname = sys.argv[1]
    sum = 0

    seeds, maps = parse_file(fname)

    min_location = 999999999
    for seed in seeds:
        src = 'seed'
        value = seed 
        while src != 'location':
            m = maps[src]
            for r in m['map']:
                if value >= r[1] and value < r[1] + r[2]:
                    value = r[0] + (value - r[1])
                    break
            src = m['to']
        if value < min_location:
            min_location = value

    print("min_location = {}", min_location)

if __name__ == "__main__":
    main()
