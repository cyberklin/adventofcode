import sys
import collections

CACHE = {} 

def blink(stone, n):
    new_stones = []
    s = str(stone)
    cache_key = s + '_' + str(n)
    if cache_key in CACHE: 
        return CACHE[cache_key]

    if s == '0':
        new_stones.append(1)
    elif len(s) % 2 == 0:
        new_stones.append(int(s[:len(s)//2]))
        new_stones.append(int(s[len(s)//2:]))
    else:
        new_stones.append(stone*2024)

    if n == 1:
        result = len(new_stones)
    else: 
        result = 0
        for ns in new_stones:
            result += blink(ns, n - 1)

    CACHE[cache_key] = result
    return result


def main():
    fname = sys.argv[1]

    stones = list(map(int, open(fname).readline().rstrip('\n').split(' ')))

    result = 0
    for s in stones:
        result += blink(s, 75)

    print('result = ', result)


if __name__ == "__main__":
    main()
