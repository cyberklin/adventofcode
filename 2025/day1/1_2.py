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
    passwd = 0
    for delta in get_delta():
        new_position = position + delta
        if delta > 0: 
            zeros = new_position // 100
        else:
            zeros = abs(delta) // 100
            if position > 0 and (abs(delta) % 100) >= position:
                zeros = zeros + 1

        print("position %d, delta %d, new_position %d (%d), zeros %d" % (position, delta, new_position, new_position % 100, zeros))
        position = new_position % 100
        passwd = passwd + zeros

    print('password = ', passwd)

if __name__ == "__main__":
    main()
