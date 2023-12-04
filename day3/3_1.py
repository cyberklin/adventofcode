import sys
#import collections

matrix = [] 

def read_matrix(fname):
    with open(fname) as f:
        length = -1
        i = 0
        for line in f:
#            if i > 2: return
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

def is_symbol(char):
    if char == '.':
        return False
    if char.isdigit():
        return False
    return True


def is_symbol_here_up_down(i, j, n):
    if is_symbol(matrix[i][j]): return True
    if i > 0 and is_symbol(matrix[i-1][j]): return True
    if i < n - 1 and is_symbol(matrix[i+1][j]): return True
    return False

def find_parts():
    parts = []

    if not matrix:
        return parts

    # matrix len, width + loop counters
    n, m, i = len(matrix), len(matrix[0]), 0

    while i < n:
        print("------ row ", i + 1)
        # loop counter
        j = 0
        # flags if we have digit in current + prev positions
        is_digit, is_digit_prev = False, False
        # flags if symbol is either here, up or down from current and prev positions
        is_symbol_around, is_symbol_around_prev = False, False
        # buffer to build number
        buf_number = ''
        # flag if current num in buffer adjacent to symbol
        is_buf_number_adjacent = False

        while j < m:
             
            is_digit_prev = is_digit
            is_symbol_around_prev = is_symbol_around

            is_digit = matrix[i][j].isdigit()
            is_symbol_around = is_symbol_here_up_down(i, j, n)

            if is_digit and not is_digit_prev:
                # we start reading number 
                buf_number = buf_number + matrix[i][j]
                if is_symbol_around or is_symbol_around_prev:
                    is_buf_number_adjacent = True
            elif is_digit and is_digit_prev:
                # we continue reading number
                buf_number = buf_number + matrix[i][j]
                if is_symbol_around: 
                    is_buf_number_adjacent = True
           
            # we should finish if it's a digit it's the last symbol of the row
            is_last_digit = is_digit and j == m - 1             
            # or if we found first non-digit after digit
            is_num_finished = is_digit_prev and not is_digit
            if is_last_digit or is_num_finished:
                # we finished reading number
                if is_symbol_around: 
                    is_buf_number_adjacent = True
                if is_buf_number_adjacent:
                    print("we found part number: ", buf_number)
                    parts.append(int(buf_number))

                # reset state
                buf_number = '' 
                is_buf_number_adjacent = False

            j = j + 1

        i = i + 1

    return parts

def main():
    if len(sys.argv) < 2:
        print("Usage: ", sys.argv[0], " INPUT_FILE")
        sys.exit(1)
    fname = sys.argv[1]
    read_matrix(fname)
#    print_matrix()
    parts = find_parts()

    sum = 0
    for i in parts:
        sum = sum + i

    print("sum = {}", sum)



if __name__ == "__main__":
    main()
