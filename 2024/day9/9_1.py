import sys
import collections

def read_input(fname):
    line = open(fname).read().rstrip()
    files, spaces = collections.deque(), collections.deque()
    for i in range(0, len(line)):
        if (i % 2 == 0):
            files.append((i // 2, int(line[i])))
        else:
            spaces.append(int(line[i]))
    return files, spaces


def main():
    fname = sys.argv[1]

    files, spaces = read_input(fname)

    result = 0
    pos = 0
    while len(files): 
        fid,length = files.popleft()
        for i in range(0, length):
            result += pos*fid
            pos += 1
        space = spaces.popleft()
        for i in range(0, space):
            if len(files):
                fid,length = files.pop()
                result += pos*fid
                pos += 1
                length -= 1
                if length > 0: 
                    files.append((fid, length))

    print('result = ', result)

if __name__ == "__main__":
    main()
