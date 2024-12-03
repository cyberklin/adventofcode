import sys

def main():
    fname = sys.argv[1]

    result = 0

    with open(fname) as f:
        for line in f:
            report = line.rstrip('\n')
            levels = report.split(' ')

            delta = 0
            good_report = 1
            for i in range(1, len(levels)):
                new_delta = int(levels[i]) - int(levels[i-1])
                valid_delta = 0 < abs(new_delta) < 4 and (delta * new_delta) >= 0
                if not valid_delta:
                    good_report = 0
                    break
                delta = new_delta
            if good_report:
                result += 1

    print('result = ', result)

if __name__ == "__main__":
    main()
