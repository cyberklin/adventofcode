import sys

def check_report(levels, skip = -1):
    good_report = 1
    delta = 0
    i = 1 if skip == 0 else 0
    j = i + 1
    while j < len(levels):
        if j == skip:
            j = j + 1
            continue

        new_delta = int(levels[j]) - int(levels[i])
        valid_delta = 0 < abs(new_delta) < 4 and (delta * new_delta) >= 0
        if not valid_delta:
            good_report = 0
            break
        delta = new_delta
        i = j
        j = j + 1

    return good_report

def main():
    fname = sys.argv[1]

    result = 0

    with open(fname) as f:
        for line in f:
            report = line.rstrip('\n')
            levels = report.split(' ')
            for i in range(-1, len(levels)):
                if check_report(levels, i):
                    result += 1
                    break

    print('result = ', result)

if __name__ == "__main__":
    main()
