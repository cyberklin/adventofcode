import sys
    
def main():
    fname = sys.argv[1]

    max = 16777216 # 2 ** 24
    seed = 1
    seeds, values = {1: 0}, {0: 1}
    for i in range(1, max - 1):
        seed = (seed ^ (seed << 6)) % max
        seed = (seed ^ (seed >> 5)) % max
        seed = (seed ^ (seed << 11)) % max
        seeds[seed] = i
        values[i] = seed

    result = 0
    for line in open(fname).readlines():
         seed = int(line.strip())
         pos = seeds[seed]
         next_pos = (pos + 2000) % (max - 1)
         nth = values[next_pos]
         result += nth
         
    print('result = ', result)

if __name__ == "__main__":
    main()