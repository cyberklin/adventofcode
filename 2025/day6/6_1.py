import sys

def read_input(fname):
 
    lines = []
    with open(fname) as f:
        for line in f:
            line = list(filter(None, line.rstrip('\n').split(' ')))
            lines.append(line)
            
    return lines, len(lines), len(lines[0])

def main():

    lines, n, m = read_input(sys.argv[1])

    result = 0
    for i in range(0, m):
        op = lines[n - 1][i]
        op_result = 1 if op == '*' else 0
        for j in range(n - 2, -1, -1):
            next = int(lines[j][i])
            op_result = (op_result * next) if op == '*' else (op_result + next)
        result += op_result

    print('result = ', result)

if __name__ == "__main__":
    main()
