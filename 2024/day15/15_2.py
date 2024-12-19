import sys
import collections
import math

def read_input(fname):

    field, start, cmds = [], (0,0), []
    map = {'O': '[]', '#': '##', '.': '..', '@': '@.'}

    with open(fname) as f:
        line = f.readline().strip()
        while line != '':
            field.append(list(''.join(map[c] for c in line)))
            if '@' in field[-1]:
                start = (len(field)-1,field[-1].index('@'))
            line = f.readline().strip()
        for line in f:
            cmds.extend(list(line.strip()))

    return field, start, cmds

MOVES = {
    '^'    : [-1,  0],
    '>' : [ 0, +1],
    'v'  : [+1,  0],
    '<'  : [ 0, -1],
}

def get_next_pos(pos, move):
    return (pos[0] + MOVES[move][0], pos[1] + MOVES[move][1])

class Warehouse:
    def __init__(self, field, start, cmds):
        self.field = field
        self.start = start
        self.cmds = cmds

    def can_move(self, pos, move):
        next_pos = get_next_pos(pos, move)
        next_tile = self.field[next_pos[0]][next_pos[1]]
        if next_tile == '.':
            return True
        elif next_tile == '#':
            return False
        else:
            left = next_pos if next_tile == '[' else get_next_pos(next_pos, '<')
            right = next_pos if next_tile == ']' else get_next_pos(next_pos, '>')
            if move == '<':
                return self.can_move(left, '<')
            elif move == '>':
                return self.can_move(right, '>')
            elif move == '^':
                return self.can_move(left, '^') and self.can_move(right, '^')
            elif move == 'v':
                return self.can_move(left, 'v') and self.can_move(right, 'v')
        return False
    
    def move(self, pos, move):
        next_pos = get_next_pos(pos, move)
        next_tile = self.field[next_pos[0]][next_pos[1]]
        if next_tile != '.':
            left = next_pos if next_tile == '[' else get_next_pos(next_pos, '<')
            right = next_pos if next_tile == ']' else get_next_pos(next_pos, '>')
            if move == '<':
                self.move(left, '<')
                self.move(right, '<')
            elif move == '>':
                self.move(right, '>')
                self.move(left, '>')
            elif move == '^':
                self.move(left, '^')
                self.move(right, '^')
            elif move == 'v':
                self.move(left, 'v')
                self.move(right, 'v')

        self.field[next_pos[0]][next_pos[1]] = self.field[pos[0]][pos[1]]
        self.field[pos[0]][pos[1]] = '.'
    
    def run(self):
        pos = self.start
        for cmd in self.cmds:
            if self.can_move(pos, cmd):
                self.move(pos, cmd)
                self.field[pos[0]][pos[1]] = '.'
                pos = get_next_pos(pos, cmd)
                self.field[pos[0]][pos[1]] = '@'

    def print(self):
        for row in self.field:
            print(''.join(row))

    def score(self):
        result = 0
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if self.field[i][j] == '[':
                    result += i * 100 + j
        return result

def main():
    fname = sys.argv[1]

    field, start, cmds = read_input(fname)
    
    W = Warehouse(field, start, cmds)
    W.run()
    print('result =',W.score())

if __name__ == "__main__":
    main()
