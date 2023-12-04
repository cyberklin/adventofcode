import sys

spelled_digits_dict = {
  # string : corresponding digit
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9',
}

spelled_digits_dict_reversed = {}

for k,v in spelled_digits_dict.items():
    spelled_digits_dict_reversed[k[::-1]] = v # reversed key, same value

def is_spelled_digit(line, digits_dict):
    ret = -1
    for ndl in digits_dict:
        ndl_len = len(ndl)
#        print("checking for ", ndl, " in ", line)
        if ndl_len < len(line) and line[0:ndl_len] == ndl:
            ret = digits_dict[ndl]
            break
    return ret

def find_first_digit(line, spelled_dict):
    ret = -1
    for i in range(0, len(line)):
        if line[i].isnumeric():
            ret = line[i]
            break
        spelled_digit = is_spelled_digit(line[i:], spelled_dict)
        if spelled_digit != -1:
            ret = spelled_digit
            break
#    print("first digit ", ret, " in ", line)
    return ret

def main():

    fname = sys.argv[1]
    sum = 0
    with open(fname) as f:
        for line in f:
            line = line.rstrip()
            print(line)
            first = find_first_digit(line, spelled_digits_dict)
            # last digit is first digit in reversed string (+we use reversed dict as well)
            last = find_first_digit(line[::-1], spelled_digits_dict_reversed)
            print("first = ", first, ", last = ", last)
            if first == -1 or last == -1:
                print("error: ", line)
            value = int(first + last)
            sum = sum + value

    print("sum = {}", sum)



if __name__ == "__main__":
    main()
