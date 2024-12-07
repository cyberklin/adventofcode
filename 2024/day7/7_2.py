import sys
import collections
import math

def check_equation(value, numbers):

    if len(numbers) == 1:
        result = (value == numbers[0])
    else:
        mul_result = check_equation(value, [numbers[0]*numbers[1]] + numbers[2:])
        add_result = check_equation(value, [numbers[0]+numbers[1]] + numbers[2:])
        cc_result = check_equation(value, [int(str(numbers[0]) + str(numbers[1]))] + numbers[2:])
        result = mul_result or add_result or cc_result

    return result


def main():
    fname = sys.argv[1]
    result = 0

    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            value = int(line.split(':', 2)[0])
            numbers = list(map(int, line.split(':', 2)[1].lstrip().split(' ')))
            if check_equation(value, numbers):
                result += int(value)
 
    print('result = ', result)



            

if __name__ == "__main__":
    main()
