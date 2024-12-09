import sys
import collections
import math 

class Block:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data

class Memory:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        N = Block(data)
        if self.head == None:
            self.head = N
        if self.tail != None:
            N.prev = self.tail
            self.tail.next = N
        self.tail = N

    def addAfter(self, B, data):
        New = Block(data)
        New.next = B.next
        New.prev = B
        if B.next:
            B.next.prev = New
        B.next = New
        if self.tail == B:
            self.tail = New

    def remove(self, B):
        if self.head == B:
            self.head = B.next
            B.next.prev = None
        elif self.tail == B:
            self.tail = B.prev
            B.prev.next = None
        else:
            B.prev.next = B.next
            B.next.prev = B.prev

    def get_tail(self):
        return self.tail

    def get_head(self):
        return self.head

def read_input(fname):
    line = open(fname).read().rstrip()
    M = Memory()
    pos = 0
    length = len(line)
    if length % 2 != 0:
        line += '0'
    for i in range(0, len(line) // 2):
        M.append([pos, i, int(line[i*2]), int(line[i*2+1])])
        pos += int(line[i*2]) + int(line[i*2+1])
    return M

def main():
    fname = sys.argv[1]

    M = read_input(fname)
    result = 0

    moved = collections.defaultdict(int)
    Block = M.get_tail()
    while Block:
        b_pos, b_fid, b_flen, b_slen = Block.data
        if not moved[b_fid]: 
            Space = M.get_head()
            while Space:
                s_pos, s_fid, s_flen, s_len = Space.data
                if s_pos >= b_pos:
                    break 
                if s_len >= b_flen: 
                    # move file
                    Space.data[3] = 0
                    new_data = [s_pos + s_flen, b_fid, b_flen, s_len - b_flen]
                    M.addAfter(Space, new_data)
                    Block.prev.data[3] += b_flen + b_slen
                    M.remove(Block)
                    moved[b_fid] = 1
                    break
                Space = Space.next

        Block = Block.prev

    Block = M.get_head()
    while(Block):
        b_pos, b_fid, b_flen, b_slen = Block.data
        for i in range(0, b_flen):
            result += (b_pos + i)*b_fid
        Block = Block.next
    print('result = ', result)

if __name__ == "__main__":
    main()
