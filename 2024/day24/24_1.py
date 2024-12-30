import sys
import collections

class Gate:

    def __init__(self, in1, in2, cmd, out):
        self.values = {in1: None, in2: None}
        self.op1 = in1
        self.op2 = in2
        self.cmd = cmd
        self.out = out

    def __str__(self):
        return self.op1 + ' ' + self.cmd + ' ' + self.op2

    def set(self, name, value):
        self.values[name] = value

    def ready(self):
        return self.values[self.op1] is not None and self.values[self.op2] is not None

    def output(self):
        value = None
        if self.cmd == 'AND':
            value = self.values[self.op1] & self.values[self.op2]
        elif self.cmd == 'OR':
            value = self.values[self.op1] | self.values[self.op2]
        elif self.cmd == 'XOR':
            value = self.values[self.op1] ^ self.values[self.op2]
        return (self.out, value)

def parse_file(fname):

    with open(fname) as f:
        inputs = {}
        gates = collections.defaultdict(list)
        outputs = {}
        for line in f:
            line = line.rstrip('\n')
            if line == '':
                break
            name, value  = line.split(': ',2)
            inputs[name] = int(value)
        for line in f:
            line = line.rstrip('\n')
            in1, cmd, in2, _, out = line.split(' ', 5)
            gate = Gate(in1, in2, cmd, out)
            gates[in1].append(gate)
            gates[in2].append(gate)
            if out[0] == 'z':
                outputs[out] = gate

    return inputs, gates, outputs


def main():
    fname = sys.argv[1]

    inputs, gates, outputs = parse_file(fname)

    q = collections.deque()
    for name, value in inputs.items():
        q.append((name, value))

    results = {}

    while len(outputs) and len(q):
        name, value = q.popleft()
        for gate in gates[name]:
            gate.set(name, value)
            if gate.ready():
                output, outvalue = gate.output()
                if output in outputs:
                    results[output] = outvalue
                    del outputs[output]
                else:
                    q.append((output, outvalue))

    result = 0
    for key, value in results.items():
        if value == 1: 
            bitnum = int(key[1:])
            result += 2 ** bitnum
    print('result =', result)

if __name__ == "__main__":
    main()
