import sys
import collections

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
            perimeter, count = 0, 0
            area = {}
            while len(q):
                x, y = q.popleft()
                if area.get((x,y), 0):
                    continue
                count += 1
                area[(x,y)] = 1
                visited[(x,y)] = 1
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_x, new_y = x + dx, y + dy
                    if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                        perimeter += 1
                    elif field[x][y] != field[new_x][new_y]:
                        perimeter += 1
                    else:
                        q.append((new_x, new_y))

            result += perimeter * count
            
                    

    print('result = ', result)

if __name__ == "__main__":
    main()
