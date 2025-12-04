import sys
import copy

MOVES = [
    [-1,  0], # UP
    [-1, +1], # UP RIGHT 
    [ 0, +1], # RIGHT
    [+1, +1], # DOWN RIGHT
    [+1,  0], # DOWN
    [+1, -1], # DOWN LEFT
    [ 0, -1], # LEFT 
    [-1, -1], # UP LEFT
]

def read_input(fname):
 
    coords = {}
    n, m = 0, 0
    with open(fname) as f:
        for line in f:
            line = line.rstrip('\n')
            m = 0 
            for s in line:
                if s == '@': 
                    coords[(n,m)] = 1
                m += 1
            n += 1  

    return coords, n, m

def main():

    forklifts, n, m = read_input(sys.argv[1])
    result = 0
    
    step_result = 1
    while step_result:
        step_result = 0
        next_state = copy.deepcopy(forklifts)
        for x, y in forklifts:
            adj_count = sum(1 for dx, dy in MOVES if (x+dx, y+dy) in forklifts)
            if adj_count < 4: 
                step_result += 1
                del next_state[(x, y)]
        forklifts = next_state
        result += step_result

    print('result = ', result)

if __name__ == "__main__":
    main()
