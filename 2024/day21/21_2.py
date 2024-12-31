import sys
import collections
import math

def calc_routes_from_to(field, start, end, prefix = ''):
    result = []

    if start == end:
        return [prefix]
    
    dx, dy = end[0] - start[0], end[1] - start[1]
    next_steps = []
    if dx < 0 and field[start[0] - 1][start[1]] != '#':
        next_steps.append(('^', (start[0] - 1, start[1])))
    elif dx > 0 and field[start[0] + 1][start[1]] != '#':
        next_steps.append(('v', (start[0] + 1, start[1])))
    if dy < 0 and field[start[0]][start[1] - 1] != '#':
        next_steps.append(('<', (start[0], start[1] - 1)))
    elif dy > 0 and field[start[0]][start[1] + 1] != '#':
        next_steps.append(('>', (start[0], start[1] + 1)))

    for step in next_steps:
        result.extend(calc_routes_from_to(field, step[1], end, prefix + step[0]))

    return result    

def init_routes(field):
    iter1 = ((i,j) for i in range(len(field)) for j in range(len(field[i])))
    routes = {}
    for (i1,j1) in iter1:
        iter2 = ((i,j) for i in range(len(field)) for j in range(len(field[i])))
        for (i2,j2) in iter2:
            v1, v2 = field[i1][j1], field[i2][j2]
            if v1 == '#' or v2 == '#':
                continue
            if (i1,j1) == (i2,j2):
                routes[(v1, v2)] = ['']
            routes[(v1, v2)] = calc_routes_from_to(field, (i1, j1), (i2, j2))
    return routes

directional_keypad = [
        ['#', '^', 'A'],
        ['<', 'v', '>'],
]

directional_keypad_routes = init_routes(directional_keypad)

numeric_keypad = [
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        ['#', '0', 'A'],
]

numeric_keypad_routes = init_routes(numeric_keypad)

cache = {}

class RobotArm:
    def __init__(self, routes, name):
        self.routes = routes
        self.current = 'A'
        self.name = name

    def press(self, code, current =''):
        if current != '':
            self.current = current

        if len(code) == 0:
            return ['']

        next_key = code[:1]
        routes1 = self.routes[(self.current, next_key)]
        self.current = next_key
        routes2 = self.press(code[1:])
        result = [] 
        for r1 in routes1:
            for r2 in routes2:
                result.append(r1 + 'A' +r2)
        return result

def split_code_to_words(code):
    words = []
    buf = ''
    for char in code:
        buf += char
        if char == 'A':
            words.append(buf)
            buf = ''
    if buf:
        words.append(buf)
    return words    

def get_min_len(arm, code, num_arms):
    global cache

    cache_key = (code,num_arms)
    if cache_key in cache:
        return cache[cache_key]
    
    if num_arms == 0:
        result = len(code)
    else:
        min_len = 0

        words = split_code_to_words(code)
        for word in words:
            candidates = arm.press(word, 'A')
            word_min_len = math.inf
            for c in candidates:
                c_min_len = get_min_len(arm, c, num_arms - 1)
                if c_min_len < word_min_len:
                    word_min_len = c_min_len
            min_len += word_min_len
        result = min_len

    cache[cache_key] = result
    return result
    
def main():
    fname = sys.argv[1]

    result = 0

    for line in open(fname).readlines():
        code = line.strip()
        numeric_arm = RobotArm(numeric_keypad_routes, 'numeric')
        directional_arm = RobotArm(directional_keypad_routes, 'directional')
        
        min_len = 0
        for key in code:
            key_sequences = numeric_arm.press(key)
            key_min_len = math.inf
            for ks in key_sequences:
                encoded_ks_min_len = get_min_len(directional_arm, ks, 25)
                if encoded_ks_min_len < key_min_len:
                    key_min_len = encoded_ks_min_len
            min_len += key_min_len
            
        num_part = int(''.join(filter(str.isdigit, code)))
        code_result = num_part * min_len        
        result += code_result
        print(code,'=', min_len, '*', num_part, '=', code_result)
        
    print('result = ', result)

if __name__ == "__main__":
    main()
