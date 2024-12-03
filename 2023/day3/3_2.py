import sys
#import collections

matrix = [] 

def read_matrix(fname):
    with open(fname) as f:
        length = -1
        i = 0
        for line in f:
            line = line.rstrip()
            matrix.append(line)
            if length >= 0 and len(line) != length:
                print(line)
                print("line above has different length from expected, exiting")
                sys.exit(2)
            length = len(line)
            i = i + 1

def print_matrix():
    for line in matrix:
        print(line)

def parse_numbers(string):
    #takes string and retuns all numbers as [{'pos':position,'num':number}]
    ret = [] 

    length = len(string)
    is_digit = False # if current char digit
    buf_number = '' # buffer for number being read 
    position = -1 # pos of first digit for num currently in buf
    i = 0

    #print("parsing ", string)
    while i < length:
        is_digit = string[i].isdigit()

        if is_digit:
            if position == -1: position = i # first digit
            buf_number = buf_number + string[i]

        # we should finish if it's a digit it's the last symbol of the row
        is_last_digit = is_digit and i == length - 1
        # or if we found first non-digit after digit
        is_num_finished = (position != -1) and not is_digit
        if is_last_digit or is_num_finished:
            # we finished reading number
            ret.append({'pos': position, 'num': int(buf_number)})

            # reset state
            buf_number = ''
            is_buf_number_adjacent = False
            position = -1

        i = i + 1

    return ret

def expand_number(i, j):
    # i, j - coordinates of one digit from number 
    # we look for the whole number and return it

    # move left to find beginnig
    start = j
    while start >= 0 and matrix[i][start].isdigit():
        start = start - 1

    # move right to find end
    length = len(matrix[i])
    end = j
    while end < length and matrix[i][end].isdigit():
        end = end + 1

    #print('expanding:', [i, j, matrix[i][j], start, end, matrix[i][start + 1 : end]])
    number = int(matrix[i][start + 1 : end])
    
    return number

def get_gear(i, j, m, n):
    ret = [] 

    if matrix[i][j] != '*':
        return ret

    # area to look for numbers
    top_left = [max(i-1,0),max(j-1,0)]
    bottom_right = [min(i+1,n-1),min(j+1,m-1)]

    adj_numbers = []
    # got through rows of that area
    for x in range(top_left[0], bottom_right[0] + 1):
        # get all numbers from each row of our area
        row = matrix[x][top_left[1]:bottom_right[1]+1]
        numbers = parse_numbers(matrix[x][top_left[1]:bottom_right[1]+1])
        for num in numbers:
            position = [x, num['pos'] + top_left[1]]
            adj_numbers.append({'pos': position, 'num': num['num']})

    if len(adj_numbers) != 2:
        return ret

    adj_numbers_expanded = []
    ratio = 1
    for num in adj_numbers:
        expanded_number = expand_number(num['pos'][0], num['pos'][1])
        ratio = ratio*expanded_number
        adj_numbers_expanded.append(expanded_number)
        
    ret = {'pos': [i, j], 'numbers': adj_numbers_expanded, 'ratio': ratio}
    return ret

def find_gears():
    gears = []

    if not matrix:
        return gears

    # matrix len, width + loop counters
    n, m, i = len(matrix), len(matrix[0]), 0

    while i < n:
        #print("------ row ", i + 1)
        j = 0
        while j < m:
            gear = get_gear(i, j, n, m)
            if gear:
                gears.append(gear)
            j = j + 1
        i = i + 1

    return gears

def main():
    if len(sys.argv) < 2:
        print("Usage: ", sys.argv[0], " INPUT_FILE")
        sys.exit(1)
    fname = sys.argv[1]
    read_matrix(fname)
#    print_matrix()
    gears = find_gears()

    sum = 0
    for gear in gears:
        print(gear) 
        sum = sum + gear['ratio']

    print("sum = {}", sum)



if __name__ == "__main__":
    main()
