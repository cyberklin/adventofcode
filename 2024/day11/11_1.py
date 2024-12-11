import sys

def main():
    fname = sys.argv[1]

    result = 0
    stones = list(map(int, open(fname).readline().rstrip('\n').split(' ')))

    for step in range(25):
        for i in range(len(stones)):
            s = str(stones[i])
            if s == '0':
                stones[i] = 1
            elif len(s) % 2 == 0:
                stones[i] = int(s[:len(s)//2])
                stones.append(int(s[len(s)//2:]))
            else:
                stones[i] = stones[i]*2024

    result = len(stones)
    print('result = ', result)


if __name__ == "__main__":
    main()
