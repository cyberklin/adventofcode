import sys
import collections

UP    = 1
RIGHT = 2
DOWN  = 4
LEFT  = 8

MOVES = {
    UP    : [-1,  0],
    RIGHT : [ 0, +1],
    DOWN  : [+1,  0],
    LEFT  : [ 0, -1],
}

def get_next_coords(coords, direction):
    diff = MOVES[direction]
    return (coords[0] + diff[0], coords[1] + diff[1])

def turn_right(direction):
    return direction << 1 if direction != LEFT else UP

def turn_left(direction):
    return direction >> 1 if direction != UP else LEFT

def get_value(matrix, coords):
    i, j = coords
    if i >=0 and i < len(matrix) and j >= 0 and j < len(matrix[i]):
        return matrix[i][j]
    else:
        return ''

def get_sides(field, n, m, perimeter):
    sides_num = 0
    visited = { }

    for cur_pos, cur_dir in perimeter: 

        cur_dir = turn_right(cur_dir)
        while not visited.get((cur_pos,cur_dir), 0):
            visited[(cur_pos,cur_dir)] = 1
            next_pos_forward = get_next_coords(cur_pos, cur_dir)
            next_pos_left = get_next_coords(cur_pos, turn_left(cur_dir))
            cur_value = get_value(field, cur_pos)
            can_go_forward = cur_value == get_value(field, next_pos_forward)
            can_go_left = cur_value == get_value(field, next_pos_left)
            if can_go_left:
                cur_pos = next_pos_left
                cur_dir = turn_left(cur_dir)
                sides_num += 1
            elif can_go_forward:
                cur_pos = next_pos_forward
            else: 
                cur_dir = turn_right(cur_dir)
                sides_num += 1

    return sides_num

def main():
    fname = sys.argv[1]

    field = [list(line.strip()) for line in open(fname)]
    n, m = len(field), len(field[0])
    result = 0
    visited = {} 

    for i in range(n):
        for j in range(m):
            pos = (i, j)
            if visited.get(pos, 0):
                continue
            
            visited[pos] = 1
            q = collections.deque()
            q.append(pos)
            perimeter, count = [], 0
            area = {}
            while len(q):
                x, y = q.popleft()
                if area.get((x,y), 0):
                    continue
                count += 1
                area[(x,y)] = 1
                visited[(x,y)] = 1
                for d in [UP, RIGHT, DOWN, LEFT]:
                    new_x, new_y = get_next_coords((x,y), d)
                    if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m or field[x][y] != field[new_x][new_y]:
                        perimeter.append(((x,y), d)) 
                    else:
                        q.append((new_x, new_y))

            sides_num = get_sides(field, n, m, perimeter)
            result += sides_num * count

    print('result = ', result)

if __name__ == "__main__":
    main()
