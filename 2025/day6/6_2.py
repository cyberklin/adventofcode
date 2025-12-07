import sys

def read_input(fname):
 
    lines = []
    with open(fname) as f:
        for line in f:
            lines.append(line.rstrip('\n'))
            
    return lines, len(lines), len(lines[0])

def main():

    lines, n, m = read_input(sys.argv[1])

    result = 0
    op_result = 0
    op = ''

    for i in range(0, m):
        if lines[n - 1][i] != ' ':
            result += op_result
            op = lines[n - 1][i]
            op_result = op_result = 1 if op == '*' else 0
        
        number = ''
        for j in range(n - 2, -1, -1):
            if lines[j][i] != ' ':
                number = lines[j][i] + number
            
        if number:
            next = int(number)
            op_result = (op_result * next) if op == '*' else (op_result + next)
    
    result += op_result

    print('result = ', result)

if __name__ == "__main__":
    main()
