import sys
import collections

def generate_xorshift_tables(seed, max):
    seeds, values = {seed: 0}, {0: seed}
    prices, diffs = {0: int(str(seed)[-1])}, {}

    for i in range(1, max - 1):
        seed = (seed ^ (seed << 6)) % max
        seed = (seed ^ (seed >> 5)) % max
        seed = (seed ^ (seed << 11)) % max
        seeds[seed] = i
        values[i] = seed
        prices[i] = int(str(seed)[-1])
        diffs[i] = prices[i] - prices[i - 1]
    diffs[0] = prices[0] - prices[max - 2]

    return seeds, values, prices, diffs
    
def main():
    fname = sys.argv[1]

    max = 16777216 # 2 ** 24
    seed = 1

    seeds, _, prices, diffs = generate_xorshift_tables(seed, max)

    result = (0, 0, 0, 0)
    max_bananas = 0 
    imax = max - 1
    diffs_count = collections.defaultdict(int)
    for line in open(fname).readlines():
        seed = int(line.strip())
        pos = seeds[seed]
        seen_diffs = {}
        for i in range(pos + 4, pos +2000 + 1):
            last_4_diffs = (diffs[(i - 3) % imax], diffs[(i - 2) % imax], diffs[(i - 1) % imax], diffs[i % imax])
            if last_4_diffs not in seen_diffs:
                seen_diffs[last_4_diffs] = 1
                diffs_count[last_4_diffs] += prices[i % imax]
                if diffs_count[last_4_diffs] > max_bananas:
                    max_bananas = diffs_count[last_4_diffs]
                    result = last_4_diffs

    print('max 4 diffs = ', result)
    print('result = ', max_bananas)

if __name__ == "__main__":
    main()
