import sys
import math

def predict_value(values):

    ret = 0
    all_values = [values]
    cur_values = values

    while True:
        all_zeros = True
        deltas = [] 
        for i in range(1, len(cur_values)):
            delta = cur_values[i] - cur_values[i-1]
            deltas.append(delta)
            if delta != 0:
                all_zeros = False

        all_values.append(deltas)
        cur_values = deltas
        if all_zeros:
            break

    # climb up
    for i in range(len(all_values) - 1, 0, -1):
        next_value = all_values[i][-1] + all_values[i - 1][-1]
        all_values[i - 1].append(next_value)

    ret = all_values[0][-1]
    return ret

def main():
    fname = sys.argv[1]

    result = 0

    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            values = list(map(int, line.split()))
            next_value = predict_value(values)
            result += next_value

    print("result = {}", result)

if __name__ == "__main__":
    main()
