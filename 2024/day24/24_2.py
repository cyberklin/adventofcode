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
        return '"' + self.op1 + ' ' + self.cmd + ' ' + self.op2 + '"'

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

    def reset(self):
        self.values = {self.op1: None, self.op2: None}

def parse_file(fname):

    with open(fname) as f:
        inputs = {}
        gates = []
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
            gates.append(Gate(in1, in2, cmd, out))
            if out[0] == 'z':
                outputs[out] = 1

    return inputs, gates, outputs

def expand(gates, gates_by_input, gates_by_output, gate):
    input1, input2 = gate.op1, gate.op2
    if input1[0] != 'x' and input1[0] != 'y':
        input1 = expand(gates, gates_by_input, gates_by_output, gates_by_output[input1][0])
    if input2[0] != 'x' and input2[0] != 'y':
        input2 = expand(gates, gates_by_input, gates_by_output, gates_by_output[input2][0])

    cmd = '^' if gate.cmd == 'XOR' else '&' if gate.cmd == 'AND' else '|'
    return '(' + input1 + ' ' + cmd + ' ' + input2 + ')'

def main():
    fname = sys.argv[1]

    signals, gates, outputs = parse_file(fname)

    gates_by_input = collections.defaultdict(list)
    gates_by_output = collections.defaultdict(list)

    for g in gates:
        gates_by_input[g.op1].append(g)
        gates_by_input[g.op2].append(g)
        gates_by_output[g.out].append(g)

    for s, v in signals.items():
        for g in  gates_by_input[s]:
            print('start ->',str(g),';')

    for g in gates:
        for g2 in gates_by_input[g.out]:
            print(str(g),"->",str(g2),';')

    for o in outputs:
        for g in gates_by_output[o]:
            print(str(g),"->",o,';')

    for z in range(46):
        o = 'z' + "{0:0=2d}".format(z)
        g = gates_by_output[o][0]
        expanded = expand(gates, gates_by_input, gates_by_output, g)
        bit_num = int(o[1:])

        sums = [(0b1111111111111111111111111111111111111111,0b1111111111111111111111111111111111111111)]
        for s in sums:
            a, b = s[0], s[1]
            c = a + b
            for i in range(45):
                num = "{0:0=2d}".format(i)
                a_bit = (a & (2 ** i)) >> i
                b_bit = (b & (2 ** i)) >> i
                expanded = expanded.replace('x' + num, str(a_bit))
                expanded = expanded.replace('y' + num, str(b_bit))
            expected = (c & (2 ** bit_num)) >> bit_num
            actual = eval(expanded)
            if actual != expected:
                print('actual=',actual,'expected=',expected)
                print(o,' not expected', "{0:b}".format(a), "{0:b}".format(b), "{0:b}".format(c))

if __name__ == "__main__":
    main()
