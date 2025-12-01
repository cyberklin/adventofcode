import sys

def get_delta():

    fname = sys.argv[1]

    with open(fname) as f:

        for line in f:

            line = line.rstrip('\n')
            direction = -1 if line[0] == 'L' else 1
            number = int(line[1:])
            yield direction * number

def main():

    position = 50
    count = 0
    for delta in get_delta():
        print("position %d, delta %d" % (position, delta))
        position = (position + delta) % 100
        if position == 0:
            count = count + 1

    print('password = ', count)

if __name__ == "__main__":
    main()
